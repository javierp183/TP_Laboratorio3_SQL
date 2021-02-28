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

# --------------------------------------------------------------------------- #
# Imports
# --------------------------------------------------------------------------- #

import pyodbc
from loader import Config
import datetime

# Configuracion de base de datos
config = Config().settings()


def leer_consulta(file=None):
    out = open(file, "r")
    return out.read()


class Database:
    def __init__(self, database=None):
        server = "localhost\sqlexpress"
        server = "myserver,port"
        server = "tcp:localhost"

        if database != None:
            database = "{}".format(database)
        else:
            database = "{}".format(config["database"]["nombre"])

        username = "{}".format(config["database"]["usuario"])
        password = "{}".format(config["database"]["clave"])
        cnxn = pyodbc.connect(
            "DRIVER={};SERVER=".format(config["database"]["driver"])
            + server
            + ";DATABASE="
            + database
            + ";UID="
            + username
            + ";PWD="
            + password,
            autocommit=True,
        )
        self.cursor = cnxn.cursor()

    def execquery(self, query):
        try:
            self.cursor.execute("{}".format(query))

            return self.cursor.fetchall()
        except pyodbc.Error as ex:
            return ex.args[0]

        # except:
        #    return None
        # return

        # try:
        #     return self.cursor.fetchall()
        # except pyodbc.ProgrammingError as e:
        #     print("Salida de pyodbc error")
        #     print(str(e))
        #     if "Previous SQL was not a query." in str(e):
        #         return "Previous SQL was not a query."

    def createdb(self, database):
        """ Create database """
        try:
            self.cursor.execute("create database {};".format(database))
            return True
        except:
            return False

    def dropdb(self, database):
        try:
            self.cursor.execute("drop database {};".format(database))
        except pyodbc.ProgrammingError as e:
            if str(e).__contains__("not exist"):
                print("database not exist")


class Operador(Database):
    def atributos(self, usuario):
        return self.execquery(
            "select O.ID,P.Nombre,O.Usuario,O.Nombres,O.Apellidos,O.Clave,O.FechaReg \
            from Operador as O  \
                inner join Pais as P on P.ID = O.IDPais \
             where usuario = '{}';".format(
                usuario
            )
        )[0]

    def agregar(self, pais, usuario, nombre, apellido, clave, alta):
        fecha = datetime.datetime.now()
        print(
            "insert into Operador(IDPais,Usuario,Nombres,Apellidos,Clave,FechaReg,Alta) values ('{}','{}','{}','{}','{}',CAST(N'{}' AS Date),{});".format(
                pais, usuario, nombre, apellido, clave, fecha.date(), alta
            )
        )
        return self.execquery(
            "insert into Operador(IDPais,Usuario,Nombres,Apellidos,Clave,FechaReg,Alta) values ('{}','{}','{}','{}','{}',CAST(N'{}' AS Date),{});".format(
                pais, usuario, nombre, apellido, clave, fecha.date(), alta
            )
        )

    def baja_logica(self, usuario):
        pass

    def estado(self, usuario):
        return self.execquery(
            "select O.Alta from Operador as O where usuario = '{}'".format(usuario)
        )[0][0]

    def borrar(self, usuario):
        return self.execquery(
            " \
        delete from Operador where usuario = '{}';".format(
                usuario
            )
        )

    def actualizar(self, usuario, update=0, usrdata=0):
        if not update:
            data = {}
            usr = self.execquery(
                "select * from Operador where usuario = '{}';".format(usuario)
            )[0]

            print(usr)

            data = {
                "Pais": usr[1],
                "Usuario": usr[2],
                "Nombre": usr[3],
                "Apellido": usr[4],
                "Clave": usr[5],
                "FechaReg": usr[6],
                "Alta": usr[7],
            }

            return data

        if update:
            print(usrdata["usuario_original"])
            print(
                "Update Operador set IDPais=1, Usuario='{}', Nombres='{}', Apellidos='{}', Clave='{}', FechaReg='{}', Alta={} where Usuario = '{}';".format(
                    usrdata["usuario"],
                    usrdata["nombre"],
                    usrdata["apellido"],
                    usrdata["clave"],
                    usrdata["fecha"],
                    usrdata["alta"],
                    usrdata["usuario_original"],
                )
            )
            print("datos")
            self.execquery(
                "Update Operador set IDPais=1, Usuario='{}', Nombres='{}', Apellidos='{}', Clave='{}', FechaReg='{}', Alta={} where Usuario = '{}';".format(
                    usrdata["usuario"],
                    usrdata["nombre"],
                    usrdata["apellido"],
                    usrdata["clave"],
                    usrdata["fecha"],
                    usrdata["alta"],
                    usrdata["usuario_original"],
                )
            )

    def listar(self):
        return self.execquery(
            "select O.ID,P.Nombre,O.Usuario,O.Nombres,O.Apellidos,O.Clave,O.FechaReg, O.Alta \
            from Operador as O  \
                inner join Pais as P on P.ID = O.IDPais;"
        )

    def cantidad(self):
        return self.execquery("select count(*) from Operador")[0][0]

    def activos(self):
        return self.execquery("select count(*) from operador where Alta = 1")[0][0]

    def noactivos(self):
        return self.execquery("select count(*) from operador where Alta = 0")[0][0]

    def baja(self, usuario):
        return self.execquery(
            "Update Operador set Alta = 0 where Usuario = '{}'".format(usuario)
        )

    def alta(self, usuario):
        return self.execquery(
            "Update Operador set Alta = 1 where Usuario = '{}'".format(usuario)
        )

    def clave(self, usuario):
        return self.execquery(
            "select O.Clave from Operador as O where usuario = '{}'".format(usuario)
        )[0][0]

    def Id(self, usuario):
        return self.execquery(
            "select O.ID from Operador as O where usuario = '{}'".format(usuario)
        )[0][0]

    def ventas_por_año(self, usuario, anio):
        return self.execquery(
            "select count(V.Fecha) \
            from Ventas as V \
                inner join Operador as O on O.ID = V.IDOperador \
            where O.Usuario = '{}' and YEAR(V.Fecha) = '{}'".format(
                usuario, anio
            )
        )[0][0]


class Cliente(Database):
    def atributos(self, email):
        return self.execquery(
            "select C.IDPais, C.Nombres, C.Apellidos, C.Email, C.Sexo, C.CUIL, C.FechaNac, C.FechaReg \
            from Cliente as C \
            where C.Email = '{}';".format(
                email
            )
        )[0]

    def agregar(self, data):
        print(
            "insert into Cliente(IDPais,Apellidos,Nombres,Email,Sexo,CUIL,FechaNac,FechaReg) values (1,'{}','{}','{}','{}','{}',CAST(N'{}' AS Date),CAST(N'{}' AS Date));".format(
                data["apellido"],
                data["nombre"],
                data["email"],
                data["sexo"],
                data["cuil"],
                data["fechanac"],
                data["fechareg"],
            )
        )
        return self.execquery(
            "insert into Cliente(IDPais,Apellidos,Nombres,Email,Sexo,CUIL,FechaNac,FechaReg) values (1,'{}','{}','{}','{}','{}',CAST(N'{}' AS Date),CAST(N'{}' AS Date));".format(
                data["apellido"],
                data["nombre"],
                data["email"],
                data["sexo"],
                data["cuil"],
                data["fechanac"],
                data["fechareg"],
            )
        )

    def borrar(self, email):
        print("delete from Cliente where email = '{}'".format(email))
        return self.execquery("delete from Cliente where email = '{}'".format(email))

    def actualizar(self):
        pass

    def listar(self):
        return self.execquery(
            "select C.ID, P.Nombre, C.Apellidos, C.Nombres, C.Email, C.Sexo, C.CUIL, C.FechaNac, C.FechaReg \
                                from Cliente as C \
                                inner join Pais as P on P.ID = C.IDPais;"
        )

    def Id(self, cuil):
        return self.execquery(
            "select C.ID from Cliente as C where Cuil = '{}'".format(cuil)
        )[0][0]

    def consulta_ventas_por_sexo(self):
        return self.execquery(
            "select distinct C.Sexo, \
                ( \
                select count(V.ID) \
                from Ventas as V \
                where C.Sexo = 'M' \
            ) as [Sexo Masculino], \
                ( \
                select count(V.ID) \
                from Ventas as V \
                where C.Sexo = 'F' \
            ) as [Sexo Femenino] \
            from Cliente as C"
        )

    def edad_media_vista(self):
        return self.execquery("select * from VW_EdadMediaClientes")[0][0]

    def superan_media_vista(self):
        return self.execquery("select * from VW_ClientesQueSuperanEdadMedia")


class Producto(Database):
    def atributos(self, Id):
        return self.execquery(
            "select P.ID,P.Descripcion,P.Color,P.Nombre \
            from Producto as P where P.ID = '{}';".format(
                Id
            )
        )[0]

    def listar(self):
        return self.execquery("select * from Producto")

    def agregar(self, producto):
        return self.execquery(
            "exec dbo.SP_guardar_producto \
                  @Descripcion = '{}', \
                  @Color = '{}', \
                  @Precio = {}, \
                  @Stock = {}, \
                  @FechaReg = '2013-12-12'".format(
                producto["descripcion"],
                producto["color"],
                producto["precio"],
                producto["stock"],
            )
        )

    def borrar(self, producto):
        print(
            "exec dbp.SP_borrar_producto \
                    @Descripcion = '{}'".format(
                producto
            )
        )
        return self.execquery(
            "exec dbo.SP_borrar_producto \
                    @Descripcion = '{}'".format(
                producto
            )
        )

    def actualizar_stock(self, producto, cantidad):
        print(
            "Update Producto set Stock='{}' where Descripcion = '{}';".format(
                cantidad, producto
            )
        )

        return self.execquery(
            "Update Producto set Stock='{}' where Descripcion = '{}';".format(
                cantidad, producto
            )
        )

    def buscar(self, producto):
        return self.execquery(
            "select P.Descripcion,P.Color,P.Precio,P.Stock from Producto as P where Descripcion = '{}'".format(
                producto
            )
        )

    def Id(self, producto):
        return self.execquery(
            "select P.ID from Producto as P where Descripcion = '{}'".format(producto)
        )[0][0]

    def Precio(self, producto):
        return self.execquery(
            "select P.Precio from Producto as P where Descripcion = '{}'".format(
                producto
            )
        )[0][0]

    def agregar_stock(self, producto):
        print("update Producto set stock='{}' where Descripcion = '{}';")


class Stock(Database):
    def atributos(self, Id):
        return self.execquery(
            "select S.ID,S.IDProducto,S.Talle,S.Stock \
            from Stock as S where S.ID = '{}';".format(
                Id
            )
        )[0]

    def agregar(self, producto):
        print(producto)
        return self.execquery(
            "exec dbo.SP_guardar_producto \
                                    @Descripcion = '{}', @Color = '{}', @Precio = '{}', @Stock = {}, @FechaReg = '{}'".format(
                producto["descripcion"],
                producto["color"],
                producto["precio"],
                producto["stock"],
                producto["fechareg"],
            )
        )

    def borrar(self):
        pass

    def actualizar(self):
        pass


class Venta(Database):
    def atributos(self, Id):
        return self.execquery(
            "select S.ID,S.IDProducto,S.Talle,S.Stock \
            from Stock as S where S.ID = '{}';".format(
                Id
            )
        )[0]
        pass

    def agregar(self):
        pass

    def borrar(self):
        pass

    def actualizar(self):
        pass

    def procesar_ventas(
        self,
        total_de_productos,
        total_valor_venta,
        fecha_venta,
        operador_id,
        cliente_id,
    ):
        print(
            "insert into Ventas (CantidadTotalProductos, valorTotaldeVenta, Fecha, IDCliente, IDOperador) values ({},{},CAST(N'{}' AS Date),{},{})".format(
                total_de_productos,
                total_valor_venta,
                fecha_venta,
                cliente_id,
                operador_id,
            )
        )
        return self.execquery(
            "insert into Ventas (CantidadTotalProductos, valorTotaldeVenta, Fecha, IDCliente, IDOperador) values ({},{},CAST(N'{}' AS Date),{},{})".format(
                total_de_productos,
                total_valor_venta,
                fecha_venta,
                cliente_id,
                operador_id,
            )
        )

    def buscar(self, total_de_productos):
        return self.execquery(
            "select V.ID from Ventas as V where CantidadTotalProductos = {}".format(
                total_de_productos
            )
        )[0][0]

    def consulta_ventas_por_anio(self, anio):
        return self.execquery(
            "select count(V.Fecha) \
            from Ventas as V \
            where YEAR(V.Fecha) = '{}'".format(
                anio
            )
        )[0][0]


class Ventas_x_Productos(Database):
    def agregar(self, idventas, idproducto, cantidad_producto, precio_producto):
        return self.execquery(
            "insert into Ventas_x_Producto (IDVentas, IDProducto, CantidadProducto,PrecioProducto) values ({},{},{},{})".format(
                idventas, idproducto, cantidad_producto, precio_producto
            )
        )

    def cuantas_veces_se_vendio_un_producto(self, producto):
        return self.execquery(
            "select count(P.ID) \
                from Producto as P \
                inner join Ventas_x_Producto as VXP on VXP.IDProducto = P.ID \
            where P.Descripcion = '{}'".format(
                producto
            )
        )[0][0]


class Pais(Database):
    def lista(self):
        return self.execquery("select * from Pais")

    def agregar(self, pais):
        print("insert into Pais (Nombre) values ('{}')".format(pais))
        return self.execquery("insert into Pais (Nombre) values ('{}')".format(pais))

    def borrar(self, pais):
        print("delete from pais where Nombre = '{}'".format(pais))
        return self.execquery("delete from pais where Nombre = '{}'".format(pais))

    def actualizar(self):
        pass

    def buscar(self, pais):
        return self.execquery(
            "select P.Nombre from Pais as P where Nombre = '{}'".format(pais)
        )[0][0]

    def Id(self, pais):
        return self.execquery(
            "select P.ID from Pais as P where Nombre = '{}'".format(pais)
        )[0][0]

    def suma_total_por_pais(self):
        return self.execquery(
            "select P.Nombre, \
                ( \
                select sum(V.ValorTotaldeVenta) \
                from Operador as O \
                    inner join Ventas as V on V.IDOperador = O.ID \
                where P.ID = O.IDPais \
            ) as [Venta total por Pais] \
            from Pais as P"
        )

    def total_clientes_por_pais(self):
        return self.execquery(
            "select P.Nombre, \
                ( \
                    select count(C.ID) \
                from Cliente as C \
                where C.IDPais = P.ID \
                ) as [Cantidad de Clientes] \
                from Pais as P"
        )

