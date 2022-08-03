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

    def add_product(self, category, characteristics):
        """Adding new product to the list of certain category"""        
        self.new_ID = {"ID":len(category)}
        category.append({**self.new_ID, **characteristics})

    def delete_product(self, category, id):
        """Removing a specific product from the list"""        
        del category[id]
        try:
            for product in category[id:]:
                product["ID"] -= 1
        except IndexError:
            pass
    
    def update_product(self, category_name, id, changes):
        """Updating a specific product from the list"""
        self.new_ID = {"ID":id}  
        getattr(self, category_name)[id] = {**self.new_ID, **changes}

    def buy_product(self, category, id, number):
        """Reduces the balance and quantity of the product"""        
        self.balance -= category[id]["Price"]*number
        category[id]["Number"] -= number
        if category[id]["Number"] == 0:
            self.DELETE(category, id)

    def get_products_list(self, category_name):
        return getattr(self, category_name)
