#Write a Python program to create a class representing a shopping cart. 
#Include methods for adding and removing items, and calculating the total price. 

class Cart:
    def __init__(self):
        self.carts = []
        self.item = ["skirt", "shirt", "trousers", "dress"]
        self.price = {"skirt":35, "shirt":56, "trousers":74, "dress":83}
        self.color = ["red", "yellow", "white", "black"]
        self.size = ["S", "M", "L", "XL"]
#Method for adding items    
    def add(self, item, color, size):
        if item in self.item and color in self.color and size in self.size:
            self.cart.append({"item" : item, "color" : color , "size" : size })
            print("Item was added")
        else:
            print("Invalid choice")
        return
#Method for removing items    
    def remove(self, item, color, size):
        if item in self.carts:
            self.cart.remove({"item" : item, "color" : color , "size" : size })
            print("Item was removed")
        else:
            print("Invalid choice")
        return
#Method for calculating the total price 
    def calculator(self, item):
        if item == "skirts" in self.carts or item == "shirt" in self.carts or item == "trousers" in self.carts or item == "dress" in self.carts:
            total_cost = sum(self.item[item["item"]] for item in self.price)
            print(total_cost)
  
cart = Cart()
        
print("Welcome in our shop!")
print("1) Add item")
print("2) Delete item")
print("3) Calculate total price")

print("Enter the number: ")
choice = int(input())
    
if choice == 1:
    print("Items: skirt, shirt, trousers, dress")
    item = str(input())
    print("Colors: red, yellow, white, black")
    color = str(input())
    print("Size: S, M, L, XL")
    size = str(input())
    cart.add(item, color, size)
elif choice == 2:
    print("Enter the item, color and size from your list: ")
    item = str(input())
    color = str(input())
    size = str(input())
    cart.remove(item, color, size)
elif choice == 3:
    cart.calculator(cart.carts)
else:
    print("Wrong number")
