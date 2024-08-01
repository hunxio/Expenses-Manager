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