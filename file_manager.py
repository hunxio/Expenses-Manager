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
        chart_data = []
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        row = list(csv_reader)
        for expense in row:
            category, value = expense[1], float(expense[2])
            if chart_data == []:
                chart_data.append([category, value])
            elif chart_data != []:
                for _ in range(len(chart_data)):
                    items_category, items_value = chart_data[_][0], chart_data[_][1]
                    #TODO: FIX ITEMS_VALUE NOT UPDATING AFTER CALCULATING HOW MUCH IT IS
                    if category == items_category:
                        items_value = float(items_value) + float(value)
        return chart_data


get_category_value("data.csv")