# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# JDSmith,3.10.20,Renamed and started file modifications
# JDSmith,3.10.20,Lifted code from Assignment06, started refactoring
# ------------------------------------------------------------------------ #
# TODO: Look at previous assignments for the base functionality, focus on new concepts
# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to the Product class
# Data -------------------------------------------------------------------- #
# Declare variables and constants
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Product,Price}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strProduct = ""  # Captures the user product data
strPrice = ""  # Captures the user price data
strStatus = ""  # Captures the status of an processing functions
# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows:
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            product, price = line.split(",")
            row = {"Product": product.strip(), "Price": price.strip()}
            list_of_rows.append(row)
        file.close()

    @staticmethod  # 5
    def add_data_to_list(product, price, list_of_rows):
        """
        Appends rows to the list of dictionary rows
        :param product: value for key Product:
        :param price: value for key Price:
        :param list_of_rows: list where data should go:
        :return: rows in list, success message:
        """
        # TODO: Add Code Here!
        list_of_rows.append({'Product': product, 'Price': price})
        return list_of_rows, 'Success'

    # TODO: Add Code to process data to a file
    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """
        Writes data in memory into a file
        :param file_name: the file name as a string:
        :param list_of_rows: list of dictionary rows:
        :return: current contents:
        """
        file = open(file_name, 'w')
        for row in lstTable:
            file.write(str(row['Product'] + ',' + str(row['Price'] + '\n')))
        file.close()
        return list_of_rows, 'Success'

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    pass
    # TODO: Add code to show menu to user
    @staticmethod  # 2 this shows the menu
    def print_menu_products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Add new product and list price
            2) Review current product list
            3) Save list to file    
            4) Exit 
            ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod # 3 this lets you choose a menu item
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("What would you like to do? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice
    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod  # 6
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')
    # TODO: Add code to show the current data from the file to user
    @staticmethod  # 1 this is the stuff in the dictionary rows that are loaded in memory
    def print_current_products_in_list(list_of_rows):
        """ Shows the current Products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Products ToDo are: *******")
        for row in list_of_rows:
            print(row["Product"] + " (" + row["Price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod  # 4
    def input_new_product_and_price():
        """
        Gets new Product and Price from user
        :return: product and price strings from user input
        """
        product = input('Product: ')
        price = input('Price: ')
        return product, price
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName, lstTable)  # read file data

# Show user a menu of options
while (True):
    # Step 3 Show current data
    IO.print_menu_products()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new item
        strProduct, strPrice = IO.input_new_product_and_price()
        FileProcessor.add_data_to_list(strProduct, strPrice, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Review list
        IO.print_current_products_in_list(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.write_data_to_file('products.txt', lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit
