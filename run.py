# cannot create products and update inventory in one step using a CSV import in Shopify
# you need to use separate CSV files for each task
# To create new products, use a Products CSV import, and for updating inventory, use an Inventory CSV file

from os import listdir
from os.path import isfile, join, splitext
import pandas as pd
from tabulate import tabulate
from pick import pick

products_df = pd.DataFrame()
inventory_df = pd.DataFrame()

# DEV ONLY : list all files in ./data
TEST_DATA_DIR = './data'
onlyfiles = [f for f in listdir(TEST_DATA_DIR) if isfile(join(TEST_DATA_DIR, f))]
print(onlyfiles)

# Prompt user, choose vendor
options = ['Nike', 'ASICS', 'ON']
vendor, index = pick(options, "Choose a vendor:")

# Prompt user choose file
path, i = pick(onlyfiles, "Choose file")

# Prompt user choose location
location, i = pick(["Renegade Running", "Los Angeles"], "Choose location")
print(f"Importing {vendor} order sheet from {path} to location")

# 
filename, file_extension = splitext(f"{TEST_DATA_DIR}/{path}")
if (file_extension == '.xlsx'):
    df = pd.read_excel(f"{TEST_DATA_DIR}/{path}")
elif (file_extension == '.csv'):
    df = pd.read_csv(f"{TEST_DATA_DIR}/{path}")

# Define result dataframe and common columns
# REQUIRED: HANDLE, LOCATION, SKU, or Option1 Name and Option1 Value
products_df["Vendor"] = vendor

# Handle
# Title
# Option 1 Name
# Option 1 Value
# SKU
# inventory_df["Location"] = location
# On hand (current)
# On hand (new)

products_df["Product Category"] = "Apparel & Accessories > Shoes > Athletic Shoes"
products_df["Option1 Name"] = "Color"
products_df["Option2 Name"] = "Shoe size"
products_df["Option2 Linked To"] = "product.metafields.shopify.shoe-size"
products_df["Variant Inventory Tracker"] = "shopify"
products_df["Variant Price"] = ""

# products_df["Variant Requires Shipping"]
# products_df["Variant Taxable"]
# products_df["Variant Barcode"]
# products_df["SEO Title"]
# products_df["SEO Description"]
# Description
# Published on online store
# Option1 LinkedTo
# Weight value (grams)
# Inventory Quantity
# Continue selling when out of stock
# Price

products_df["Fulfillment service"] = "manual"
products_df["Status"] = "draft"

# Map columns
match vendor:
    case "Nike":
        # Action for pattern1
        print ("Running Nike column mapping")
        print(df.columns.tolist())
    case "ASICS":
        # TODO: handle multiple products in the same order sheet
        print ("Running ASICS column mapping")
        products_df["Title"] = df["Item name"] # TODO: get unique values from Item name
        products_df["Handle"] = df.at[0, "Item name"].lower().replace("/", "-").replace(" ", "-") # TODO: and concat with Color name from same row
        products_df["Option1 Value"] = df["Color name"]
        products_df["Variant SKU"] = df["Trading code"]
        products_df["Cost per item"] = df["Unit price"]
    case _:
        # Default action if no other case matches
        print ("Running default case")


# CONVERT DATAFRAME TO CSV AND SAVE FILE
print(tabulate(products_df, headers="keys", tablefmt="pretty"))
print(tabulate(inventory_df, headers="keys", tablefmt="pretty"))
# df.to_csv(f"{TEST_DATA_DIR}/{path}", index=None, header=True)
