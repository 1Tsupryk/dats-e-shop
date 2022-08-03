class Database:
    
    def __init__(self):
        self.balance = 100
        self.password = ""
        self.new_ID = {}
        self.cpu = []
        self.ram = []
        self.power = []
        self.motherboard = []
        self.video = []
        self.fan = []

    def add_product(self, category_name, characteristics):
        """Adding new product to the list of certain category"""
        current_category = self.get_products_list(category_name)
        self.new_ID = {"ID":len(current_category)}
        current_category.append({**self.new_ID, **characteristics})

    def delete_product(self, category_name, id):
        """Removing a specific product from the list"""
        current_category = self.get_products_list(category_name)
        del current_category[id]
        try:
            for product in current_category[id:]:
                product["ID"] -= 1
        except IndexError:
            pass
    
    def update_product(self, category_name, id, changes):
        """Updating a specific product from the list"""
        current_category = self.get_products_list(category_name)
        self.new_ID = {"ID":id}  
        current_category[id] = {**self.new_ID, **changes}

    def buy_product(self, category_name, id, number):
        """Reduces the balance and quantity of the product"""
        current_category = self.get_products_list(category_name)
        self.balance -= current_category[id]["Price"]*number
        current_category[id]["Number"] -= number
        if current_category[id]["Number"] == 0:
            self.DELETE(current_category, id)

    def get_products_list(self, category_name):
        return getattr(self, category_name)