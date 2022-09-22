from unicodedata import category
from console import *
from database import *

user = Console()
db = Database()
is_active = True
action = ""
current_category = ""

def create_new_password():
    new_password = user.create_password()
    if new_password == "r":
        main_action()
    else:
        db.password = new_password
        main_action()

def db_login():
    if user.login(db.password) == "r":
        main_action()
    else:
        db_action = user.read_db_action()
        return db_action

def main_action():
    action = user.read_user_action()
    match action:
        case "b":
            user.show_balance(db.balance)
            main_action()
        case "c":
            category_name = user.get_category_name()
            if category_name == "r":
                main_action()
            else:
                category = db.get_products_list(category_name)
                category_len = len(category)
                if not user.is_empty_category(category_len):    
                    user.show_products_list(category)
                    id = user.get_product_id(category_len)
                    if id != "r":
                        number = user.get_number_of_product()
                        if (user.availability_check(number, category[id]["Number"]) and
                        user.balance_check(db.balance, number, category[id]["Price"])):
                            db.buy_product(category_name, id, number)
        case "a":
            if db.password != "":
                db_login()
            else:
                create_new_password()
        case "q":
            pass



print("Welcome to the DATS e-shop!")
