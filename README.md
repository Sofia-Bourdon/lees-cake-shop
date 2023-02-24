# Welcome to Lee's Cake Shop,

Lee's Cake Shop is a command line based program created to handle data automation which runs on a mock terminal on Heroku.

This program was designed to help a business minimize product wastage, keep track of sales and profit rates as well as the total combined profit. It generates the data based on the user input and updates into a Google sheets worksheet.

## How to use

* The user runs the program on the app and type 'sales' to enter new sales numbers.
* The sales numbers must be a collection of 10 numbers separated by commas. The computer will verify if it was entered correctly and request the user to enter the sales numbers again if needed.
* The program will then generate a new wastage number based on the previous stock and each rate calculation which will be displayed on the screen. Every 2 sales registered the computer will then calculate a new stock number to minimize the wastage.

## Features 

### User greeting and interactive command prompt 
<img width="750" alt="Screenshot 2023-02-24 at 11 57 02" src="https://user-images.githubusercontent.com/112895499/221162247-3a3cb5a1-dd2d-4007-b034-993f4873cd8e.png">
* Greets the user with a simple message.
* Requests the user to enter one of two options to continue running the program.
* When 'sales' is entered the program will run and the next feature will be displayed.
* When 'exit' is entered a message informing the user that the program is being exited is displayed on the screen and the program exits.

### Requesting data input and validation
<img width="750" alt="Screenshot 2023-02-24 at 12 08 10" src="https://user-images.githubusercontent.com/112895499/221164552-4760d368-561e-4f3b-9999-df317fcf0826.png">
* The computer requests the user to enter the sales data and instructions are given.
* The data given is then checked by the program.
* If the data entered by the user did not follow the instructions an error message will appear and they will be requested to reenter the data.
<img width="747" alt="Screenshot 2023-02-24 at 12 13 08" src="https://user-images.githubusercontent.com/112895499/221165533-b129f034-21de-4d67-93be-4b759a501829.png">
* The program will also check for the correct values given. Only numbers will be accepted.
<img width="749" alt="Screenshot 2023-02-24 at 12 15 42" src="https://user-images.githubusercontent.com/112895499/221166029-403d1757-1bdf-4e78-bf49-d467db57b722.png">
* When the correct data is inserted the computer will inform the user that the data is valid and utilize the given numbers to calculate wastage, stock numbers and others. 
<img width="750" alt="Screenshot 2023-02-24 at 12 16 54" src="https://user-images.githubusercontent.com/112895499/221166510-a79c124c-49cf-4f04-a457-b82aad0241b8.png">

### Automatic data handling 
<img width="749" alt="Screenshot 2023-02-24 at 12 20 37" src="https://user-images.githubusercontent.com/112895499/221166903-082b8a06-627a-47d2-aebd-0d886374f9d0.png">
* The new sales data is then added into the 'sales' worksheet along with the date.
<img width="1484" alt="Screenshot 2023-02-24 at 12 23 26" src="https://user-images.githubusercontent.com/112895499/221167512-1dcdb1f1-e724-4760-8d5f-02f51c124231.png">
* New wastage numbers are calculated based on the number of sales and the previous stock number and added to the 'wastage' sheet.
<img width="1484" alt="Screenshot 2023-02-24 at 12 26 34" src="https://user-images.githubusercontent.com/112895499/221168032-e1ef7ada-5d17-4928-ace8-21b8ad126622.png">
* The profit percentage for each cake is calculated based on the existing selling price and cost price. If the numbers are updated by the user the result will differ.
* The net revenue is then calculated based on the total number of sales that each product had as well as the sp and cp. The result is updated into the 'rate' worksheet column.
* The profit of each cake is then calculated also taking the wastage numbers into consideration and added to the 'profit' column indide the 'rate' sheet. As new sales are entered the profit numbers will increase or decrease. 
* A sum of all the profit numbers are displayed on the side as the total profit inside the 'rate' sheet.
<img width="1484" alt="Screenshot 2023-02-24 at 12 33 55" src="https://user-images.githubusercontent.com/112895499/221169370-9bb636d2-15f4-4e2e-a2a1-567cac5872b8.png">
* A new stock number based on the last couple of sales will then be calculated to prevent further wastage. The numbers will be displayed as a new row on the 'stock' sheet.
<img width="1485" alt="Screenshot 2023-02-24 at 12 37 04" src="https://user-images.githubusercontent.com/112895499/221169952-757b32dd-0cf1-4328-961d-00e67d65bd4f.png">

### Future features

* A monthly favorites feauture where the program tracks the most sold cakes of each month.
* A reset function which allows the user to delete the existing data using the app.


## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
