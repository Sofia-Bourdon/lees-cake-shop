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

sp_data = []
cp_data = []
no_of_cakes_sold = []
no_of_cakes_wasted = []


def update_sales_worksheet(new_data):
    """
    Add values given by the user to sales worksheet.
    """
    print("Updating sales worksheet...")
    today_date = datetime.today().strftime('%Y-%m-%d')
    sales_worksheet.append_row([today_date] + new_data)
    print("Sales worksheet updated successfully.")


def update_stock_worksheet():
    """
    Calculates the new stock numbers and updates into stock sheet
    """
    global new_stock
    new_stock = []

    print("Calculating new stock...")

    for i in range(2, 12):
        last_two_sales = []
        last_two_sales.append(sum([int(i) for i in sales_worksheet.col_values(i)[-2:]]))
        for i in range(len(last_two_sales)):
            new_stock.append(round(int(last_two_sales[i]) / 2))
    print("Updating new values into the stock worksheet...")
    stock_worksheet.append_row(new_stock)

    print("Stock worksheet updated successfully")
    print(new_stock)


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


def update_rate_worksheet():

    # print(f"Transfering {data} to worksheet...")

    for index, data in enumerate(profit_perc_data):
        rate_worksheet.update_cell(index+2, 4, data)

    for index, data in enumerate(net_revenue):
        rate_worksheet.update_cell(index+2, 5, data)

    for index, data in enumerate(individual_profit):
        rate_worksheet.update_cell(index+2, 6, data)

    print("Rate worksheet updated successfully.")


def update_total_profit():
    """
    Calculates the total profit and updates into the spreadsheet
    """
    total_profit = sum(int(i) for i in individual_profit)
    print(f"Your total profit is: {total_profit}")
    rate_worksheet.update_cell(11, 8, total_profit)


def calculate_individual_profit():
    """
    Calculates the individual profit of each product.
    """
    global individual_profit
    individual_profit = []
    global no_of_cakes_wasted
    no_of_cakes_wasted = []

    for i in range(2, 12):
        no_of_cakes_wasted.append(sum([int(j) for j in wastage_worksheet.col_values(i)[1:]]))

    print("Calculating Profit...")

    for i in range(10):
        ind_profit_values = []
        ind_profit_values.append(int(net_revenue[i]) - (int(no_of_cakes_wasted[i]) * int(cp_data[i])))
        for i in range(len(ind_profit_values)):
            individual_profit.append(ind_profit_values[i])

    print(f"Your no of cakes wasted is: {no_of_cakes_wasted}")
    print(f"Your Profit is: {individual_profit}")
    return individual_profit


def calculate_net_revenue():
    """
    Calculates the net revenue of each product.
    """
    global net_revenue
    net_revenue = []
    global no_of_cakes_sold
    no_of_cakes_sold = []

    for i in range(2, 12):
        no_of_cakes_sold.append(sum([int(j) for j in sales_worksheet.col_values(i)[1:]]))

    print("Calculating net revenue...")

    for i in range(len(no_of_cakes_sold)):
        net_revenue.append(int(no_of_cakes_sold[i] * (int(sp_data[i]) - int(cp_data[i]))))

    print(f"your total net revenue is: {net_revenue}")
    # return net_revenue


def calculate_profit_perc():
    """
    Gets the sp and cp value and calculates the total profit percentage for each product.
    """
    sp_values = rate_worksheet.col_values(2)
    cp_values = rate_worksheet.col_values(3)

    global profit_perc_data
    profit_perc_data = []

    for i in range(1, len(sp_values)):
        global sp_data
        sp_data = sp_values[1:]

    for i in range(1, len(cp_values)):
        global cp_data
        cp_data = cp_values[1:]

    print("Calculating profit percentage...")

    for i in range(len(sp_data)):
        profit_perc_values = []
        profit_perc_values.append(100 * (int(sp_data[i]) - int(cp_data[i])) / int(cp_data[i]))
        for i in range(len(profit_perc_values)):
            profit_perc_data.append(int(profit_perc_values[i]))

    print(f"Your total profit percentage is {profit_perc_data}")

    return profit_perc_data


def add_sales_data():
    """
    Checks the values given by the user and adds to the spreadsheet 'sales'
    """
    print("Please enter your weekly sales data.")
    print("The data must be separated by commas.")
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
                update_stock_worksheet()
                break
            else:
                print("10 numbers needed to complete this operation.")
                print(f"You provided {len(values)}. Please try again. \n")
                print(data_input)
        except raise ValueError:
            print("Not a number. Please enter a valid number.")

        return values


def main():
    print("Hello, welcome to lee's cakes data management program.")
    choice = input("To add new sales to your worksheet enter 'sales'. To exit program enter 'exit'.\n")
    if choice == "sales":
        add_sales_data()
        calculate_profit_perc()
        calculate_net_revenue()
        calculate_individual_profit()
        update_total_profit()
        update_rate_worksheet()
    elif choice == "exit":
        print("Exiting program...")
        exit()


main()