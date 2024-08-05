import customtkinter
from matplotlib import pyplot
import numpy

from file_manager import get_category_value

def make_graph(application: object) -> None:
    try:
        print(get_category_value("data.csv"))
    except FileNotFoundError:
        application.columnconfigure(1, weight=1)
        error_message_label = customtkinter.CTkLabel(application, text="Please add an expense to create a graph.", fg_color="transparent", font=("Monsterrat", 18))
        error_message_label.grid(row=0, column=1, padx=0, pady=0, sticky="WE")
