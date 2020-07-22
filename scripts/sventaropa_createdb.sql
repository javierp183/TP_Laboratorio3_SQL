-- remvoe database
drop database sventaropa
-- create database
create database sventaropa
-- Use database
use sventaropa
Create Table Operador
(
    ID bigint not null identity (1, 1),
    IDPais bigint not null,
    Usuario varchar(100) not null UNIQUE,
    Nombres varchar(100) not null,
    Apellidos varchar(100) not null,
    Clave varchar(100) not null check (len(Clave) >= 32),
    FechaReg date null,
    Alta bit not null
)
Create Table Cliente
(
    ID bigint not null identity (1, 1),
    IDPais bigint not null,
    Apellidos varchar(100) not null,
    Nombres varchar(100) not null,
    Email varchar(100) not null UNIQUE,
    Sexo char null,
    CUIL bigint not null check (len(CUIL) >= 11),
    FechaNac date null,
    FechaReg date null
)
Create Table Producto
(
    ID bigint not null identity (1, 1),
    Descripcion varchar(100) not null,
    Color varchar(100) not null,
    Precio money not null check (Precio >= 0),
    Stock integer not null check (Stock >= 0),
    FechaReg date null
)
CREATE TABLE Pais
(
    ID bigint not null identity (1, 1),
    Nombre varchar(100) not null UNIQUE
)
create table Ventas
(
    ID bigint not null identity(1, 1),
    CantidadTotalProductos integer not null,
    ValorTotaldeVenta money not null,
    Fecha date null,
    IDCliente bigint not null,
    IDOperador bigint not null
)
alter table Producto 
add CONSTRAINT PK_Producto PRIMARY KEY (ID)
alter table Ventas
add CONSTRAINT PK_Ventas PRIMARY KEY (ID)
create table Ventas_x_Producto
(
    IDVentas bigint not null FOREIGN KEY REFERENCES Ventas(ID),
    IDProducto bigint not null FOREIGN KEY REFERENCES Producto(ID),
    CantidadProducto integer not null,
    PrecioProducto money not null,
    PRIMARY KEY (IDVentas, IDProducto)
)
/* Restricciones */
-- primary key
alter table Operador
Add CONSTRAINT PK_Operador Primary key (ID)
alter table Cliente
add CONSTRAINT PK_Cliente PRIMARY KEY (ID)
alter table Pais
add CONSTRAINT PK_Pais PRIMARY KEY (ID)
-- Foreign key Operador
alter table Operador
add CONSTRAINT FKOperador_IDPais FOREIGN KEY (IDPais) REFERENCES Pais (ID)
-- Foreign key Cliente
alter table Cliente
add CONSTRAINT FKCliente_IDPais FOREIGN KEY (IDPais) REFERENCES Pais (ID)
-- Foreign key Ventas
alter table Ventas
add CONSTRAINT FK_IDCliente FOREIGN KEY (IDCliente) REFERENCES Cliente (ID)
alter table Ventas
add CONSTRAINT FK_IDOperador FOREIGN KEY (IDOperador) REFERENCES Operador (ID)