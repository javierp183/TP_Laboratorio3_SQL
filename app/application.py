from consolemenu import *
from consolemenu.items import *


class Listados:
    pass


def action(name):
    print("\nHello from action {}!!!\n".format(name))
    Screen().input("Press [Enter] to continue")


def mensaje():
    print("salida del mensaje")
    Screen().input("Press [Enter] to continue")


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

    # Add all the items to the root menu
    menu.append_item(FunctionItem("Listar Operadores 1", action, args=["one"]))
    menu.append_item(FunctionItem("Listar Clientes 2", action, args=["two"]))
    menu.append_item(FunctionItem("Listar Ventas 3", action, args=["three"]))
    menu.append_item(
        FunctionItem("Listar Ventas por Producto 4", action, args=["four"])
    )
    menu.append_item(FunctionItem("Listar Clientes por Pais 5", mensaje))

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
