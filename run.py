import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('lees_cake_shop')

sales = SHEET.worksheet('favorites')

data = sales.get_all_values()


def add_sales_data():
    """
    Updates the values given by the user to the spreadsheet 'sales'
    """
    print("Please enter your weekly sales data.")
    print("Only 10 values from 1 to 20 are accepted and the data must be separated by commas.")
    print("Example: 2,4,6,8,10,12,14,16,18,20.")

    data_input = input("Insert data: ").split(",")
    validate_number(data_input)



def validate_number(values):
    """
    Converts the data given by user into Integers.
    Checks for the right number of values (10) If not, Raises ValueError.
    """
    try:
        [int(value) for value in values]
        if len(values) != 10:
            raise ValueError()
    except ValueError:
        print(f"10 numbers needed to complete this operation. You provided {len(values)}. Please try again. \n")



add_sales_data()
