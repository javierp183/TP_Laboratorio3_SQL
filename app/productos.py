from datetime import datetime
from consolemenu import *
from consolemenu.items import *
from database import Pais, Producto
from string import Template
import subprocess


def listar_productos():
    print(Producto().listar())
    Screen().input("Press [Enter] to continue")
    pass


def main():

    # Create the root menu
    menu = MultiSelectMenu(
        "Menu Principal",
        "TP laboratorio 3 - SQL Server",
        epilogue_text=(
            "Selecciona una o mas opciones separadas por ,(comma) o por extension"
            "de numeros Por ejemplo:  1,2,3   o   1-4   o   1,3-4"
        ),
        exit_option_text="Salir",
    )  # Customize the exit text

    menu.append_item(FunctionItem("Listar Productos", listar_productos))

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
