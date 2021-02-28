from datetime import datetime
from consolemenu import *
from consolemenu.items import *
from database import Cliente
from string import Template


def listar_clientes():
    for i in Cliente().listar():
        print(
            "Nacionalidad: {} Nombre: {} Apellido: {} email: {} Sexo: {} CUIL: {} Fecha de Naciomiento: {} Fecha de Registro: {}".format(
                i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]
            )
        )
    Screen().input("Press [Enter] to continue")


def buscar_cliente_por_email():
    email = input("Ingrese Email del Cliente: ")
    clt = Cliente().atributos(email)

    print(clt)
    Screen().input("Press [Enter] to continue")


def ingresar_nuevo_cliente():
    data = {}
    pais = input("Ingrese el Pais: ")
    apellido = input("Ingrese apellido del Cliente: ")
    nombre = input("Ingrese nombre del Cliente: ")
    email = input("Ingrese el email: ")
    sexo = input("Ingrese el sexo (M|F): ")
    cuil = input("Ingrese el Cuil: ")  # transformar a unique en la base de datos
    fechanac = input("Ingrese la fecha de nacimiento (dd/mm/yy): ")
    date_time_obj = datetime.strptime(fechanac, "%d/%m/%y")
    fechareg = datetime.now().date()

    data["pais"] = pais
    data["apellido"] = apellido
    data["nombre"] = nombre
    data["email"] = email
    data["cuil"] = cuil
    data["fechanac"] = date_time_obj.date()
    data["fechareg"] = fechareg
    data["sexo"] = sexo

    if Cliente().agregar(data) == "23000":
        print("Este registro ya existe, por favor intrese otro")
    else:
        print("Nuevo registro ingresado")
    Screen().input("Press [Enter] to continue")


def borrar_cliente():
    email = input("Ingrese email de cliente a borrar: ")
    Cliente().borrar(email)
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

    menu.append_item(FunctionItem("Listar Clientes", listar_clientes))
    menu.append_item(FunctionItem("Informacion del Cliente", buscar_cliente_por_email))
    menu.append_item(FunctionItem("Ingrese nuevo Cliente", ingresar_nuevo_cliente))
    menu.append_item(FunctionItem("Eliminar Cliente", borrar_cliente))

    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
