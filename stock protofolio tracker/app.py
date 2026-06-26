from flask import Flask, render_template, request

app = Flask(__name__)

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 170
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():

    portfolio_data = []
    total_investment = 0

    stock_symbols = request.form.getlist("stock")
    share_counts = request.form.getlist("quantity")

    for symbol, shares in zip(stock_symbols, share_counts):

        symbol = symbol.strip().upper()
        shares = shares.strip()

        if symbol and shares and symbol in stock_prices:

            shares = int(shares)

            current_price = stock_prices[symbol]

            investment_amount = current_price * shares

            total_investment += investment_amount

            portfolio_data.append({
                "stock": symbol,
                "quantity": shares,
                "price": current_price,
                "value": investment_amount
            })

    return render_template(
        "result.html",
        portfolio=portfolio_data,
        total=total_investment
    )


if __name__ == "__main__":
    app.run(debug=True)