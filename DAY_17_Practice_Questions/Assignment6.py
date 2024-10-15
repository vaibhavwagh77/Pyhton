#Online Food Management System

class food:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def display_info(self):
        print(f"food :{self.name}")
        print(f"price: $ {self.price}")
        print(f"category: $ {self.category}")
item1 = food("Maggi", 10,"main course")
item2 = food("IceCream", 30,"Desert")
item1.display_info()
print("- - - - -")
item2.display_info()
