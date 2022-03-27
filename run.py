""" Love Sandwiches """
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
@@ -65,13 +66,29 @@ def update_sales_worksheet(data):
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type. 
    the surplus is definied as the sales figure subtracted from the stock:
    -Postitive surplus indicates waste
    - Negative surplus indicated extra made when stock was sold out. 
    """

    print("Calculating suplus data...|n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(stock_row)


def main():
    """
    run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)

    main()
     
print("welcome to Love Sandwiches Data Automation")
main()