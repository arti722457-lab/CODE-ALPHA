
import csv
import os
from datetime import date

FILE_NAME = "portfolio.csv"

# Create CSV file
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "ID", "Stock Name", "Quantity",
                "Buy Price", "Current Price", "Purchase Date"
            ])


# Add stock
def add_stock():
    print("\n===== ADD STOCK =====")

    name = input("Enter stock name or symbol: ").strip().upper()

    try:
        quantity = int(input("Enter quantity: "))
        buy_price = float(input("Enter buying price per share: "))
        current_price = float(input("Enter current price per share: "))

        if not name or quantity <= 0 or buy_price <= 0 or current_price < 0:
            print("Please enter valid stock details!")
            return

        with open(FILE_NAME, "r", newline="") as file:
            rows = list(csv.reader(file))
            stock_id = len(rows)

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                stock_id,
                name,
                quantity,
                buy_price,
                current_price,
                date.today()
            ])

        print("\nStock added successfully!")

    except ValueError:
        print("Please enter valid numeric values!")


# View all stocks
def view_stocks():
    print("\n===== YOUR STOCK PORTFOLIO =====")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        found = False

        for stock in reader:
            found = True

            investment = (
                int(stock["Quantity"]) *
                float(stock["Buy Price"])
            )

            current_value = (
                int(stock["Quantity"]) *
                float(stock["Current Price"])
            )

            profit_loss = current_value - investment

            print("\nStock:", stock["Stock Name"])
            print("Quantity:", stock["Quantity"])
            print("Buy Price: Rs.", stock["Buy Price"])
            print("Current Price: Rs.", stock["Current Price"])
            print("Investment: Rs.", round(investment, 2))
            print("Current Value: Rs.", round(current_value, 2))
            print("Profit/Loss: Rs.", round(profit_loss, 2))
            print("Purchase Date:", stock["Purchase Date"])

        if not found:
            print("No stocks found!")


# Update current stock price
def update_price():
    name = input("\nEnter stock symbol to update: ").strip().upper()

    try:
        new_price = float(input("Enter new current price: "))

        if new_price < 0:
            print("Price cannot be negative!")
            return

        with open(FILE_NAME, "r", newline="") as file:
            rows = list(csv.DictReader(file))

        found = False

        for stock in rows:
            if stock["Stock Name"].upper() == name:
                stock["Current Price"] = new_price
                found = True

        if not found:
            print("Stock not found!")
            return

        with open(FILE_NAME, "w", newline="") as file:
            fields = [
                "ID", "Stock Name", "Quantity",
                "Buy Price", "Current Price", "Purchase Date"
            ]

            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

        print("Stock price updated successfully!")

    except ValueError:
        print("Please enter a valid price!")


# Portfolio summary
def portfolio_summary():
    total_investment = 0
    current_value = 0
    total_stocks = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for stock in reader:
            quantity = int(stock["Quantity"])
            buy_price = float(stock["Buy Price"])
            market_price = float(stock["Current Price"])

            total_investment += quantity * buy_price
            current_value += quantity * market_price
            total_stocks += quantity

    profit_loss = current_value - total_investment

    print("\n===== PORTFOLIO SUMMARY =====")
    print("Total Shares:", total_stocks)
    print("Total Investment: Rs.", round(total_investment, 2))
    print("Current Portfolio Value: Rs.", round(current_value, 2))
    print("Total Profit/Loss: Rs.", round(profit_loss, 2))

    if profit_loss > 0:
        print("Status: PROFIT")
    elif profit_loss < 0:
        print("Status: LOSS")
    else:
        print("Status: NO PROFIT NO LOSS")


# Delete stock record
def delete_stock():
    stock_id = input("\nEnter stock ID to delete: ")

    with open(FILE_NAME, "r", newline="") as file:
        rows = list(csv.DictReader(file))

    new_rows = [
        stock for stock in rows
        if stock["ID"] != stock_id
    ]

    if len(new_rows) == len(rows):
        print("Stock ID not found!")
        return

    fields = [
        "ID", "Stock Name", "Quantity",
        "Buy Price", "Current Price", "Purchase Date"
    ]

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(new_rows)

    print("Stock deleted successfully!")


# Main program
create_file()

while True:

    print("\n================================")
    print("       STOCK PORTFOLIO TRACKER")
    print("================================")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Update Stock Price")
    print("4. Portfolio Summary")
    print("5. Delete Stock")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_stock()

    elif choice == "2":
        view_stocks()

    elif choice == "3":
        update_price()

    elif choice == "4":
        portfolio_summary()

    elif choice == "5":
        delete_stock()

    elif choice == "6":
        print("Thank you for using Stock Portfolio Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")
