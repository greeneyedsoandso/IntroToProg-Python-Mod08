# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# JDSmith,3.14.2020,Threw out a week of work and started over
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strStatus = ""


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JDSmith,3.14.2020,Threw out a week of work and started over
    """
    # -- Properties --
    @property  # DON'T USE NAME for this directive!
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name)

    @product_name.setter  # The NAME MUST MATCH the property!
    def product_name(self, value):  # (setter or mutator)
        if not str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Product names cannot be numbers")

    @property  # DON'T USE NAME for this directive!
    def product_price(self):  # (getter or accessor)
        return str(self.__product_price)

    @product_price.setter  # The NAME MUST MATCH the property!
    def product_price(self, value):  # (setter or mutator)
        if str(value).isnumeric():
            self.__product_price = value
        else:
            raise Exception("Please enter a price in dollars")

    # methods
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.product_name = product_name
        self.product_price = product_price

    def __str__(self):
        return self.product_name + ',' + self.product_price

    def pretty(self):
        return self.product_name + ', $' + self.product_price

# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JDSmith,3.14.2020,Threw out a week of work and started over
    """
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of rows
        :param file_name: (string) with name of file:
        :return: (list) of rows:
        """
        list_rows = []
        file = open(file_name, 'r')
        for line in file:
            i = line.strip().split(',')
            list_rows.append(Product(i[0], i[1]))
            return list_rows
        file.close()

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """
        Writes data in memory into a file
        :param file_name: the file name as a string:
        :param list_of_product_objects: objects:
        :return: current contents:
        """
        file = open(file_name, 'w')
        for row in list_of_product_objects:
            file.write(str(f'{row}\n'))
        file.close()
        return list_of_product_objects, 'Success'
# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Processes data to and from a file and a list of product objects:

    methods:
        print_menu_products():
        input_menu_choice(): -> (string)
        input_yes_no_choice(message):
        input_press_to_continue(optional_message=''):
        print_current_products_in_list(list_of_rows):
        input_new_product_and_price():
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JDSmith,3.14.2020,Threw out a week of work and started over
    """
    @staticmethod  # this shows the menu
    def print_menu_products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Review current product list
            2) Add new product and list price
            3) Save list to file    
            4) Exit 
            ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod  # this lets you choose a menu item
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

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)

    # TODO: Add code to show the current data from the file to user
    @staticmethod  # this is the stuff loaded in memory
    def print_current_products_in_list(list_of_rows):
        """ Shows the current Products in the list of rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Products and Prices are: *******")
        for row in list_of_rows:
            row = Product.pretty(row)
            print(row)
        print("****************************************************")

    @staticmethod
    def input_new_product_and_price(list_data):
        """
        Gets new Product and Price from user
        :return: product and price strings from user input
        """
        product = input('Product: ')
        price = input('Price: $')
        obj_list = Product(product, price)
        list_data.append(obj_list)
        return list_data

# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while True:
    IO.print_menu_products()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    if strChoice.strip() == '1':  # Show current list
        # IO.print_current_products_in_list(lstOfProductObjects)
        IO.print_current_products_in_list(lstOfProductObjects) # Show current data in the list/table
        continue  # to show the menu
    elif strChoice.strip() == '2':  # Add a new item
        try:
            prod_price = IO.input_new_product_and_price(lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
        except Exception as e:
            print(str(e))
        continue  # to show the menu
    elif strChoice.strip() == '3':
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu
    elif strChoice.strip() == '4':
        break
