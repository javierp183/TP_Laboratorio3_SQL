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


def buscar_cliente_por_email():
    email = input("Ingrese Email del Cliente: ")
    clt = Cliente().atributos(email)

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
    menu.append_item(FunctionItem("Ingrese nuevo Operador", ingresar_nuevo_operador))
    menu.append_item(FunctionItem("Informaicon del Cliente", buscar_cliente_por_email))
    menu.append_item(FunctionItem("Listar Paises registrados", listar_paises))
    menu.append_item(FunctionItem("Listar Productos", listar_productos))
    menu.append_item(FunctionItem("Tu nombre", ingreso))

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
