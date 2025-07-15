class Product:
    """This product class create a single product and allow inventory
    class to manage the whole product list.we will pass the instance of
    this clss to inventory class later. """
    count_id = 100

    def __init__(self,product_name,product_price,product_quantity,product_id= None):
        if product_id is not None:
            self.product_id = product_id
        else:
            self.product_id = Product.count_id
            Product.count_id += 1

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
        data =(f"Product ID: {self.product_id} | "
              f"Product Name: {self.product_name} | "
              f"Product Price: {self.product_price} | "
              f"Product Stock: {self.product_quantity}")

        return data

    def to_save_dictionary(self):
        product_info = {
            "product_id" : self.product_id,
            "product_name" : self.product_name,
            "product_price" : self.product_price,
            "product_stock" : self.product_quantity
        }
        return product_info

    @classmethod
    def from_saved_dictionary(cls, dictionary):
        """accessing as dictionary and returning as instance,"""
        return cls(
            product_id=dictionary["product_id"],
            product_name=dictionary["product_name"],
            product_price=dictionary["product_price"],
            product_quantity=dictionary["product_stock"]

        )


