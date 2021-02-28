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
from database import Venta, Producto, Operador, Cliente, Ventas_x_Productos
from os import environ


def venta():
    data = {}
    total_de_productos = 0
    total_valor_venta = 0
    fecha_venta = datetime.now().date()
    operador_id = Operador().Id(environ.get("APPUSER"))
    cliente = input("Ingrese el CUIL del cliente: ")
    cliente_id = Cliente().Id(cliente)
    producto = input("Ingrese los productos a comprar (pantalon,zapatillas,..): ")
    cantidad = input("Ingrese la cantidad de los mismos (3,2,..): ")

    producto = list(producto.split(","))
    cantidad = list(cantidad.split(","))

    zip_iterator = zip(producto, cantidad)
    data = dict(zip_iterator)

    for k, v in data.items():
        if Producto().buscar(k)[0][3] > 0:
            nuevo_stock = Producto().buscar(k)[0][3] - int(v)
            total_de_productos = total_de_productos + int(v)
            total_valor_venta = int(v) * Producto().buscar(k)[0][2]

            Producto().actualizar_stock(k, nuevo_stock)
        else:
            print("No hay Stock de producto '{}'".format(k))

    Venta().procesar_ventas(
        total_de_productos, total_valor_venta, fecha_venta, operador_id, cliente_id
    )

    venta_id = int(Venta().buscar(total_de_productos))

    print("Resumen de venta: ")
    print("Productos: ")
    for k, v in data.items():
        print("producto: " + k + " cantidad: " + v)
        Ventas_x_Productos().agregar(
            venta_id, Producto().Id(k), v, Producto().Precio(k)
        )

    print("Venta procesada!")

    # Venta().procesar_ventas(data=data)

    # print("Desea generar el ticket de venta?: ")
    # ticket = input("[1|SI] [2|NO]")
    Screen().input("Press [Enter] to continue")
    pass


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

    menu.append_item(FunctionItem("Venta de producto", venta))

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
