# Root files
import Constants
import file_manager

# Modules
import customtkinter
import pandas as pd


def add_expense(application) -> None:

    global payment_check, category_check, name_expense_input, amount_expense_input

    # Entry-label for Expense's name
    name_expense_label = customtkinter.CTkLabel(
        application,
        text="Nome della spesa",
        fg_color="transparent",
        font=("Monsterrat", 18),
    )
    name_expense_label.grid(row=0, column=1, padx=20, pady=0)
    name_expense_input = customtkinter.CTkEntry(
        application, placeholder_text="Spesa, Ristorante, Bolletta luce ...", width=250
    )
    name_expense_input.grid(row=0, column=2, padx=0, pady=0)

    # Category expense
    category_check = customtkinter.StringVar(value="")
    bills_radio = customtkinter.CTkRadioButton(
        application,
        text="Bolletta",
        command=lambda: category_event(category_check),
        variable=category_check,
        value="bills",
        hover=True,
        font=("Monsterrat", 17),
    )
    bills_radio.grid(row=1, column=1, padx=0, pady=0)
    grocery_radio = customtkinter.CTkRadioButton(
        application,
        text="Spesa",
        command=lambda: category_event(category_check),
        variable=category_check,
        value="grocery",
        hover=True,
        font=("Monsterrat", 17),
    )
    grocery_radio.grid(row=1, column=2, padx=0, pady=0)
    meds_radio = customtkinter.CTkRadioButton(
        application,
        text="Medicinali",
        command=lambda: category_event(category_check),
        variable=category_check,
        value="meds",
        hover=True,
        font=("Monsterrat", 17),
    )
    meds_radio.grid(row=2, column=1, padx=0, pady=0)
    other_radio = customtkinter.CTkRadioButton(
        application,
        text="Altro",
        command=lambda: category_event(category_check),
        variable=category_check,
        value="other",
        hover=True,
        font=("Monsterrat", 17),
    )
    other_radio.grid(row=2, column=2, padx=0, pady=0)

    # Amount expense
    amount_expense_label = customtkinter.CTkLabel(
        application,
        text="Costo della spesa",
        fg_color="transparent",
        font=("Monsterrrat", 18),
    )
    amount_expense_label.grid(row=3, column=1, padx=0, pady=0)
    amount_expense_input = customtkinter.CTkEntry(
        application, placeholder_text="100,00", width=180
    )
    amount_expense_input.grid(row=3, column=2, padx=0, pady=0)
    euro_label = customtkinter.CTkLabel(
        application, text="€", fg_color="transparent", font=("Monsterrat", 18)
    )
    euro_label.grid(row=3, column=3, padx=0, pady=0)

    # Payment type
    payment_check = customtkinter.StringVar(value="")
    cash_radio = customtkinter.CTkRadioButton(
        application,
        text="Contanti",
        command=lambda: payment_event(payment_check),
        variable=payment_check,
        value="cash",
        hover=True,
        font=("Monsterrat", 17),
    )
    cash_radio.grid(row=4, column=1, padx=0, pady=0)
    card_radio = customtkinter.CTkRadioButton(
        application,
        text="Carta di Credito",
        command=lambda: payment_event(payment_check),
        variable=payment_check,
        value="card",
        hover=True,
        font=("Monsterrat", 17),
    )
    card_radio.grid(row=4, column=2, padx=0, pady=0)

    # Submit button
    submit_button = customtkinter.CTkButton(
        application, text="Conferma", command=submit_add_expense
    )
    submit_button.grid(row=5, column=1, padx=0, pady=0)


def category_event(variable_name: str) -> str:
    return variable_name.get()


def payment_event(variable_name: str) -> str:
    return variable_name.get()


def submit_add_expense() -> None:
    name_expense = name_expense_input.get().title().strip()
    amount_expense = amount_expense_input.get()
    try:
        amount_expense = "{:.2f}".format(int(amount_expense)).strip()
    except ValueError:
        amount_expense_replace = amount_expense.replace(",", ".")
        amount_expense = "{:.2f}".format(float(amount_expense_replace)).strip()
        print(type(amount_expense))
    category = category_event(category_check).title()
    payment = payment_event(payment_check).title()

    data = {
        "Name": [name_expense],
        "Category": [category],
        "Amount Expense": [amount_expense],
        "Payment Type": [payment],
    }

    file_manager.csv_file(data)
