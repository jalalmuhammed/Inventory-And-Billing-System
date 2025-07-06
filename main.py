from authentication import authenticate,register_new_user,check_manager


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

        elif choice in [2,3]:
            is_authenticated,user_name = authenticate()
            if is_authenticated:
                if choice == 2:
                    print(f"{user_name},Welcome To Your Cashier Dashboard. ")
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