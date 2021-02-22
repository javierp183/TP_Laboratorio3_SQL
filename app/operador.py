from datetime import datetime
from consolemenu import *
from consolemenu.items import *
from database import Operador
from string import Template


def listar():
    print(Operador().listar())
    Screen().input("Press [Enter] to continue")


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


def ingresar_nuevo_operador():
    pais = input("Ingrese el Pais: ")
    usuario = input("Ingrese nombre de usuario: ")
    nombre = input("Ingrese nombre del Operador: ")
    apellido = input("Ingrese apellido: ")
    clave = input("Ingrese clave: ")
    Operador().agregar(
        pais="1", usuario=usuario, nombre=nombre, apellido=apellido, clave=clave, alta=1
    )
    Screen().input("Press [Enter] to continue")


def eliminar_operador():
    usuario = input("Ingrese nombre de usuario del Operador: ")
    Operador().borrar(usuario=usuario)
    print("Operador {} eliminado".format(usuario))
    Screen().input("Press [Enter] to continue")


def actualizar_datos_operador():
    usuario = input("Ingrese nombre de usuario: ")
    usr = Operador().actualizar(usuario=usuario)
    print(usr)
    print("Desea actualizar los datos de este usuario?")
    opcion = input("0 no | 1 si: ")
    if opcion:
        ndata = {}
        pais = input("Nuevo Pais: ")
        usuario = input("Nuevo Usuario: ")
        nombre = input("Nuevo nombre: ")
        apellido = input("Nuevo apellido: ")
        clave = input("Nueva clave: ")
        fecha = datetime.now().date()
        alta = input("Estado de Alta: ")
        ndata["pais"] = pais
        ndata["usuario"] = usuario
        ndata["nombre"] = nombre
        ndata["apellido"] = apellido
        ndata["clave"] = clave
        ndata["fecha"] = fecha
        ndata["alta"] = alta

        Operador().actualizar(usuario=usuario, update=opcion, usrdata=ndata)
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
    menu.append_item(
        FunctionItem("Informacion del Operador", buscar_operador_por_usuario)
    )
    menu.append_item(FunctionItem("Ingrese nuevo Operador", ingresar_nuevo_operador))
    menu.append_item(FunctionItem("Actualizar Operador", actualizar_datos_operador))
    menu.append_item(FunctionItem("Eliminar Operador", eliminar_operador))

    menu.start()
    menu.join()


main()