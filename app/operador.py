from datetime import datetime
from consolemenu import *
from consolemenu.items import *
from database import Operador
from string import Template

print("test")


def listar():
    print(Operador().listar())
    Screen().input("Press [Enter] to continue")


def main():
    # Create the root menu
    menu = MultiSelectMenu(
        "Menu Operadores",
        "TP laboratorio 3 - SQL Server",
        epilogue_text=(
            "Selecciona una o mas opciones separadas por ,(comma) o por extension"
            "de numeros Por ejemplo:  1,2,3   o   1-4   o   1,3-4"
        ),
        exit_option_text="Salir",
    )  # Customize the exit text

        # Add all the items to the root menu
    menu.append_item(FunctionItem("Listar Operadores", listar))

    menu.start()
    menu.join()



main()
