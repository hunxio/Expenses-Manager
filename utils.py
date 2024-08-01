# Modules
import customtkinter

# Clear all widgets in the grid except those in column 0
def clear_widgets(application: object) -> None:
    # Checks for all the widgets childrens in the application
    for widget in application.winfo_children():
        # info retrieves the informations about the grid system (for rows and columns)
        info = widget.grid_info()
        # For all the columns which aren't 0 it will 'delete' them
        if info.get('column') != 0:
            widget.grid_forget()


def create_table(application: object, headers: list, rows: list) -> None:
    # It creates a new label on row0, for each header it founds, shifting position by 1
    for col_index, header in enumerate(headers):
        header_label = customtkinter.CTkLabel(application, text=header, font=("Monsterrat", 16))
        header_label.grid(row=0, column=col_index + 1, padx=10, pady=0)

    # It creates a new label on row0+1 and column0+1, at every cycle it will shift by 1 position
    for row_index, row in enumerate(rows):
        for col_index, cell in enumerate(row):
            cell_label = customtkinter.CTkLabel(application, text=cell, font=("Monsterrat", 15))
            cell_label.grid(row=row_index + 1, column=col_index + 1, padx=10, pady=0)