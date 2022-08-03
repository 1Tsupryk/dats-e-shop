import re

class Console:

    def read_user_action(self):
        """Reads user's action right after program starts""" 
        print("-"*50)       
        print(("Enter B to check your balance.\n"
        "Enter C to choose category.\n"
        "Enter A to sign in as Admin.\n"
        "Enter Q to quit the shop."))
        print("-"*50)
        action = input("Please, choose the option: ").strip().lower()
        if self.__is_valid_user_action(action):
            return action
        else:
            self.read_user_action()
    
    def __is_valid_user_action(self, user_action):
        """User action validation"""        
        if (user_action != "b" and user_action != "c" and user_action != "a"
        and user_action != "q"):
            print("-"*50)
            print("Input is invalid, try again.")
            return False
        else:
            return True

    def get_category(self):
        """Reads users entered category and saves it to the variable"""
        print("-"*50)
        print(("Categories: \nEnter CPU for CPUs/Processors; \n"
        "Enter RAM for Memory (RAM); \n"
        "Enter POWER for Power Supplies; \n"
        "Enter MOTHERBOARD for Motherboards; \n"
        "Enter VIDEO for Graphics/Video Cards; \n"
        "Enter FAN for Fans, Heat Sinks & Cooling. \n"
        "Enter R to return."))
        print("-"*50)
        category_name = input("Please, choose the option: ").strip().lower()
        if category_name == "r":
            return "r"
        elif self.__is_valid_category(category_name):
            return category_name
        else:
            self.get_category()
        
    def __is_valid_category(self, category_name):
        """Category input validation"""        
        if (category_name != "ram" and category_name != "cpu" 
        and category_name != "power" and category_name != "motherboard"
        and category_name != "video" and category_name != "fan"):
            print("-"*50)
            print("Input is invalid, try again.")
            return False
        else:
            return True

    def show_balance(self, balance):
        """Outputs users balance"""        
        self.current_position = "balance"
        print("-"*50)
        print(f"Your balance: {balance}$")
        self.return_back(self.current_position)

    def create_password(self):
        """Creates password for admin panel"""        
        print("-"*50)
        password = input("Please, create the password (at least 8 characters) or enter R to return: ")
        if password.lower().strip() == "r":
            return "r"
        elif self.__is_valid_password(password):
            print("-"*50)
            print("Password saved!")
            return password
        else:
            self.create_password()


    def __is_valid_password(self, password):
        """Validation of entered password"""        
        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
            return True
        else:
            print("-"*50)
            print("Password is invalid, try again.")
            return False

    def login(self, password):
        """Asking for password to log in admin panel """        
        print("-"*50)
        login_password = input("Please, enter the password or enter R to return.\n")
        is_password_correct = self.__login_check(login_password, password)
        if is_password_correct:
            if is_password_correct == "r":
                return "r"
            else:
                return True
        else:
            self.login(password)

    def __login_check(self, login_password, password):
        """Checking the correctness of the password"""        
        if login_password == password:
            print("-"*50)
            print("Password confirmed!")
            return True
        elif login_password.lower() == "r":
            return "r"
        else:
            print("-"*50)
            print("Wrong password, try again.")
            return False

    def read_db_action(self):
        """Asks for db action"""        
        print("-"*50)
        db_action = input(("Enter ADD to add new products;\n"
        "Enter DELETE to delete products;\n"
        "Enter UPDATE to change product properties.\n"
        "Enter R to leave admin panel.\n"
        "Please choose the option: ")).strip().lower()
        if db_action == "r":
            return "r"
        elif self.__is_valid_db_action(db_action):
            return db_action
        else:
            self.read_db_action()
    
    def __is_valid_db_action(self, db_action):
        """Validation of db action"""        
        if db_action != "add" and db_action != "delete" and db_action != "update":
            print("Input is invalid, try again.")
            return False
        else:
            return True

    def __read_product_name(self):
        """Getting name of product"""    
        print("-"*50)   
        return {"Name" : input("Enter a name of the product: ")}
    
    def __read_product_number(self):
        """Getting number of products"""        
        try:
            print("-"*50)
            return {"Number" : int(input("Enter a number of the product: "))}
        except ValueError:
            print("-"*50)
            print("Invalid input, try again. ")
            self.__read_product_number()
        
    def __read_product_price(self):
        """Getting price of product"""        
        try:
            print("-"*50)
            return {"Price" : float(input("Enter a price of the product (Example: 329.99): "))}
        except ValueError:
            print("-"*50)
            print("Invalid input, try again.")
            self.__read_product_price()

    def get_product_chars(self):
        """Returning created product"""
        return {**self.__read_product_name(), **self.__read_product_number(),
        **self.__read_product_price()}

    def get_product_id(self, category_len):
        """Getting product id for buying, deleting or updating"""
        print("-"*50)
        id = input("Enter id of the product or R to return: ").strip().lower()
        if id == "r":
            return "r"     
        else:   
            try:
                if id.isdigit():
                    id = int(id)
                if id >= category_len:
                    print("-"*50)
                    print("We don't have product with such id, try again.")
                    self.get_product_id(category_len)
                else:
                    return id
            except TypeError:
                    print("-"*50)
                    print("Invalid input, try again.")
                    self.get_product_id(category_len)

    def get_number_of_product(self, db_number_of_product):
        """Getting number of products to buy""" 
        try:
            print("-"*50)
            number = int(input("Enter number of the products: "))
            if number > db_number_of_product:
                print("-"*50)
                print("We don't have enough number, try again.")
                self.get_number_of_product(db_number_of_product)
            elif number == 0:
                print("-"*50)
                print("You can't buy 0 products, try again.")
                self.get_number_of_product(db_number_of_product)
            else:
                return number
        except ValueError:
            print("-"*50)
            print("Invalid input, try again.")
            self.get_number_of_product(db_number_of_product)

    def refill_balance(self, balance):
        """Refilling balance"""
        try:
            print("-"*50)
            balance = int(input("Enter the number to top up the account(For example: 300): "))
            return balance
        except ValueError:
            print("-"*50)
            print("Invalid input, try again.")
            self.refill_balance()

    def show_products_list(self, category):
        """Printing list of products of certain category"""
        print("-"*50)    
        for product in category:
            print("ID: ", product["ID"])
            print("Name: ", product["Name"])
            print("Number: ", product["Number"])
            print("Price: ", product["Price"])
            print("-"*50)

    def is_empty_category(self, category_len):
        if len(category_len) == 0:
            print("-"*50)
            print("This category is empty!")

    def availability_check(self, number, db_number_of_product):
        if db_number_of_product - number < 0:
            print("-"*50)
            print("We don't have this number of products.")
            return False
        else:
            return True

    def balance_check(self, balance, number, category):
        if balance - category[id]["Price"]*number < 0:
            print("-"*50)
            print("You don't have enough money to buy this product.")
            return False
        else:
            return True