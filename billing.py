import json

from inventory import Inventory
from datetime import datetime
import os,constants
inventory = Inventory()

class FileManager:
    def __init__(self):
        """make sure there is a file,if not creating one"""
        if not os.path.isfile(constants.SALES_DATA_FILE):
            with open(constants.SALES_DATA_FILE,"w") as file:
                json.dump([],file)

    def load_data(self):
        with open(constants.SALES_DATA_FILE,"r") as file:
            return json.load(file)

    def save_file(self,data):
        with open(constants.SALES_DATA_FILE,"w") as file:
            json.dump(data,file, indent=4)



class BillItem:
    def __init__(self,product,product_quantity):
        self.product_id = product.product_id
        self.product_name = product.product_name
        self.product_quantity = product_quantity
        self.product_price = product.product_price


    def bill_info(self):
        return (f"{self.product_id}        | {self.product_name}       "
                f"   | {self.product_quantity}         | {self.product_price}")


class Bill:
    bill_id = 1000

    def __init__(self,inventory):
        self.cart = []
        self.total_bill = []
        self.inventory = inventory
        self.file = FileManager()
        self.sales_data = self.file.load_data()

        if self.sales_data:
            last_bill = self.sales_data[-1]["bill_id"]
            Bill.bill_id = last_bill

        Bill.bill_id += 1
        self.bill_id = Bill.bill_id

        self.total_bill.append(f" Bismi Super Markert \n"
                               f"Bill ID: {self.bill_id}  Date& Time: "
                               f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} \n"
                               f"Product ID | Product Name  | Quantity  | Unit Price")

    def add_to_cart(self,product_id,product_quantity):
        #check whether product exist in inventory with this product id
        product = self.inventory.find_product_by_id(product_id)
        if not product:
            print(f"Product Not Found With ID: {product_id}")
            return
        if product.product_quantity < product_quantity:
            print(f"Current stock of product ID: {product_id},is not sufficient"
                  f" to Process the Order,Current Stock: {product.product_quantity}")
            return

        bill = BillItem(product,product_quantity)
        self.total_bill.append(bill.bill_info())
        self.cart.append(bill)
        product.reduce_stock(product_quantity)
        self.inventory.save_all_products()


    def add_total(self):
        total = 0

        for billitem in self.cart:
            product_sum = billitem.product_quantity * billitem.product_price
            total += product_sum


        return total,f"Total Amount Payable Before GST: {total}"

    def apply_gst(self,total):
        gst = total * 0.18
        total += gst
        return round(total,2),f"Total Amount Payable After 18% GST: {round(total,2)}"

    def apply_discount(self,total):
        discount = total * 0.05
        total -= discount
        return round(total,2),f"Total Amount Payable After 5% Discount: {round(total,2)}"
    def get_bill_item(self):
        bill = []

        for bills in self.cart:
            bill.append({
            "product_id" : bills.product_id,
            "product_name" : bills.product_name,
            "product_price" : bills.product_price,
            "product_quantity" : bills.product_quantity
            })

        return bill

    def save_total_bill(self):
        """This function displays Bill to the user and saving the whole bill to the json file."""
        amount_total,amount_text = self.add_total()
        self.total_bill.append(amount_text)
        gst_added_total,gst_added_text = self.apply_gst(amount_total)
        self.total_bill.append(gst_added_text)
        discount_added_total,discount_added_text = self.apply_discount(gst_added_total)
        self.total_bill.append(discount_added_text)

        thankyou_msg = "Thank You,Visit Again."
        self.total_bill.append(thankyou_msg)


        data = {
            "bill_id" : self.bill_id,
            "sales_date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "sales_items" : self.get_bill_item(),
            "total_bill" : amount_total,
            "total_after_gst" : gst_added_total,
            "total_after_discount" : discount_added_total,
            "amount_payable" : discount_added_total

        }

        self.sales_data.append(data)
        self.file.save_file(self.sales_data)
        print("Sales Data Added Successfully.")
        for bill in self.total_bill:
            print(bill)

    def show_cart(self):
        for bill in self.cart:
            print(bill.bill_info())


jalal = Bill(inventory)
jalal.add_to_cart(103,4)
jalal.add_to_cart(100,2)
jalal.save_total_bill()
