# Root files
from utils import clear_widgets, create_table
from file_manager import open_csv_file
# Modules
import customtkinter
import pandas as pd

def check_expense(application: object) -> None:
    # Delets columns content where column > 0
    clear_widgets(application)
    headers, rows = open_csv_file("data.csv", "data.csv")
    create_table(application, headers, rows)