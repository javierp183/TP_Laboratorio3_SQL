from consolemenu import *
from consolemenu.items import *
from database import Operador
from string import Template


def action(name):
    print("\nHello from action {}!!!\n".format(name))
    Screen().input("Press [Enter] to continue")


def buscar_operador_por_usuario():
    # usuario = input("Ingrese Usuario del Operador: ")
    usr = Operador().atributos(usuario="javier")
    print(usr)

    # myt = Template(
    #     "\t Pais: $pais \n \
    #     Usuario: $usuario \n \
    #     Nombre(s): $nombre \n \
    #     Apellido(s): $apellido"
    # )
    # mys = myt.substitute(
    #     pais="{}".format(usr[1]),
    #     usuario="{}".format(usr[2]),
    #     nombre="{}".format(usr[3]),
    #     apellido="{}".format(usr[4]),
    # )
    # print(mys)

    Screen().input("Press [Enter] to continue")


def ingreso():
    print("ingrese nombre:")
    nombre = input()
    print("tu nombre es {}".format(nombre))
    Screen().input("Press [Enter] to continue")


# telecentro: 21337970 reclamo internet


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
    menu.append_item(
        FunctionItem("Listar Atributos del Operador", buscar_operador_por_usuario)
    )
    menu.append_item(FunctionItem("Listar Clientes 2", action, args=["two"]))
    menu.append_item(FunctionItem("Listar Ventas 3", action, args=["three"]))
    menu.append_item(
        FunctionItem("Listar Ventas por Producto 4", action, args=["four"])
    )
    menu.append_item(
        FunctionItem("Listar Clientes por Pais 5", buscar_operador_por_usuario)
    )
    menu.append_item(FunctionItem("Tu nombre", ingreso))

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
