from consolemenu import *
from consolemenu.items import *
from database import Operador, Cliente, Pais, Producto
from string import Template


def buscar_operador_por_usuario():
    usuario = input("Ingrese Usuario del Operador: ")
    usr = Operador().atributos(usuario)

    myt = Template(
        "\t Pais: $pais \n \
        Usuario: $usuario \n \
        Nombre(s): $nombre \n \
        Apellido(s): $apellido \n \
        Fecha de Registro: $fecha \n "
    )

    mys = myt.substitute(
        pais="{}".format(usr[1]),
        usuario="{}".format(usr[2]),
        nombre="{}".format(usr[3]),
        apellido="{}".format(usr[4]),
        fecha="{}".format(usr[6]),
    )

    print(mys)
    Screen().input("Press [Enter] to continue")


def buscar_cliente_por_email():
    email = input("Ingrese Email del Cliente: ")
    clt = Cliente().atributos(email)

    # myt = Template(
    #     "\t Pais: $pais \n \
    #     Usuario: $usuario \n \
    #     Nombre(s): $nombre \n \
    #     Apellido(s): $apellido \n \
    #     Fecha de Registro: $fecha \n "
    # )

    # mys = myt.substitute(
    #     pais="{}".format(usr[1]),
    #     usuario="{}".format(usr[2]),
    #     nombre="{}".format(usr[3]),
    #     apellido="{}".format(usr[4]),
    #     fecha="{}".format(usr[6]),
    # )

    print(clt)
    Screen().input("Press [Enter] to continue")


def buscar_product_por_descripcion():
    descripcion = input("Ingrese descripcion: ")
    pass


def listar_paises():
    print(Pais().lista())
    Screen().input("Press [Enter] to continue")
    pass


def listar_productos():
    print(Producto().listar())
    Screen().input("Press [Enter] to continue")
    pass


def action(name):
    print("\nHello from action {}!!!\n".format(name))
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
        FunctionItem("Informacion del Operador", buscar_operador_por_usuario)
    )
    menu.append_item(FunctionItem("Informaicon del Cliente", buscar_cliente_por_email))
    menu.append_item(FunctionItem("Listar Paises registrados", listar_paises))
    menu.append_item(FunctionItem("Listar Productos", listar_productos))
    menu.append_item(
        FunctionItem("Listar Clientes por Pais 5", buscar_operador_por_usuario)
    )
    menu.append_item(FunctionItem("Tu nombre", ingreso))

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
