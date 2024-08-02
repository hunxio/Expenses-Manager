# Root files
from utils import clear_widgets, create_table
from file_manager import open_csv_file
# Modules
import customtkinter
import pandas as pd

def check_expense(application: object) -> None:
    # Delets columns content where column > 0
    clear_widgets(application)
    try:
        headers, rows = open_csv_file("data.csv", "data.csv")
        create_table(application, headers, rows)
    except (TypeError, FileNotFoundError):
        application.columnconfigure(1, weight=1)
        error_message_label = customtkinter.CTkLabel(application, text="Please add an expense to create the file.", fg_color="transparent", font=("Monsterrat", 18))
        error_message_label.grid(row=0, column=1, padx=0, pady=0, sticky="WE")