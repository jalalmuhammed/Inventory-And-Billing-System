from products import Product
import os
import json
from constants import INVENTORY_DATA_FILE

class FileManager:
    """This class handle the file operations smoothly in the inventory"""
    def __init__(self):
        #make sure there is a file,if not creating one
        if not os.path.isfile(INVENTORY_DATA_FILE):
            with open(INVENTORY_DATA_FILE,"w") as file:
                json.dump([],file)

    def load_file(self):
        with open(INVENTORY_DATA_FILE,"r") as file:
            return json.load(file)

    #save date to the file
    def save_file(self,data):
        with open(INVENTORY_DATA_FILE,"w") as file:
            json.dump(data, file, indent=4)




class Inventory:
    def __init__(self):
        #creating a list of instances of product class.
        self.products = []
        self.file = FileManager()

    def add_product(self,name,price,stock):
        """this function add a product to inventory."""
        product = Product(name,price,stock)

        self.products.append(product)
        print(f"The {name} Added To Products.")

    def find_product_by_id(self,product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        print(f"There is No Product Asociated With This ID: {product_id}")

    def find_product_by_name(self,product_name):
        for product in self.products:
            if product.product_name == product_name:
                return product
        print(f"There is No Product Named As: {product_name}")

    def update_product(self,product_id,product_price=None,product_quantity=None):
        for product in self.products:
            if product.product_id == product_id:
                if product_price is not None:
                    product.update_price(product_price)
                    print(f"Product Price Updated to: {product_price}")
                if product_quantity is not None:
                    product.update_stock(product_quantity)
                    print(f"Product Stock Updated to: {product_quantity}")

    def remove_product(self,product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return
        print(f"No Product Associated With ID: {product_id}")


    def show_all_inventory(self):
        for product in self.products:
            product.show_product_info()

    def save_file(self,data):
        self.file.save_file(data)

    def load_file(self):
        data = self.file.load_file()
        return data




