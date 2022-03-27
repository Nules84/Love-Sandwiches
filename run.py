""" Love Sandwiches """
import gspread
from google.oauth2.service_account import Credentials

@@ -14,18 +15,23 @@


def get_sales_data():

    """
    Get Sales figures input from the user
    """
    print("Please enter sales data from the last market")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10, 20, 30, 40, 50, 60\n")
    while True:
        print("Please enter sales data from the last market")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10, 20, 30, 40, 50, 60\n")

        data_str = input("Enter your data here: ")

    data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")

    sales_data = data_str.split(",")
    validate_data(sales_data)
        if validate_data(sales_data):
            print("Data is valid")
            break

    return sales_data


def validate_data(values):
@@ -42,6 +48,9 @@ def validate_data(values):
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


get_sales_data()
data = get_sales_data()
