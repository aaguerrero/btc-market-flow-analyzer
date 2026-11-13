import asyncio
import websockets
import json
from collections import deque

PAIR = "btcusdt"                 # Par en Binance Futures
THRESHOLD_WHALE = 100_000         # Mínimo en USD para considerar whale
ORDERBOOK_LEVELS = 5             # Niveles de orderbook a analizar
WHALE_WINDOW_SEC= 3              # ventana de acumulación de flujo 
OBI_EWMA_ALPHA = 0.25
OBI_BUY_THRESHOLD = 0.15
OBI_SELL_THRESHOLD = -0.15

COOLDOWN_SEC = 8                 # enfriamiento entre señales

# Guardamos últimas señales para evitar repeticiones
last_signals = deque(maxlen=5)

# Listener de trades (para detectar whales)
async def trades_listener():
    uri = f"wss://fstream.binance.com/ws/{PAIR}@trade"
    while True:
        try:
            async with websockets.connect(uri) as ws:
                async for msg in ws:
                    data = json.loads(msg)
                    price = float(data["p"])
                    qty = float(data["q"])
                    side = "Buy" if data["m"] is False else "Sell"  # m=False → Buyer aggressive
                    value = price * qty

                    if value >= THRESHOLD_WHALE:
                        signal = None
                        if side == "Buy":
                            signal = f"🟢 Whale BUY detectada: ${value:,.0f} @ {price}"
                        else:
                            signal = f"🔴 Whale SELL detectada: ${value:,.0f} @ {price}"

                        if signal and signal not in last_signals:
                            print(signal)
                            last_signals.append(signal)

        except Exception as e:
            print(f"⚠️ Error en trades_listener: {e}. Reintentando...")
            await asyncio.sleep(3)


# Listener del orderbook (para imbalance)
async def orderbook_listener():
    uri = f"wss://fstream.binance.com/ws/{PAIR}@depth5@100ms"  # top 5 niveles, update cada 100ms
    while True:
        try:
            async with websockets.connect(uri) as ws:
                async for msg in ws:
                    data = json.loads(msg)

                    # ✅ Verificamos que tenga bids y asks
                    if "bids" not in data or "asks" not in data:
                        continue

                    bids = [(float(b[0]), float(b[1])) for b in data["bids"]]
                    asks = [(float(a[0]), float(a[1])) for a in data["asks"]]

                    if not bids or not asks:
                        continue

                    bid_vol = sum(q for _, q in bids[:ORDERBOOK_LEVELS])
                    ask_vol = sum(q for _, q in asks[:ORDERBOOK_LEVELS])

                    signal = None
                    if bid_vol > 2 * ask_vol:
                        signal = "🟢 COMPRA detectada: fuerte presión compradora"
                    elif ask_vol > 2 * bid_vol:
                        signal = "🔴 VENTA detectada: fuerte presión vendedora"

                    if signal and signal not in last_signals:
                        print(signal)
                        last_signals.append(signal)

        except Exception as e:
            print(f"⚠️ Error en orderbook_listener: {e}. Reintentando...")
            await asyncio.sleep(3)



# Ejecutamos ambos listeners
async def main():
    await asyncio.gather(
        trades_listener(),
        orderbook_listener()
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Bot detenido manualmente.")
