# Root files
from utils import clear_widgets
from file_manager import get_category_value
# Modules
import customtkinter
from matplotlib import pyplot
import numpy

def make_graph(application: object) -> None:
    # Delets columns content where column > 0
    clear_widgets(application)
    try:
        data_chart = get_category_value("data.csv")
    except FileNotFoundError:
        application.columnconfigure(1, weight=1)
        error_message_label = customtkinter.CTkLabel(application, text="Please add an expense to create a graph.", fg_color="transparent", font=("Monsterrat", 18))
        error_message_label.grid(row=0, column=1, padx=0, pady=0, sticky="WE")

    category, value = [], []
    for items in data_chart:
        category.append(items[0])
        value.append(items[1])

    figure = pyplot.figure(figsize=(8, 5))
    pyplot.pie(value, labels=category)
    pyplot.show()