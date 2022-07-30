import re

class Console:

    def __init__(self):
        self.category = ""
        self.action = ""
        self.category_name = ""
        self.password = ""
        self.asked_password = ""
        self.current_position = ""
        self.db_action = ""
        self.chars = {}
        self.id = 0
        self.number = 0

    def read_user_action(self):
        """Reads user's action right after program starts""" 
        self.current_position = "start"
        print("-"*50)       
        print(("Enter B to check your balance.\n"
        "Enter C to choose category.\n"
        "Enter A to sign in as Admin.\n"))
        self.action = input("Please, choose the option: ").strip().lower()
        self.__is_valid_user_action(self.action)
    
    def __is_valid_user_action(self, user_action):
        """User action validation"""        
        if user_action != "b" and user_action != "c" and user_action != "a":
            print("-"*50)
            print("Input is invalid, try again.")
            self.read_user_action()

    def get_category(self, db):
        """Reads users entered category and saves it to the variable"""
        if self.current_position == "db_action":
            self.current_position = "db_category_choosing"
        else:
            self.current_position = "category_choosing"
        print("-"*50)
        print(("Categories: \nEnter CPU for CPUs/Processors; \n"
        "Enter RAM for Memory (RAM); \n"
        "Enter POWER for Power Supplies; \n"
        "Enter MOTHERBOARD for Motherboards; \n"
        "Enter VIDEO for Graphics/Video Cards; \n"
        "Enter FAN for Fans, Heat Sinks & Cooling. \n"
        "Enter R to return."))
        print("-"*50)
        self.category_name = input("Please, choose the option: ").strip().lower()
        if self.category_name == "r":
            self.return_back(self.current_position)
        else:
            self.__is_valid_category(self.category_name)
            self.category = getattr(db, self.category_name)

    def __is_valid_category(self, category_name):
        """Category input validation"""        
        if (category_name != "ram" and category_name != "cpu" and category_name != "power"
        and category_name != "motherboard" and category_name != "video" and category_name != "fan"):
            print("-"*50)
            self.category_name = input("Input is invalid, try again: ")
            if self.category_name == "r":
                self.return_back(self.current_position)
            else:
                self.__is_valid_category(self.category_name)

    def show_balance(self, balance):
        """Outputs users balance"""        
        self.current_position = "balance"
        print("-"*50)
        print(f"Your balance: {balance}$")
        self.return_back(self.current_position)

    def password_creation(self, db):
        """Creates password for admin panel"""        
        self.current_position = "password_creation"
        print("-"*50)
        self.password = input(("You are entering as admin for the first time. \n"
        "Please, create the password (at least 8 characters) or enter R to return: "))
        if self.password == "r":
            self.return_back(self.current_position)
        else:
            self.__is_valid_password(self.password, db)

    def __is_valid_password(self, password, db):
        """Validation of entered password"""        
        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
            db.password = password
            print("-"*50)
            print("Password saved!")
        else:
            print("-"*50)
            password = input("Password is invalid, try again: ")
            if password == "r":
                self.return_back(self.current_position)
            else:
                self.__is_valid_password(password, db)

    def __is_password_correct(self, asked_password, password):
        """Checking the correctness of the password"""        
        if asked_password == password:
            print("-"*50)
            print("Password confirmed!")
        elif asked_password.lower() == "r":
            self.read_user_action()
        else:
            print("-"*50)
            asked_password = input("Wrong password, try again: \n")
            self.__is_password_correct(asked_password, password)

    def ask_for_password(self, password):
        """Asking for password to log in admin panel """        
        self.current_position = "password_check"
        print("-"*50)
        self.asked_password = input("Please, enter the password or enter R to return.\n")
        if self.asked_password == "r":
            self.return_back(self.current_position)
        else:
            self.__is_password_correct(self.asked_password, password)

    def read_db_action(self):
        """Asks for db action"""        
        self.current_position = "db_action"
        print("-"*50)
        self.db_action = input(("Enter ADD to add new products;\n"
        "Enter DELETE to delete products;\n"
        "Enter UPDATE to change product properties.\n"
        "Enter EARN to change your balance\n"
        "Enter R to leave admin panel.\n")).strip().lower()
        if self.db_action == "r":
            self.return_back(self.current_position)
        else:
            self.__is_valid_db_action(self.db_action)
    
    def __is_valid_db_action(self, db_action):
        """Validation of db action"""        
        if db_action != "add" and db_action != "delete" and db_action != "update" and db_action != "earn":
            self.db_action = input("Input is invalid, try again: ")
            if self.db_action == "r":
                self.return_back(self.current_position)
            else:
                self.__is_valid_db_action(self.db_action)

    def __read_product_name(self):
        """Getting name of product"""    
        print("-"*50)   
        self.chars["Name"] = input("Enter a name of the product: ")
    
    def __read_product_number(self):
        """Getting number of products"""        
        try:
            print("-"*50)
            self.chars["Number"] = int(input("Enter a number of the product: "))
        except ValueError:
            print("-"*50)
            print("Invalid input, try again. ")
            self.__read_product_number()
        
    def __read_product_price(self):
        """Getting price of product"""        
        try:
            print("-"*50)
            self.chars["Price"] = float(input("Enter a price of the product (Example: 329.99): "))
        except ValueError:
            print("-"*50)
            print("Invalid input, try again.")
            self.__read_product_price()

    def read_product_chars(self):
        """Returning created product"""
        self.chars.clear()
        self.__read_product_name()
        self.__read_product_number()
        self.__read_product_price()

    def get_product_id(self, category):
        """Getting product id for buying, deleting or updating"""
        print("-"*50)        
        self.id = input("Enter id of the product or R to return: ").strip().lower()
        try:
            if self.id == "r":
                self.return_back(self.current_position)
            elif self.id.isdigit():
                self.id = int(self.id)
            if self.id >= len(category):
                print("-"*50)
                print("We don't have product with such id, try again.")
                self.get_product_id(category)
        except TypeError:
                print("-"*50)
                print("Invalid input, try again.")
                self.get_product_id(category)

    def show_products_list(self, category):
        """Printing list of products of certain category"""
        print("-"*50)    
        for product in category:
            print("ID: ", product["ID"])
            print("Name: ", product["Name"])
            print("Number: ", product["Number"])
            print("Price: ", product["Price"])
            print("-"*50)

    def get_number_of_product(self, category):
        """Getting number of products to buy""" 
        try:
            print("-"*50)
            self.number = int(input("Enter number of the products: "))
            if self.number > category[self.id]["Number"]:
                print("-"*50)
                print("We don't have enough number, try again.")
                self.get_number_of_product(category)
            elif self.number == 0:
                print("-"*50)
                print("You can't buy 0 products, try again.")
                self.get_number_of_product(category)
        except ValueError:
            print("-"*50)
            print("Invalid input, try again.")
            self.get_number_of_product(category)

    def buy_product(self, category, id, number, db):
        """Withdraws a certain amount of money from the balance, changes the number of products"""        
        if category[id]["Number"] - number < 0:
            print("-"*50)
            print("We don't have this number of products.")
            self.show_products_list(self.category)
            self.get_product_id(category)
        elif db.balance - category[id]["Price"]*number < 0:
            print("-"*50)
            print("You don't have enough money to buy this product.")
            self.show_products_list(self.category)
            self.get_product_id(category)
        else:
            db.balance -= category[id]["Price"]*number
            category[id]["Number"] -= number
            if category[id]["Number"] == 0:
                db.DELETE(category, id, position = self.current_position)
            print("-"*50)
            print("You've successfully purchased the product!")

    def return_back(self, position):
        """Takes the user back"""        
        match position:
            case ("category_choosing" | "balance" | "password_check" 
             | "password_creation" | "db_action" | "product_buying"):
                self.read_user_action()
            case "db_category_choosing":
                self.read_db_action()

    def is_empty_category(self, category, db):
        if len(category) == 0:
            print("-"*50)
            print("This category is empty!")
            self.get_category(db)