
class Product:
    """This product class create a single product and allow inventory
    class to manage the whole product list.we will pass the instance of
    this clss to inventory class later. """
    product_id = 100

    def __init__(self,product_name,product_price,product_quantity):
        Product.product_id += 1
        self.product_id = Product.product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity


    def update_price(self,new_price):
        if new_price > 0:
            self.product_price = new_price

    def update_stock(self,quantity):
            self.product_quantity = quantity

    def reduce_stock(self,quantity):
        if (self.product_quantity - quantity) >= 0:
            self.product_quantity -= quantity

    def show_product_info(self):
        print(f"Product ID: {self.product_id} | "
              f"Product Name: {self.product_name} | "
              f"Product Price: {self.product_price:.2f} | "
              f"Product Stock: {self.product_quantity}")


