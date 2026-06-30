# Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total_investment = 0

print("===================================")
print("     STOCK PORTFOLIO TRACKER")
print("===================================")

while True:
    print("\nAvailable Stocks:")
    for stock in stock_prices:
        print(stock)

    stock_name = input("\nEnter Stock Name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available!")
        continue

    try:
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    value = stock_prices[stock_name] * quantity
    total_investment += value

    print(f"Investment in {stock_name}: Rs. {value}")

print("\n==============================")
print("Total Investment = Rs.", total_investment)
print("==============================")

# Save result to a text file
with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("=======================\n")
    file.write("Total Investment = Rs. " + str(total_investment))

print("\nResult saved successfully in portfolio.txt")