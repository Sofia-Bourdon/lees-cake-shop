import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime


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
sales_worksheet = SHEET.worksheet("sales")
wastage_worksheet = SHEET.worksheet("wastage")
stock_worksheet = SHEET.worksheet("stock")
favorites_worksheet = SHEET.worksheet("favorites")
rate_worksheet = SHEET.worksheet("rate")


def update_sales_worksheet(new_data):
    """
    Add values given by the user to sales worksheet.
    """
    print("Updating sales worksheet...")
    today_date = datetime.today().strftime('%Y-%m-%d')
    sales_worksheet.append_row([today_date] + new_data)
    print("Sales worksheet updated successfully.")


def update_wastage_worksheet(sales_data):
    """
    Calculate the total waste by subtracting the sales number from the stock.
    """
    stocks = stock_worksheet.get_all_values()[1]
    wastage = []
    for i in range(len(stocks)):
        wastage.append(int(stocks[i]) - int(sales_data[i]))
    
    print("Updating Wastage worksheet...")
    today_date = datetime.today().strftime('%Y-%m-%d')
    wastage_worksheet.append_row([today_date] + wastage)
    print("Wastage worksheet updated successfully.")


def calculate_rate_worksheet():
    """
    Uses the sp and cp values to calculate net revenue and profit based on sales numbers.
    """
    no_of_cakes_sold = []
    no_of_cakes_wasted = []
    sp_values = rate_worksheet.col_values(2)
    cp_values = rate_worksheet.col_values(3)
    sp_data = []
    cp_data = []
    net_revenue = []
    profit_perc_data = []
    profit = []
    
    for i in range(1, len(sp_values)):
        sp_data = sp_values[1:]

    for i in range(1, len(cp_values)):
        cp_data = cp_values[1:]

    for i in range(len(sp_data)):
        profit_perc_values = []
        profit_perc_values.append(100 * (int(sp_data[i]) - int(cp_data[i])) / int(cp_data[i]))
        for i in range(len(profit_perc_values)):
            profit_perc_data.append(int(profit_perc_values[i]))

    print("Updating profit percentage...")

    for index, data in enumerate(profit_perc_data):
        rate_worksheet.update_cell(index+2, 4, data)

    print("Profit percentage updated successfully.")


def add_sales_data():
    """
    Checks the values given by the user and adds to the spreadsheet 'sales'
    """
    print("Please enter your weekly sales data.")
    print("Only 10 values from 1 to 20 are accepted and the data must be separated by commas.")
    print("Example: 2,4,6,8,10,12,14,16,18,20.")

    while True:
        try:
            data_input = input("Insert data: ").split(",")
            values = [int(i) for i in data_input]
            if len(values) == 10:
                print("Data is valid!")
                print(values)
                update_sales_worksheet(values)
                update_wastage_worksheet(values)
                update_rate_worksheet(values)
                break
            else:
                print(f"10 numbers needed to complete this operation. You provided {len(values)}. Please try again. \n")
                print(data_input)
        except:
            print("Not a number. Please enter a valid number.")



def main():
    print("Hello, welcome to lee's cakes data management program.")
    choice = input("To add new sales to your worksheet enter 'sales'. To exit program enter 'exit'.\n")
    if choice == "sales":
        add_sales_data()
    elif choice == "exit":
        print("Exiting program...")
        exit()

calculate_rate_worksheet()
# main()
