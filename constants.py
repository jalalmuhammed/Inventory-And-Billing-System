import os

#this is where all the constants are going to be stored

DATA_FOLDER = "data"
AUTH_DATA_FILE = os.path.join(DATA_FOLDER,"authentication.json")
INVENTORY_DATA_FILE = os.path.join(DATA_FOLDER,"inventory.json")
SALES_DATA_FILE = os.path.join(DATA_FOLDER, "sales.json")
CSV_DATA_FILE = os.path.join(DATA_FOLDER,"Export.csv")