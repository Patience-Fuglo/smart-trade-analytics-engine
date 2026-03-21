from typing import List, Dict, Optional, Tuple


raw_trades = [
    ["Aapl", 150, 160, 10],
    ["goog", "2800", 2780, 5],
    ["msft", 300, None, 0],
    ["tsla", 250, 270, 2],
]


def clean_symbol(symbol) -> str:
    return str(symbol).strip().upper()


def validate_prices(buy_price: float, sell_price: float) -> None:
    if not isinstance(buy_price, (int, float)) or not isinstance(sell_price, (int, float)):
        raise TypeError("Buy and sell prices must be numbers.")
    if buy_price <= 0 or sell_price <= 0:
        raise ValueError("Buy and sell prices must be greater than zero.")


def validate_quantity(quantity: int) -> None:
    if not isinstance(quantity, int):
        raise TypeError("Quantity must be an integer.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")


def calculate_pnl(buy_price: float, sell_price: float, quantity: int) -> float:
    return (sell_price - buy_price) * quantity


def calculate_return_percentage(buy_price: float, sell_price: float) -> float:
    if buy_price == 0:
        raise ZeroDivisionError("Buy price cannot be zero.")
    return ((sell_price - buy_price) / buy_price) * 100


def classify_trade(pnl: float) -> str:
    if pnl > 0:
        return "PROFIT"
    if pnl < 0:
        return "LOSS"
    return "BREAKEVEN"


def risk_check(return_percentage: float) -> str:
    return "HIGH RISK" if return_percentage < -5 else "NORMAL"


def process_single_trade(raw_trade: list) -> Optional[Dict]:
    try:
        symbol, buy_price, sell_price, quantity = raw_trade

        symbol = clean_symbol(symbol)
        buy_price = float(buy_price)
        sell_price = float(sell_price)
        quantity = int(quantity)

        validate_prices(buy_price, sell_price)
        validate_quantity(quantity)

        pnl = calculate_pnl(buy_price, sell_price, quantity)
        return_pct = calculate_return_percentage(buy_price, sell_price)
        result = classify_trade(pnl)
        risk = risk_check(return_pct)

        return {
            "symbol": symbol,
            "buy_price": buy_price,
            "sell_price": sell_price,
            "quantity": quantity,
            "pnl": pnl,
            "return_pct": round(return_pct, 2),
            "result": result,
            "risk": risk,
        }

    except (ValueError, TypeError, ZeroDivisionError):
        print(f"Invalid trade skipped: {raw_trade}")
        return None
    finally:
        print("Trade processed")


def process_all_trades(raw_trades: List[list]) -> List[Dict]:
    trade_log = []
    for trade in raw_trades:
        processed = process_single_trade(trade)
        if processed is not None:
            trade_log.append(processed)
    return trade_log


def calculate_total_pnl(trade_log: List[Dict]) -> float:
    return sum(trade["pnl"] for trade in trade_log)


def trade_count_summary(trade_log: List[Dict]) -> Tuple[int, int]:
    winning_trades = sum(1 for trade in trade_log if trade["result"] == "PROFIT")
    losing_trades = sum(1 for trade in trade_log if trade["result"] == "LOSS")
    return winning_trades, losing_trades


def best_and_worst_trades(trade_log: List[Dict]) -> Tuple[Optional[Dict], Optional[Dict]]:
    if not trade_log:
        return None, None
    best_trade = max(trade_log, key=lambda trade: trade["pnl"])
    worst_trade = min(trade_log, key=lambda trade: trade["pnl"])
    return best_trade, worst_trade


def main() -> None:
    trade_log = process_all_trades(raw_trades)

    print("\nCleaned Trade Log:")
    for trade in trade_log:
        print(trade)

    total_pnl = calculate_total_pnl(trade_log)
    winning_trades, losing_trades = trade_count_summary(trade_log)
    best_trade, worst_trade = best_and_worst_trades(trade_log)

    print(f"\nTotal PnL: {total_pnl}")
    print(f"Winning Trades: {winning_trades}")
    print(f"Losing Trades: {losing_trades}")

    if best_trade:
        print(f"Best Trade: {best_trade['symbol']} | PnL: {best_trade['pnl']}")
    if worst_trade:
        print(f"Worst Trade: {worst_trade['symbol']} | PnL: {worst_trade['pnl']}")


if __name__ == "__main__":
    main()
