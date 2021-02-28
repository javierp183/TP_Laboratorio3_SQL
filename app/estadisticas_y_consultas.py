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
from string import Template
import subprocess
from database import Ventas_x_Productos, Pais, Venta
from database import Cliente, Operador


def cuantas_veces_se_vendio_un_producto():
    producto = input("Ingrese le nombre del producto: ")
    print(Ventas_x_Productos().cuantas_veces_se_vendio_un_producto(producto.lower()))
    Screen().input("Press [Enter] to continue")


def suma_total_de_ventas_por_pais():
    for i in Pais().suma_total_por_pais():
        print("Nombre País: {} Suma de Dinero: {}".format(i[0], i[1]))
    Screen().input("Press [Enter] to continue")


def total_clientes_por_paises():
    for i in Pais().total_clientes_por_pais():
        print("Nombre País: {} Cantidad de Clientes: {}".format(i[0], i[1]))
    Screen().input("Press [Enter] to continue")


def consulta_cantidad_ventas_por_anio():
    anio = input("Ingrese el año: ")
    print(Venta().consulta_ventas_por_anio(anio))
    Screen().input("Press [Enter] to continue")


def consulta_de_ventas_por_sexo():
    print(Cliente().consulta_ventas_por_sexo())
    Screen().input("Press [Enter] to continue")


def ventas_por_año_por_operador():
    operador = input("Ingrese operador: ")
    anio = input("Ingrese el año (YYYY): ")

    print(Operador().ventas_por_año(operador, anio))
    Screen().input("Press [Enter] to continue")


def edad_media_clientes():
    print(Cliente().edad_media_vista())
    Screen().input("Press [Enter] to continue")


def clientes_que_superan_edad_media():
    for i in Cliente().superan_media_vista():
        print("Nombre: {} Apellido: {} Email: {}".format(i[0], i[1], i[2]))
    Screen().input("Press [Enter] to continue")


def main():

    # Create the root menu
    menu = MultiSelectMenu(
        "Menu Ventas",
        "TP laboratorio 3 - SQL Server",
        epilogue_text=(
            "Selecciona una o mas opciones separadas por ,(comma) o por extension"
            "de numeros Por ejemplo:  1,2,3   o   1-4   o   1,3-4"
        ),
        exit_option_text="Salir",
    )  # Customize the exit text

    menu.append_item(
        FunctionItem(
            "Cantidad de ventas de un producto", cuantas_veces_se_vendio_un_producto
        )
    )
    menu.append_item(
        FunctionItem("Suma total de dinero por Pais", suma_total_de_ventas_por_pais),
    )
    menu.append_item(
        FunctionItem("Total de clientes por Pais", total_clientes_por_paises),
    )
    menu.append_item(
        FunctionItem("Cantidad de Ventas por año", consulta_cantidad_ventas_por_anio),
    )
    menu.append_item(
        FunctionItem(
            "Cantidad de Ventas por Sexo(M:asculino|F:emenino)",
            consulta_de_ventas_por_sexo,
        ),
    )
    menu.append_item(
        FunctionItem("Ventas por año por Operador", ventas_por_año_por_operador,),
    )
    menu.append_item(
        FunctionItem("Edad media de los Clientes ( View )", edad_media_clientes,),
    )
    menu.append_item(
        FunctionItem(
            "Clientes que superar la edad Media ( View )",
            clientes_que_superan_edad_media,
        ),
    )

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
