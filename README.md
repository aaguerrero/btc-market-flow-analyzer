
# BTC Market Flow Analyzer

**Real-Time Bitcoin Market Microstructure Monitor**

A Python-based market monitoring tool that consumes live market data from Binance Futures WebSockets to detect large trades (Whale Activity) and order book imbalances (Buy/Sell Pressure).

The project explores real-time market data processing, asynchronous programming, and quantitative market microstructure analysis.

## 🚀 Features

### 1. Whale Trade Detection
- Monitors the BTCUSDT Futures trade stream.
- Identifies individual trades with a notional value greater than or equal to $100,000 USD.
- Classifies aggressive buyer and seller activity.
- Displays detected whale transactions in the terminal.

### 2. Order Book Imbalance
- Subscribes to Binance Futures depth5 stream.
- Monitors the top five bid and ask price levels.
- Calculates aggregated bid and ask volumes.
- Detects buying or selling pressure when one side exceeds twice the volume of the opposite side.

### 3. Asynchronous Processing
- Uses Python `asyncio` to execute both market data listeners concurrently.
- Uses WebSockets for real-time streaming.
- Implements automatic reconnection after connection errors.
- Uses a deque structure to maintain a limited history of recent signals and reduce repeated notifications.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| asyncio | Asynchronous concurrent execution |
| websockets | Real-time WebSocket communication |
| JSON | Market data parsing |
| collections.deque | Recent signal management |
| Binance Futures API | Public market data source |

## 📡 Market Data Sources

The application consumes two public Binance Futures WebSocket streams:

**Trades Stream**

```text
wss://fstream.binance.com/ws/btcusdt@trade
```

Provides individual trade information, including price, quantity and buyer-maker status.

**Order Book Stream**

```text
wss://fstream.binance.com/ws/btcusdt@depth5@100ms
```

Provides the five best bid and ask levels with updates approximately every 100 milliseconds.

No API key is required for these public market data streams.

## ⚙️ Configuration

The main parameters can be adjusted directly in the Python script.

| Parameter | Default | Description |
|---|---:|---|
| PAIR | btcusdt | Trading pair |
| THRESHOLD_WHALE | 100,000 | Minimum trade value in USD |
| ORDERBOOK_LEVELS | 5 | Order book levels analyzed |
| WHALE_WINDOW_SEC | 3 | Intended whale accumulation window |
| OBI_EWMA_ALPHA | 0.25 | Intended EWMA smoothing factor |
| OBI_BUY_THRESHOLD | 0.15 | Intended buying imbalance threshold |
| OBI_SELL_THRESHOLD | -0.15 | Intended selling imbalance threshold |
| COOLDOWN_SEC | 8 | Intended signal cooldown |

**Note:** The whale accumulation window, EWMA parameters, imbalance thresholds and cooldown are configuration placeholders for the next development iteration. They are not yet implemented in the current detection logic.

## 💻 Installation

### Prerequisites
- Python 3.10 or later.
- Internet connection.
- Git (optional, for cloning the repository).

### 1. Clone the repository

```bash
git clone https://github.com/aaguerrero/btc-market-flow-analyzer.git
cd btc-market-flow-analyzer
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

Linux / Ubuntu:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python bot.py
```

## 📊 Execution

Once started, the application establishes two concurrent WebSocket connections and begins monitoring market activity.

Example terminal output:

```text
🟢 Whale BUY detected: $125,000 @ 102500.50

🔴 Whale SELL detected: $145,000 @ 102480.20

🟢 BUY detected: Strong buying pressure

🔴 SELL detected: Strong selling pressure
```

The application continues running until manually interrupted.

To stop:

```text
CTRL + C
```

## 🏗️ Current Architecture

```text
Binance Futures WebSocket
          |
          +----------------------+
          |                      |
     Trades Stream          Depth5 Stream
          |                      |
   Whale Detection       Order Book Analysis
          |                      |
          +----------+-----------+
                     |
              Signal Detection
                     |
                  Terminal
```

## 🗺️ Development Roadmap

### Phase 1 — Core Market Monitoring
- [x] Binance Futures WebSocket integration.
- [x] Concurrent trade and order book listeners.
- [x] Individual whale trade detection.
- [x] Five-level order book volume aggregation.
- [x] Basic buy/sell pressure detection.
- [x] Automatic reconnection.

### Phase 2 — Quantitative Signal Processing
- [ ] Implement normalized Order Book Imbalance (OBI).
- [ ] Apply EWMA smoothing to OBI.
- [ ] Implement whale trade accumulation within a rolling time window.
- [ ] Implement signal cooldown.
- [ ] Improve duplicate signal management.

### Phase 3 — Market Analytics
- [ ] Correlate whale activity with order book imbalance.
- [ ] Add timestamped signal logging.
- [ ] Store market signals for historical analysis.
- [ ] Evaluate signal reliability against subsequent price movements.

### Phase 4 — Visualization
- [ ] Develop a real-time market monitoring dashboard.
- [ ] Display bid/ask volume distribution.
- [ ] Visualize OBI and whale activity.
- [ ] Build historical signal analytics.

## ⚠️ Disclaimer

This project is an experimental market monitoring and educational tool.

It analyzes publicly available market data and generates indicative market activity signals. It does not execute trades, provide investment advice, or guarantee market direction.

Whale transactions and order book imbalances should not be interpreted as standalone trading signals.

---

**Project Status:** MVP — Initial Development

**Focus:** Python · Real-Time Data Processing · Cryptocurrency Markets · Market Microstructure

# BTC Market Flow Analyzer

**Real-Time Bitcoin Market Microstructure Monitor**

A Python-based market monitoring tool that consumes live market data from Binance Futures WebSockets to detect large trades (Whale Activity) and order book imbalances (Buy/Sell Pressure).

The project explores real-time market data processing, asynchronous programming, and quantitative market microstructure analysis.

## 🚀 Features

### 1. Whale Trade Detection
- Monitors the BTCUSDT Futures trade stream.
- Identifies individual trades with a notional value greater than or equal to $100,000 USD.
- Classifies aggressive buyer and seller activity.
- Displays detected whale transactions in the terminal.

### 2. Order Book Imbalance
- Subscribes to Binance Futures depth5 stream.
- Monitors the top five bid and ask price levels.
- Calculates aggregated bid and ask volumes.
- Detects buying or selling pressure when one side exceeds twice the volume of the opposite side.

### 3. Asynchronous Processing
- Uses Python `asyncio` to execute both market data listeners concurrently.
- Uses WebSockets for real-time streaming.
- Implements automatic reconnection after connection errors.
- Uses a deque structure to maintain a limited history of recent signals and reduce repeated notifications.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| asyncio | Asynchronous concurrent execution |
| websockets | Real-time WebSocket communication |
| JSON | Market data parsing |
| collections.deque | Recent signal management |
| Binance Futures API | Public market data source |

## 📡 Market Data Sources

The application consumes two public Binance Futures WebSocket streams:

**Trades Stream**

```text
wss://fstream.binance.com/ws/btcusdt@trade
```

Provides individual trade information, including price, quantity and buyer-maker status.

**Order Book Stream**

```text
wss://fstream.binance.com/ws/btcusdt@depth5@100ms
```

Provides the five best bid and ask levels with updates approximately every 100 milliseconds.

No API key is required for these public market data streams.

## ⚙️ Configuration

The main parameters can be adjusted directly in the Python script.

| Parameter | Default | Description |
|---|---:|---|
| PAIR | btcusdt | Trading pair |
| THRESHOLD_WHALE | 100,000 | Minimum trade value in USD |
| ORDERBOOK_LEVELS | 5 | Order book levels analyzed |
| WHALE_WINDOW_SEC | 3 | Intended whale accumulation window |
| OBI_EWMA_ALPHA | 0.25 | Intended EWMA smoothing factor |
| OBI_BUY_THRESHOLD | 0.15 | Intended buying imbalance threshold |
| OBI_SELL_THRESHOLD | -0.15 | Intended selling imbalance threshold |
| COOLDOWN_SEC | 8 | Intended signal cooldown |

**Note:** The whale accumulation window, EWMA parameters, imbalance thresholds and cooldown are configuration placeholders for the next development iteration. They are not yet implemented in the current detection logic.

## 💻 Installation

### Prerequisites
- Python 3.10 or later.
- Internet connection.
- Git (optional, for cloning the repository).

### 1. Clone the repository

```bash
git clone https://github.com/aaguerrero/btc-market-flow-analyzer.git
cd btc-market-flow-analyzer
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

Linux / Ubuntu:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python bot.py
```

## 📊 Execution

Once started, the application establishes two concurrent WebSocket connections and begins monitoring market activity.

Example terminal output:

```text
🟢 Whale BUY detected: $125,000 @ 102500.50

🔴 Whale SELL detected: $145,000 @ 102480.20

🟢 BUY detected: Strong buying pressure

🔴 SELL detected: Strong selling pressure
```

The application continues running until manually interrupted.

To stop:

```text
CTRL + C
```

## 🏗️ Current Architecture

```text
Binance Futures WebSocket
          |
          +----------------------+
          |                      |
     Trades Stream          Depth5 Stream
          |                      |
   Whale Detection       Order Book Analysis
          |                      |
          +----------+-----------+
                     |
              Signal Detection
                     |
                  Terminal
```

## 🗺️ Development Roadmap

### Phase 1 — Core Market Monitoring
- [x] Binance Futures WebSocket integration.
- [x] Concurrent trade and order book listeners.
- [x] Individual whale trade detection.
- [x] Five-level order book volume aggregation.
- [x] Basic buy/sell pressure detection.
- [x] Automatic reconnection.

### Phase 2 — Quantitative Signal Processing
- [ ] Implement normalized Order Book Imbalance (OBI).
- [ ] Apply EWMA smoothing to OBI.
- [ ] Implement whale trade accumulation within a rolling time window.
- [ ] Implement signal cooldown.
- [ ] Improve duplicate signal management.

### Phase 3 — Market Analytics
- [ ] Correlate whale activity with order book imbalance.
- [ ] Add timestamped signal logging.
- [ ] Store market signals for historical analysis.
- [ ] Evaluate signal reliability against subsequent price movements.

### Phase 4 — Visualization
- [ ] Develop a real-time market monitoring dashboard.
- [ ] Display bid/ask volume distribution.
- [ ] Visualize OBI and whale activity.
- [ ] Build historical signal analytics.

## ⚠️ Disclaimer

This project is an experimental market monitoring and educational tool.

It analyzes publicly available market data and generates indicative market activity signals. It does not execute trades, provide investment advice, or guarantee market direction.

Whale transactions and order book imbalances should not be interpreted as standalone trading signals.

---

**Project Status:** MVP — Initial Development

**Focus:** Python · Real-Time Data Processing · Cryptocurrency Markets · Market Microstructure
