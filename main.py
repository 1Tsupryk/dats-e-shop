from console import *
from database import *

user = Console()
db = Database()
is_active = True


print("Welcome to the DATS e-shop!")
user.read_user_action()

while is_active:
    match user.current_position:
        case "start":
            if user.action == "b":
                user.show_balance(db.balance)
            elif user.action == "c":
                user.get_category(db)
                user.is_empty_category(user.category, db)
            elif user.action == "a":
                if db.password == "" or db.password == "r" :
                    user.password_creation(db)
                else:
                    user.ask_for_password(db.password)
            elif user.action == "q":
                print("-"*50)
                is_active = False
        case "category_choosing":
            user.current_position = "product_buying"
            user.show_products_list(user.category)
            user.get_product_id(user.category)
            if user.id != "r":
                user.get_number_of_product(user.category)
                user.buy_product(user.category, user.id, user.number, db)
                user.read_user_action()
        case "password_creation":
            user.read_user_action()
        case "password_check":
            user.read_db_action()
        case "db_action":
            if user.db_action == "add":
                user.get_category(db)
                if user.category_name != "r":
                    user.read_product_chars()
                    db.ADD(user.category, user.chars)
                    user.read_db_action()
            elif user.db_action == "delete":
                user.get_category(db)
                if user.category_name != "r":
                    user.is_empty_category(user.category, db)
                    user.show_products_list(user.category)
                    user.get_product_id(user.category)
                    if user.id != "r":
                        db.DELETE(user.category, user.id)
                        user.read_db_action()
            elif user.db_action == "update":
                user.get_category(db)
                if user.category_name != "r":
                    user.is_empty_category(user.category, db)
                    user.show_products_list(user.category)
                    user.get_product_id(user.category)
                    if user.id != "r":
                        user.read_product_chars()
                        db.UPDATE(user.category, user.id, user.chars)
                        user.read_db_action()
            elif user.db_action == "earn":
                db.EARN()
                user.read_db_action()
            

        
        
        