from billing import FileManager
from collections import Counter
import csv,constants

class SalesReport:
    def __init__(self):
        self.file = FileManager()
        self.sales_data = self.file.load_data()
        self.total_revenue = 0
        self.total_bill = 0
        self.average_bill_size = 0
        self.largest_bill = None


    def get_by_id(self,bill_id):
        for bill in self.sales_data:
            if bill["bill_id"] == bill_id:
                return bill

    def show_bill_by_id(self,bill_id):
        bill = self.get_by_id(bill_id)
        product_list = ""
        for data in bill['sales_items']:
            product_list += f"Product ID: {data['product_id']} | Product Name: {data['product_name']} | product Price: {data['product_price']} | Product Qnty: {data['product_quantity']}\n"


        show_bill= (f"Bill ID: {bill['bill_id']}\n"
                    f"Bill Date Time: {bill['sales_date_time']}\n"
                    f"Purchased Items: \n{product_list}\n"
                    f"Total Amount Paid: {bill['amount_payable']}\n"
                    f"{'*'*50}\n")
        print(show_bill)

    def show_all_bill(self):
        for bill in self.sales_data:
            self.show_bill_by_id(bill['bill_id'])


    def add_total(self):
        amount = 0
        count = 0
        for bill in self.sales_data:
            amount += bill["amount_payable"]
            count += 1

        self.total_revenue = amount
        self.total_bill = count
        self.average_bill_size = round((self.total_revenue / self.total_bill),2)

    def highest_bill(self):
        max_bill = max(self.sales_data,key=lambda bill : bill["amount_payable"])
        self.largest_bill = max_bill

    def top_products(self):
        product_counter = Counter()

        for bill in self.sales_data:
            for item in bill["sales_items"]:
                product_counter[item["product_name"]] += item["product_quantity"]

        top3_products = product_counter.most_common(3)
        result = " "
        for indx,(product,number) in enumerate(top3_products,start=1):
            result += f"{indx}. {product} - {number}\n"

        return result.strip()

    def filter_by_date(self,start_date,end_date):
        filtered_data = []
        for data in self.sales_data:
            if start_date <= data["sales_date_time"] <= end_date:
                filtered_data.append(data)

        for bill in filtered_data:
            self.show_bill_by_id(bill['bill_id'])

    def export_to_csv(self):
        with open(constants.CSV_DATA_FILE,"w") as file:
            writer = csv.writer(file)
            writer.writerow([
                "bill_id", "sales_date_time", "product_id", "product_name",
                "product_quantity", "product_price", "line_total", "bill_total"
            ])
            for bill in self.sales_data:
                for item in bill["sales_items"]:
                    line_total = item["product_quantity"] * item["product_price"]
                    writer.writerow([
                        bill["bill_id"],
                        bill["sales_date_time"],
                        item["product_id"],
                        item["product_name"],
                        item["product_quantity"],
                        item["product_price"],
                        line_total,
                        bill["amount_payable"]
                    ])

        print("Exported To Csv.")


    def overview(self):
        self.add_total()
        self.highest_bill()
        over_view = (f"Total Revenue: {self.total_revenue} \n"
                     f"Total Bills: {self.total_bill} \n"
                     f"Average Bill Size: {self.average_bill_size}\n\n"
                     
                     f"Top Selling Products\n{self.top_products()}\n\n"
                     
                     f"Highest Value Bill:\n"
                     f"Bill ID : {self.largest_bill['bill_id']}\n"
                     f"Total Paid: {self.largest_bill['amount_payable']}\n"
                     f"Date: {self.largest_bill['sales_date_time']}")

        print(over_view)


