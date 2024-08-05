# Root files
import Constants
import add_expense
import check_expense
import graphic_chart
# Modules
import customtkinter
import os
from PIL import Image


def gui():
    app = customtkinter.CTk()
    # Sets application color based on device system color
    customtkinter.set_appearance_mode("system")

    # Icon Image
    app.iconbitmap("media/icon.ico")

    # Logo Image on side bar
    logo = customtkinter.CTkImage(
        light_image=Image.open(Constants.LOGO_IMAGE_PATH),
        dark_image=Image.open(Constants.LOGO_IMAGE_PATH),
        size=(120, 120),
    )
    logo_label = customtkinter.CTkLabel(app, image=logo, text="")
    logo_label.grid(row=0, column=0, padx=0, pady=20)

    # Window Settings
    app.title("Gestore di spese")
    app.geometry("750x550")

    # Text Label side bar
    side_title_label = customtkinter.CTkLabel(
        app, text="Manager Spese", fg_color="transparent", font=("Montserrat", 18)
    )
    side_title_label.grid(row=1, column=0, padx=10, pady=0)

    # Button Widgets
    button_add_expense = customtkinter.CTkButton(
        app, text="Aggiungi spesa", command=lambda: add_expense.add_expense(app)
    )
    button_add_expense.grid(row=2, column=0, padx=10, pady=15)

    button_check_expense = customtkinter.CTkButton(
        app, text="Controlla spese", command=lambda: check_expense.check_expense(app)
    )
    button_check_expense.grid(row=3, column=0, padx=10, pady=15)

    button_graphic_chart = customtkinter.CTkButton(
        app, text="Spesa Mensile", command=lambda: graphic_chart.make_graph(app)
    )
    button_graphic_chart.grid(row=4, column=0, padx=10, pady=15)

    app.mainloop()


if __name__ == "__main__":
    gui()
