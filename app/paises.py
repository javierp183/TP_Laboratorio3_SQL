from datetime import datetime
from consolemenu import *
from consolemenu.items import *
from database import Pais
from string import Template


def listar_paises():
    print(Pais().lista())
    Screen().input("Press [Enter] to continue")
    pass


def buscar_pais():
    pais_nombre = input("ingrese nombre de pais: ")
    pais_nombre = pais_nombre.lower()
    print(Pais().buscar(pais_nombre))
    Screen().input("Press [Enter] to continue")


def ingresar_pais():
    pais_nombre = input("Ingrese nombre de pais: ")
    pais_nombre = pais_nombre.lower()
    if Pais().agregar(pais_nombre) == "23000":
        print("Este registro ya existe, por favor ingrese otro")
    else:
        print("Nuego registro ingresado")
    Screen().input("Press [Enter] to continue")


def eliminar_pais():
    pais_nombre = input("Ingrese el nombre del pais a eliminar: ")
    pais_nombre = pais_nombre.lower()
    Pais().borrar(pais_nombre)
    print("Pais '{}' eliminado".format(pais_nombre))
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

    menu.append_item(FunctionItem("Listar Paises registrados", listar_paises))
    menu.append_item(FunctionItem("Ingresar nuevo Pais", ingresar_pais))
    menu.append_item(FunctionItem("Eliminar Pais", eliminar_pais))

    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
