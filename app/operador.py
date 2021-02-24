from datetime import datetime
from consolemenu import *
from consolemenu.items import *
from database import Operador
from string import Template
from password import encriptacion


def valido_usuario():
    usuario = input("Ingrese el nombre de usuario del Operador: ")
    clave_db = Operador().clave(usuario)
    clave = input("Ingrese la clave del usuario: ")
    clave = encriptacion(clave)

    if clave == clave_db:
        return True

    return False


def listar():
    print(Operador().listar())
    # valido_usuario()
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

    pais = pais.lower()
    usuario = usuario.lower()
    nombre = nombre.lower()
    apellido = apellido.lower()
    clave = encriptacion(clave.lower())

    Operador().agregar(
        pais="1",
        usuario=usuario,
        nombre=nombre,
        apellido=apellido,
        clave=clave,
        alta=1,
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
    # print(usr["Usuario"])
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
        ndata["usuario_original"] = usr["Usuario"]

        Operador().actualizar(usuario=usuario, update=opcion, usrdata=ndata)
    Screen().input("Press [Enter] to continue")


def cantidad_de_operadoras():
    print("La cantidad de operadores es: {}".format(Operador().cantidad()))
    Screen().input("Press [Enter] to continue")


def cantidad_de_operadores_activos():
    print("La cantidad de operadores activos es: {}".format(Operador().activos()))
    Screen().input("Press [Enter] to continue")


def cantidad_de_operadores_noactivos():
    print("La cantidad de operadores (no)activos es: {}".format(Operador().noactivos()))
    Screen().input("Press [Enter] to continue")


def listar_operadores_inactivos():
    pass


def baja():
    usuario = input("Ingresar nombre de usuario: ")
    Operador().baja(usuario)
    print("Usuario: {} dado de baja".format(usuario))
    Screen().input("Press [Enter] to continue")


def alta():
    usuario = input("Ingresar nombre de usuario: ")
    Operador().alta(usuario)
    print("Usuario: {} dado de alta".format(usuario))
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
    menu.append_item(FunctionItem("Alta de Operador", alta))
    menu.append_item(FunctionItem("Baja de Operador", baja))
    menu.append_item(FunctionItem("Eliminar Operador", eliminar_operador))
    menu.append_item(
        FunctionItem("Consultar Cantidad de Operadores", cantidad_de_operadoras)
    )
    menu.append_item(
        FunctionItem(
            "Consultar Cantidad de Operadores Activos", cantidad_de_operadores_activos
        )
    )
    menu.append_item(
        FunctionItem(
            "Consultar Cantidad de Operadores No Activos",
            cantidad_de_operadores_noactivos,
        )
    )

    menu.start()
    menu.join()


if valido_usuario():
    main()
else:
    print("Usuario o Clave no valido!")
