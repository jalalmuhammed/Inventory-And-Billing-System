import os
import json
import constants

class FileManager:
    """This class assist with file handling,loading and saving the file efficiently."""
    def __init__(self):
        if not os.path.isdir(constants.DATA_FOLDER):
            os.makedirs(constants.DATA_FOLDER)

        if not os.path.isfile(constants.AUTH_DATA_FILE):
            with open(constants.AUTH_DATA_FILE, "w") as file:
                json.dump([], file)

    def load_file(self):
        with open(constants.AUTH_DATA_FILE, "r") as file:
            return json.load(file)

    def save_file(self,data):
        with open(constants.AUTH_DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

file = FileManager()

def register_new_user():
    """This function does the user registration for admins,
     and store their information in authenticate.json file."""
    try:
        name = input("Enter Your name: ").lower().strip()
        email = input("Enter Your Email: ").lower().strip()
        password = input("Enter Your Password: ").lower().strip()

        def validate_position():
            position = input("Enter Your Position "
                         "manager/cashier/analyst:").lower().strip()
            if position not in ["manager","cashier","analyst"]:
                print("Invalid Role")
                return None
            else:
                return position

        position = validate_position()
        if not position:
            print("Registration Not completed")
            return

        user_registered_data = {
            "name" : name,
            "email" : email,
            "password" : password,
            "position" : position
        }
        current_user_data = file.load_file()
        current_user_data.append(user_registered_data)
        file.save_file(current_user_data)

        print(f"{name}, Your Registration Completed.")

    except Exception as e:
        print(f"Error Occurred: {e}")


def change_user_password():
    user_name = input("Enter User Name To Update Password: ").strip()
    found = False
    current_data = file.load_file()

    for user in current_data:
        if user["name"] == user_name:
            found = True
            new_password = input("Enter New Password: ")
            if new_password != "":
                user["password"] = new_password
                file.save_file(current_data)
                print("Password Updated Successfully.")
                return

    if not found:
        print("No User Associated With That Name.")
        return


def remove_user():
    user_name = input("Enter User Name To Remove User: ").strip()
    found = False
    current_data = file.load_file()

    for user in current_data:
        if user["name"] == user_name:
            found = True
            current_data.remove(user)
            file.save_file(current_data)
            print("User Removed Successfully.")
            return

    if not found:
        print("No User Associated With That Name.")
        return

datas = file.load_file()
def authenticate():
    """This function authenticate the user and return a
    boolean value to the calling person along with username."""

    #checking for user
    try:
        user_found = None
        user_name = input("Enter User Name: ").strip().lower()
        for data in datas:
            if data.get("name") == user_name:
                user_found = data
                break

        if not user_found:
            print(f"There is no User Name as {user_name}")
            return False,None

        #verify password
        for _ in range(3):
            password = input("Enter Your Password: ").lower().strip()
            if user_found.get("password") == password:
                    return True,user_name
            else:
                print("Wrong Password.")
        else:
            print("Too many Failed attempt")
            return False,None

    except Exception as e:
        print(f"Error Occurred as: {e}")

def check_manager():
    """This function specifically check weather the user
    have a managerial access"""
    try:
        is_authenticated,user_name =authenticate()
        if is_authenticated:
            for user_data in datas:
                if user_data.get("name") == user_name:
                    if user_data.get("position") == "manager":
                        return True,user_name
                    else:
                        print(f"Access Denied,{user_name} You Are Not A Manager.")
                        return False,None

    except Exception as e:
        print(f"Error Occurred as: {e}")

def check_admin():
    """This function specifically check weather the user
    have Admin access"""
    try:
        is_authenticated,user_name =authenticate()
        if is_authenticated:
            for user_data in datas:
                if user_data.get("name") == user_name:
                    if user_data.get("position") == "admin":
                        return True,user_name
                    else:
                        print(f"Access Denied,{user_name} You Are Not Admin.")
                        return False,None

    except Exception as e:
        print(f"Error Occurred as: {e}")