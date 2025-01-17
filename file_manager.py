# Root files
import Constants

# Modules
import os
import pandas as pd
import csv


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


def get_data(file_path: str, file: str) -> list:
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        rows = list(csv_reader)
        return headers, rows


def get_category_value(file_path: str) -> list:

    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        row = list(csv_reader)

        chart_data = []
        for expense in row:
            category, value = expense[1], float(expense[2])
            found = False
            for item in chart_data:
                if item[0] == category:
                    item[1] += value
                    found = True
                    break
            if not found:
                chart_data.append([category, value])
        return chart_data

if __name__ == "__main__":
    main()