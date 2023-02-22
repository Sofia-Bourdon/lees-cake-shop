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


def update_rate_worksheet(data):

    print(f"Transfering {data} to worksheet...")

    for index, data in enumerate(profit_perc_data):
        rate_worksheet.update_cell(index+2, 4, data)

    for index, data in enumerate(net_revenue):
        rate_worksheet.update_cell(index+2, 5, data)

    for index, data in enumerate(total_profit):
        rate_worksheet.update_cell(index+2, 6, data)

    print("Rate worksheet updated successfully.")


def update_total_profit(data):



def calculate_individual_profit(worksheet):
    """
    Calculates the total profit based on the equation:
    Profit = (sp_data-cp_data)* no_of_cakes_sold - no_of_cakes_wasted * cp_data
    """
    global individual_profit 
    individual_profit = []
    global no_of_cakes_wasted
    no_of_cakes_wasted = []

    choco_cakes_wasted = sum([int(i) for i in wastage_worksheet.col_values(2)[1:]])
    vanilla_cakes_wasted = sum([int(i) for i in wastage_worksheet.col_values(3)[1:]])
    redvlvt_cakes_wasted = sum([int(i) for i in wastage_worksheet.col_values(4)[1:]])
    lemon_cakes_wasted = sum([int(i) for i in wastage_worksheet.col_values(5)[1:]])
    sponge_cakes_wasted = sum([int(i) for i in wastage_worksheet.col_values(6)[1:]])
    blackfor_cakes_wasted = sum([int(i) for i in wastage_worksheet.col_values(7)[1:]])
    icecream_cakes_wasted = sum([int(i) for i in wastage_worksheet.col_values(8)[1:]])
    funfetti_cakes_wasted = sum([int(i) for i in wastage_worksheet.col_values(9)[1:]])
    cookie_cakes_wasted = sum([int(i) for i in wastage_worksheet.col_values(10)[1:]])
    chiffon_cakes_wasted = sum([int(i) for i in wastage_worksheet.col_values(3)[1:]])

    no_of_cakes_wasted.extend(value for name, value in locals().items() if name.endswith('cakes_wasted'))

    print("Calculating Profit...")

    for i in range(len(no_of_cakes_sold)):
        ind_profit_values = []
        ind_profit_values.append(int(net_revenue[i]) - (int(no_of_cakes_wasted[i]) * int(cp_data[i])))
        for i in range(len(ind_profit_values)):
            individual_profit.append(ind_profit_values[i])

    print(f"Your no of cakes wasted is: {no_of_cakes_wasted}")
    print(f"Your Profit is: {individual_profit}")
    return individual_profit



def calculate_net_revenue(worksheet):
    """
    Calculates the net revenue by subctracting the sp by the cp and multiplying it by the no of cakes sold.
    """
    global net_revenue
    net_revenue = []
    global no_of_cakes_sold
    no_of_cakes_sold = []

    choco_cakes_sold = sum([int(i) for i in sales_worksheet.col_values(2)[1:]])
    vanilla_cakes_sold = sum([int(i) for i in sales_worksheet.col_values(3)[1:]])
    redvlvt_cakes_sold = sum([int(i) for i in sales_worksheet.col_values(4)[1:]])
    lemon_cakes_sold = sum([int(i) for i in sales_worksheet.col_values(5)[1:]])
    sponge_cakes_sold = sum([int(i) for i in sales_worksheet.col_values(6)[1:]])
    blackfor_cakes_sold = sum([int(i) for i in sales_worksheet.col_values(7)[1:]])
    icecream_cakes_sold = sum([int(i) for i in sales_worksheet.col_values(8)[1:]])
    funfetti_cakes_sold = sum([int(i) for i in sales_worksheet.col_values(9)[1:]])
    cookie_cakes_sold = sum([int(i) for i in sales_worksheet.col_values(10)[1:]])
    chiffon_cakes_sold = sum([int(i) for i in sales_worksheet.col_values(3)[1:]])

    no_of_cakes_sold.extend(value for name, value in locals().items() if name.endswith('cakes_sold'))

    print("Calculating net revenue...")
    
    for i in range(len(no_of_cakes_sold)):
        net_revenue_values = []
        net_revenue_values.append(no_of_cakes_sold[i] * (int(sp_data[i]) - int(cp_data[i])))
        for i in range(len(net_revenue_values)):
            net_revenue.append(int(net_revenue_values[i]))

    print(f"your total net revenue is: {net_revenue}")
    return net_revenue


def calculate_profit_perc(arg1, arg2):
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
                break
            else:
                print(f"10 numbers needed to complete this operation. You provided {len(values)}. Please try again. \n")
                print(data_input)
        except:
            print("Not a number. Please enter a valid number.")

        return values


def main():
    print("Hello, welcome to lee's cakes data management program.")
    choice = input("To add new sales to your worksheet enter 'sales'. To exit program enter 'exit'.\n")
    if choice == "sales":
        add_sales_data()
        calculate_profit_perc()
    elif choice == "exit":
        print("Exiting program...")
        exit()

# main()
calculate_profit_perc(sp_data, cp_data)
calculate_net_revenue(rate_worksheet)
calculate_individual_profit(rate_worksheet)
update_total_profit(individual_profit)
# update_rate_worksheet(profit_perc_data)
# update_rate_worksheet(net_revenue)
# update_rate_worksheet(individual_profit)
