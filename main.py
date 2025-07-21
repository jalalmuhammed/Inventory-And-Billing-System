
from authentication import (authenticate,register_new_user,
                            check_manager,check_admin,change_user_password,remove_user)
from inventory import Inventory
from billing import Bill
from reporting import SalesReport
sales_report = SalesReport()
inventory = Inventory()


def manager_dashboard(inventory):
    manager = inventory
    while True:
        try:
            choice = int(input("1: View Inventory 2: Add Product "
                               "3: Update Product 4: Remove Product 0: Exit: ").strip())

            if choice == 0:
                print("Exiting Manager Dashboard.")
                break
            elif choice == 1:
                manager.show_all_product()
            elif choice == 2:
                try:
                    product_name = input("Enter Product Name: ")
                    product_price = float(input("Enter Product Price: "))
                    product_stock = int(input("Enter Product Quantity: "))

                    manager.add_product(product_name,product_price,product_stock)
                except ValueError:
                    print("Enter Valid Values.")
            elif choice == 3:
                try:
                    product_id = int(input("Enter Product ID To Update Product: ").strip())
                    option = int(input("I Want To Update, 1: Price 2: Stock  : "))

                    if option == 1:
                        updated_price = float(input("Enter Updated Price: ").strip())
                        manager.update_product(product_id= product_id,
                                               product_price=updated_price,product_quantity=None)
                    elif option == 2:
                        updated_stock = int(input("Enter Updated Stock: ").strip())
                        manager.update_product(product_id=product_id,
                                               product_price=None,product_quantity=updated_stock)
                    else:
                        print("enter Valid Options")
                        return
                except ValueError:
                    print("Enter Valid Values.")
            elif choice == 4:
                product_id = int(input("Enter Product ID To Remove Product: ").strip())
                manager.remove_product(product_id)
            else:
                print("Print Valid Options.")
                break
        except Exception as e:
            print(f"Error Occurred.{e}")


def cashier_dashboard(inventory,sales_report):
    cashier = Bill(inventory)
    for_bill_history = sales_report
    while True:
        try:
            choice = int(input("1: Add Product To Cart 2: View Cart "
                               "3: Get Total Bill 4: Show Bill History "
                               "5: Clear Cart 0: Exit: ").strip())

            if choice == 0:
                print("Exiting Cashier Dashboard.")
                break

            elif choice == 1:
                try:
                    product_id = int(input("Enter Product ID: ").strip())
                    product_quantity = int(input("Enter Quantity: ").strip())

                    cashier.add_to_cart(product_id=product_id,product_quantity=product_quantity)
                except ValueError:
                    print("Enter Valid Input.")

            elif choice == 2:
                cashier.show_cart()

            elif choice == 3:
                cashier.save_total_bill()

            elif choice == 4:
                for_bill_history.show_all_bill()

            elif choice == 5:
                cashier.clear_cart()

            else:
                print("Enter Valid Options.")

        except ValueError:
            print("Enter Valid Inputs.")

def analyst_dashboard(sales_report):
    analyst = sales_report
    while True:
        try:
            choice = int(input("1: Store Overview 2: Filter By Date "
                               "3: Show By ID 4: Show All Bills "
                               "5: Export to CSV 0: Exit: ").strip())

            if choice == 0:
                print("Exiting Analyst Dashboard.")
                break

            elif choice == 1:
                analyst.overview()

            elif choice == 2:
                start_date = input("Enter Start Date: ")
                end_date = input("Enter End Date: ")
                analyst.filter_by_date(start_date,end_date)

            elif choice == 3:
                analyst.show_bill_by_id()

            elif choice == 4:
                analyst.show_all_bill()

            elif choice == 5:
                analyst.export_to_csv()

            else:
                print("Enter Valid Options.")

        except ValueError:
            print("Enter Valid Inputs.")

def admin_dashboard():
    user_input = int(input("1: Register New User \n2: Edit User Password \n3: Remove A User: ").strip())
    if user_input == 1:
        register_new_user()

    elif user_input == 2:
        change_user_password()

    elif user_input == 3:
        remove_user()

    else:
        print("Enter Valid Options")
        return

def main():
    """This is the main function,which take user choice and call the favorable functions"""

    print("WELCOME TO THE SOFTWARE.")
    try:
        choice = int(input("""
            How do you Want to Enter,
            1: Manager 2: Cashier 3:Analyst 4: Admin
            : """))

        #we specially check whether this user have access to the manager dashboard separately
        if choice == 1:
            is_authenticated, user_name = check_manager()
            if is_authenticated:
                print(f"{user_name.title()},Welcome To Your Manager Dashboard. ")
                manager_dashboard(inventory)

        elif choice in [2,3]:
            is_authenticated,user_name = authenticate()
            if is_authenticated:
                if choice == 2:
                    print(f"{user_name.title()},Welcome To Your Cashier Dashboard. ")
                    cashier_dashboard(inventory,sales_report)

                elif choice == 3:
                    print(f"{user_name.title()},Welcome To Your Analyst Dashboard. ")
                    analyst_dashboard(sales_report)

        elif choice == 4:
            is_authenticated, user_name = check_admin()
            if is_authenticated:
                print(f"{user_name.title()},Welcome To Admin Dashboard.")
                admin_dashboard()

        else:
            print("Enter Valid Options.")

    except Exception as e:
        print(f"Error Occurred: {e}")


if __name__ == "__main__":
    main()