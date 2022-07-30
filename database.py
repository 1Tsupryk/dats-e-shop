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

    def ADD(self, category, characteristics):
        """Adding new product to the list of certain category"""        
        self.new_ID = {"ID":len(category)}
        category.append({**self.new_ID, **characteristics})
        print("-"*50)
        print("Product successfully added!")

    def DELETE(self, category, id, position="db_action"):
        """Removing a specific product from the list"""        
        del category[id]
        try:
            for product in category[id:]:
                product["ID"] -= 1
            if position == "db_action":
                print("-"*50)
                print("Product successfully deleted!")
        except IndexError:
            if position == "db_action":
                print("-"*50)
                print("Product successfully deleted!")
    
    def UPDATE(self, category, id, changes):
        """Updating a specific product from the list"""
        self.new_ID = {"ID":id}  
        category[id] = {**self.new_ID, **changes}
        print("-"*50)
        print("Product successfully updated!")

    def EARN(self):
        """Refilling balance"""
        try:
            print("-"*50)
            self.balance = int(input("Enter the number to top up the account(For example: 300): "))
        except ValueError:
            print("-"*50)
            print("Invalid input, try again.")
            self.EARN()
