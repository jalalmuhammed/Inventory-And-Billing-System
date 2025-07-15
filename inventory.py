import os
import json
from constants import INVENTORY_DATA_FILE
from products import Product

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
    """This class handle inventory,it creates product as
    instance of Product Class and store it in products"""

    def __init__(self):
        #creating a list of instances of product class.
        self.products = []
        self.file = FileManager()

        #load existing file data into sel.product
        saved_file = self.file.load_file()
        max_id = 99
        for data_file in saved_file:
            product = Product.from_saved_dictionary(data_file)
            self.products.append(product)
            max_id = max(max_id, product.product_id)

        Product.count_id = max_id + 1  # ensure ID continues from max

    def save_all_products(self):
        product_to_save = []
        for product in self.products:
            product_to_save.append(product.to_save_dictionary())

        self.file.save_file(product_to_save)

    def add_product(self,name,price,stock):
        """this function add a product to inventory."""

        #checking existing product to avoid duplicate file saving
        for product in self.products:
            if product.product_name == name:
                print(f"Product {name},Already Exist in This Name.")
                return
        product = Product(name,price,stock)

        self.products.append(product)
        self.save_all_products()
        print(f"The {name} Added To Products.")

    def find_product_by_id(self,product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        print(f"There is No Product Associated With This ID: {product_id}")

    def find_product_by_name(self,product_name):
        for product in self.products:
            if product.product_name == product_name:
                return product
        print(f"There is No Product Named As: {product_name}")

    def update_product(self,product_id,product_price=None,product_quantity=None):
        """This function Updates price and quantity,
        if we didn't update the value remains as same"""

        for product in self.products:
            if product.product_id == product_id:
                change_made = False

                if product_price is not None:
                    product.update_price(product_price)
                    print(f"Product ID: {product_id}, Price Updated to: {product_price}")
                    change_made = True

                if product_quantity is not None:
                    product.update_stock(product_quantity)
                    print(f"Product ID: {product_id}, Stock Updated to: {product_quantity}")
                    change_made = True

                if change_made:
                    self.save_all_products()

    def remove_product(self,product_id):
        """This function can remove a product with its ID"""

        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                self.save_all_products()
                print(f"Product Associated With ID: {product_id} Removed.")
                return
        print(f"No Product Associated With ID: {product_id}")


    def show_all_product(self):
        """This function shows entire inventory"""
        product_to_show = []
        for product in self.products:
            product_to_show.append(product.show_product_info())

        for product in product_to_show:
            print(f"{product}\n")

    def save_file(self,data):
        self.file.save_file(data)

    def load_file(self):
        data = self.file.load_file()
        return data




