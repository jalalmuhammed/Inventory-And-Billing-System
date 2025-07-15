
from authentication import authenticate,register_new_user,check_manager
from inventory import Inventory
from billing import Bill
inventory = Inventory()


def manager_dashboard(inventory):
    manager = inventory
    while True:
        try:
            choice = int(input("1: View Inventory 2: Add Product "
                               "3: Update Product 4: Remove Product 0: Exit: ").strip())

            if choice == 0:
                print("Exiting Dashboard.")
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


def cashier_dashboard(inventory):
    cashier = Bill(inventory)
    while True:
        try:
            choice = int(input("1: Add Product To Cart 2: View Cart "
                               "3: Get Total Bill 4: Show Bill History "
                               "5: Clear Cart 0: Exit: ").strip())

            if choice == 0:
                print("Exiting Dashboard.")
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
                cashier.show_bill_history()

            elif choice == 5:
                cashier.clear_cart()

            else:
                print("Enter Valid Options.")

        except ValueError:
            print("Enter Valid Inputs.")

def main():
    """This is the main function,which take user choice and call the favorable functions"""

    print("WELCOME TO THE SOFTWARE.")
    try:
        choice = int(input("""
            How do you Want to Enter,
            1: Manager 2: Cashier 3:Analyst 4: Register 
            : """))

        #we specially check whether this user have access to the manager dashboard separately
        if choice == 1:
            is_authenticated, user_name = check_manager()
            if is_authenticated:
                print(f"{user_name},Welcome To Your Manager Dashboard. ")
                manager_dashboard(inventory)

        elif choice in [2,3]:
            is_authenticated,user_name = authenticate()
            if is_authenticated:
                if choice == 2:
                    print(f"{user_name},Welcome To Your Cashier Dashboard. ")
                    cashier_dashboard(inventory)

                elif choice == 3:
                    print(f"{user_name},Welcome To Your Analyst Dashboard. ")

        elif choice == 4:
            register_new_user()

        else:
            print("Enter Valid Options.")

    except Exception as e:
        print(f"Error Occurred: {e}")


if __name__ == "__main__":
    main()