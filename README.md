# 📊 Smart Trade Analytics Engine

A modular Python-based trade analytics engine designed to simulate core workflows in quantitative trading systems.  
This project focuses on **data validation, trade processing, PnL computation, and portfolio-level insights**, with clean structure and test coverage.

---

## 🚀 Overview

In quantitative trading and research environments, reliable trade data processing is critical.  
This project demonstrates how raw trade inputs can be:

- cleaned and validated
- transformed into structured records
- analyzed for profitability and risk
- aggregated into portfolio-level metrics

The system is intentionally built in a **modular, extensible way**, mirroring patterns used in real trading infrastructure.

---

## ⚙️ Features

### ✅ Trade Processing Pipeline
- Symbol normalization (case + formatting)
- Input validation (price, quantity, missing values)
- Safe handling of invalid trades (skipped without crashing)

### 💰 Analytics Engine
- Profit & Loss (PnL) calculation
- Return percentage computation
- Trade classification:
  - `PROFIT`
  - `LOSS`
  - `BREAKEVEN`

### ⚠️ Risk Flagging
- Simple rule-based risk detection
- Identifies trades with negative return thresholds

### 📊 Portfolio Summary Metrics
- Total PnL
- Winning vs losing trades
- Best and worst trade identification

### 🧪 Testing
- Unit tests using `pytest`
- Covers core logic (PnL, classification, validation)

---

## 🧠 Example Output

```text
Cleaned Trade Log:
{'symbol': 'AAPL', 'pnl': 100.0, ...}
{'symbol': 'GOOG', 'pnl': -100.0, ...}

Total PnL: 40.0
Winning Trades: 2
Losing Trades: 1
Best Trade: AAPL
Worst Trade: GOOG
```

---

## 🏗️ Project Structure

```
smart-trade-analytics-engine/
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── README.md
├── requirements.txt
├── pytest.ini
└── .gitignore
```

---

## 🛠️ Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python src/main.py
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 💼 Skills Demonstrated

This project highlights key skills relevant to quantitative research and trading roles:

- Python for financial data processing
- Input validation and error handling
- Modular code design
- Trade-level analytics (PnL, returns)
- Basic risk classification
- Unit testing with pytest
- Git & GitHub project structuring

---

## 🔧 Future Enhancements

This project is designed to be extended into a more advanced quant system:

- 📁 CSV / real market data ingestion
- 📊 Portfolio class with position tracking
- 📈 Sharpe ratio and performance metrics
- 📉 Drawdown analysis
- 📊 PnL and equity curve visualization
- ⚡ Event-driven backtesting engine

---

## 📌 Why This Project Matters

This project reflects foundational components of real trading systems, including:

- Data integrity checks
- Trade lifecycle processing
- Performance measurement
- Modular architecture

It serves as a stepping stone toward building full-scale quantitative research and trading pipelines.

---

## 👤 Author

**Patience Fuglo**  
Quantitative Finance & Machine Learning Enthusiast