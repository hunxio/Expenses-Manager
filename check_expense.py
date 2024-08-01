# Modules
import customtkinter
import pandas as pd

def check_expense(application: object) -> None:
    # Title label
    application.grid_columnconfigure(1, weight=1)
    title_label = customtkinter.CTkLabel(
        application,
        text="Resoconto delle spese",
        fg_color="transparent",
        font=("Monsterrat", 18),
    )
    title_label.grid(row=0, column=1, padx=20, pady=0)