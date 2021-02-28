"""
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the  nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from datetime import datetime
from consolemenu import *
from consolemenu.items import *

from database import Operador
from string import Template
import subprocess
from password import encriptacion
from os import environ


def valido_usuario():
    usuario = input("Ingrese el nombre de usuario del Operador: ")
    clave_db = Operador().clave(usuario)
    clave = input("Ingrese la clave del usuario: ")
    clave = encriptacion(clave)

    if clave == clave_db:
        if Operador().estado(usuario):
            environ["APPUSER"] = usuario
            return True

    return False


def menu_operadores():
    # print(Operador().listar())
    subprocess.call(["python", "./operador.py"])
    Screen().input("Press [Enter] to continue")


def menu_clientes():
    subprocess.call(["python", "./clientes.py"])
    # print(Cliente().listar())
    Screen().input("Press [Enter] to continue")


def menu_paises():
    # print(Pais().lista())
    subprocess.call(["python", "./paises.py"])
    Screen().input("Press [Enter] to continue")
    pass


def menu_productos():
    # print(Producto().listar())
    subprocess.call(["python", "./productos.py"])
    Screen().input("Press [Enter] to continue")
    pass


def menu_ventas():
    subprocess.call(["python", "./ventas.py"])
    Screen().input("Press [Enter] to continue")
    pass


def menu_estadisticas():
    subprocess.call(["python", "./estadisticas_y_consultas.py"])
    Screen().input("Press [Enter] to continue")
    pass


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
    menu.append_item(FunctionItem("Gestion de Usuarios Operadores", menu_operadores))
    menu.append_item(FunctionItem("Gestion de Usuarios Clientes", menu_clientes))
    menu.append_item(FunctionItem("Gestion de Productos", menu_productos))
    menu.append_item(FunctionItem("Gestion de Ventas", menu_ventas))
    menu.append_item(FunctionItem("Consultas y Estadisticas", menu_estadisticas))

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    if valido_usuario():
        main()
    else:
        print("Usuario o Clave no valido o Usuario deshabilitado!")
