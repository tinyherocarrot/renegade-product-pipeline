from os import listdir
from os.path import isfile, join, splitext
import pandas as pd
from pick import pick

TEST_DATA_DIR = './data'

onlyfiles = [f for f in listdir(TEST_DATA_DIR) if isfile(join(TEST_DATA_DIR, f))]

print(onlyfiles)
options = ['Nike', 'ASICS', 'ON']
option, index = pick(options, "Choose a vendor:")
print(f"Vendor: {option}")

path, i = pick(onlyfiles, "Choose file")
print("Importing sheets from " + option + ", " + path)

filename, file_extension = splitext(f"{TEST_DATA_DIR}/{path}")
if (file_extension == '.xlsx'):
    df = pd.read_excel(f"{TEST_DATA_DIR}/{path}")
    print(df.columns.tolist())
elif (file_extension == '.csv'):
    df = pd.read_csv(f"{TEST_DATA_DIR}/{path}")

#MAP
match option:
    case "Nike":
        # Action for pattern1
        print ("Running Nike column mapping")
    case "ASICS":
        # Action for pattern2
        print ("Running ASICS column mapping")
    case _:
        # Default action if no other case matches
        print ("Running default case")


# CONVERT DATAFRAME TO CSV AND SAVE FILE
# df.to_csv(f"{TEST_DATA_DIR}/{path}", index=None, header=True)
