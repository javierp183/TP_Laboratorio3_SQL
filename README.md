# TP_Laboratorio3_SQL

Trabajo Practico Laboratorio 3:

Tech:
 - MSSQL Server 2017
 - Docker
 - Ubuntu Linux 20.04
 - Visual Studio Code

 Estructura de archivos y directorios:

 - /TP_Laboratorio3_SQL (Main) - dir:
 - sventaropa_createdb.sql # Creacion de base de datos y sus relaciones.-
 - precarga.sql # Carga de datos a la base de datos

 - /consultas ( se resguardan la mayoria de las consultas ) - dir:
 - clientes.sql # Consultas relacionadas a clientes.
 - consutlas_operativas.sql # Consultas en general para una aplicación.
 - Operador.sql # Consultas relacionadas a los Oper adores de una aplicación.
 - Ventas.sql # Consultas relacionadas a las ventas de la aplicacion.

 - /DER ( estructura de la base de datos )
 - DER.png # Image file.

 - /inserts_y_carga
 - clientes_insert.sql
 - operador_insert.sql
 - pais_insert.sql
 - producto_insert.sql
 - ventas_x_producto_insert.sql

 - /storeproc ( Store procedure )
 - store_procedure.sql 
 
 - /vistas
 - vistas.sql


 # Orden de Inicialización de base de datos

 - 1° "sventaropa_createdb.sql".-
 - 2° "precarga.sql".-
 - 3° se pueden utilizas las lineas de "consultas","inserts_y_carga","storeproc" y "vistas".
