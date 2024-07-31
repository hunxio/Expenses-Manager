# Root files
import Constants

# Modules
import os
import pandas as pd


# Checks if the file exists in the path or not
def path_existance() -> bool:
    path = Constants.CSV_FILE_PATH
    isFile = os.path.isfile(path)
    return isFile


# Initializes and/or appends data to a .csv file depending on path_existances call
def csv_file(data: dict) -> None:
    df = pd.DataFrame(data)
    csv_file = "data.csv"
    if not path_existance():
        df.to_csv(csv_file, mode="a", index=False, header=True)
    else:
        df.to_csv(csv_file, mode="a", index=False, header=False)


if __name__ == "__main__":
    main()
