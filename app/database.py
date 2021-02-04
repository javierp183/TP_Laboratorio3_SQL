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
        self.cursor.execute("{}".format(query))
        try:
            return self.cursor.fetchall()
        except pyodbc.ProgrammingError as e:
            if "Previous SQL was not a query." in str(e):
                pass

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
            "select O.ID,O.IDPais,O.Usuario,O.Nombres,O.Apellidos,O.Clave \
            from Operador as O where usuario = '{}';".format(
                usuario
            )
        )[0]

    def agregar(self):

        pass

    def borrar(self):
        pass

    def actualizar(self):
        pass


class Cliente(Database):
    def atributos(self, email):
        return self.execquery(
            "select C.ID,C.IDPais,C.Apellidos,C.Nombres,C.Email,C.Sexo,C.FechaNac,C.Clave \
            from Cliente as C where C.Email = '{}';".format(
                email
            )
        )[0]

    def agregar(self):
        pass

    def borrar(self):
        pass

    def actualizar(self):
        pass


class Producto(Database):
    def atributos(self, Id):
        return self.execquery(
            "select P.ID,P.Descripcion,P.Color,P.Nombre \
            from Producto as P where P.ID = '{}';".format(
                Id
            )
        )[0]

    def agregar(self):
        pass

    def borrar(self):
        pass

    def actualizar(self):
        pass


class Stock(Database):
    def atributos(self, Id):
        return self.execquery(
            "select S.ID,S.IDProducto,S.Talle,S.Stock \
            from Stock as S where S.ID = '{}';".format(
                Id
            )
        )[0]

    def agregar(self):
        pass

    def borrar(self):
        pass

    def actualizar(self):
        pass


class Ventas(Database):
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


# def create_database():
#     server = "localhost\sqlexpress"
#     server = "myserver,port"
#     server = "tcp:localhost"
#     database = "master"
#     username = "{}".format(config["database"]["user"])
#     password = "{}".format(config["database"]["password"])
#     cnxn = pyodbc.connect(
#         "DRIVER={};SERVER=".format(config["database"]["driver"])
#         + server
#         + ";DATABASE="
#         + database
#         + ";UID="
#         + username
#         + ";PWD="
#         + password,
#         autocommit=True,
#     )
#     cursor = cnxn.cursor()

#     # Create database
#     try:
#         cursor.execute("create database {}".format(config["database"]["nombre"]))
#         print("la base de datos a sido creada")
#     except:
#         print("La base de datos ya existe!")


# create_database()


# def connection():
#     engine = create_engine(
#         "mssql+pyodbc://sa:h51kolv3!@localhost:1433/{}?driver=ODBC+Driver+17+for+SQL+Server".format(
#             config["database"]["nombre"]
#         ),
#         fast_executemany=True,
#     )

#     return engine


# class Operador(Base):
#     __tablename__ = "operador"
#     id = Column(Integer, primary_key=True)
#     nombre = Column(String(50))
#     apellido = Column(String(50))
#     usuario = Column(String(10))
#     clave = Column(String(10))

# class Mislibros(Base):
#     __tablename__ = "mislibros"
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     primary_author = Column(String)


# Session = sessionmaker(bind=engine)
# session = Session()
# result = session.query(Mislibros).all()

# print(result)


# metadata = MetaData()

# mybooks = Table(
#     "mislibros",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("title", String),
#     Column("primary_author", String),
# )


# metadata.create_all(engine)


# import pyodbc

# Some other example server values are
# server = "localhost\sqlexpress"  # for a named instance
# server = "myserver,port"  # to specify an alternate port
# server = "tcp:localhost"
# database = "master"
# username = "sa"
# password = "h51kolv3!"
# cnxn = pyodbc.connect(
#     "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
#     + server
#     + ";DATABASE="
#     + database
#     + ";UID="
#     + username
#     + ";PWD="
#     + password,
#     autocommit=True,
# )
# cursor = cnxn.cursor()

# # Sample select query
# cursor.execute("create database sventaropa")
# row = cursor.fetchone()
# while row:
#     print(row[0])
#     row = cursor.fetchone()


# import urllib

# params = urllib.parse.quote_plus(
#     "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=Bookworm;UID=sa;PWD=h51kolv3!"
# )