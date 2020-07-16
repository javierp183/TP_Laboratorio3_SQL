use sventaropa
insert into Operador
    (IDPais,Usuario, Nombres, Apellidos, Clave)
VALUES
    (1, 'javier', 'Javier', 'Pereyra', '0123456789012345678901234567890123456789')
insert into Operador
    (IDPais,Usuario, Nombres, Apellidos, Clave)
VALUES
    (1, 'daniel', 'Daniel', 'Pereyra', '0123456789012345678901234567890123456789')
insert into Operador
    (IDPais,Usuario, Nombres, Apellidos, Clave)
VALUES
    (1, 'victor', 'Victor', 'Pereyra', '0123456789012345678901234567890123456789')
INSERT into Cliente
    (IDPais, Apellidos, Nombres, Email, Sexo, CUIL, FechaNac)
VALUES
    (1, 'Dorrego', 'Perez', 'dorrego@gmail.com', 'M', '20333', CAST(N'1986-10-02' AS Date))
INSERT into Cliente
    (IDPais, Apellidos, Nombres, Email, Sexo, CUIL, FechaNac)
VALUES
    (1, 'Sarmiento', 'Torres', 'sarmiento@gmail.com', 'M', '21333', CAST(N'1990-10-02' AS Date))
INSERT into Cliente
    (IDPais, Apellidos, Nombres, Email, Sexo, CUIL, FechaNac)
VALUES
    (1, 'Santiago', 'Succatti', 'santiago@gmail.com', 'M', '22333', CAST(N'2000-10-02' AS Date))
insert into Producto
    (Descripcion,Color,Precio, Stock)
VALUES
    ('pantalon', 'gris', 1000, 10)
insert into Producto
    (Descripcion,Color,Precio, Stock)
VALUES
    ('camisa', 'blanco', 2000, 10)
insert into Producto
    (Descripcion,Color,Precio, Stock)
VALUES
    ('corvata', 'azul', 3000, 10)
insert into Producto
    (Descripcion,Color,Precio, Stock)
VALUES
    ('campera', 'rojo', 4000, 10)
insert into Pais
    (Nombre)
VALUES
    ('Argentina')
insert into Pais
    (Nombre)
VALUES
    ('Uruguay')
insert into Pais
    (Nombre)
VALUES
    ('Brazil')
insert into Pais
    (Nombre)
VALUES
    ('Chile')
insert into Pais
    (Nombre)
VALUES
    ('Paraguay')
insert into Pais
    (Nombre)
VALUES
    ('Bolivia')
insert into Ventas
    (CantidadTotalProductos,ValorTotaldeVenta,Fecha,IDCliente,IDOperador)
VALUES
    (1, 1000, CAST(N'1986-10-02' AS Date), 4, 5)
insert into Ventas
    (CantidadTotalProductos,ValorTotaldeVenta,Fecha,IDCliente,IDOperador)
VALUES
    (2, 2000, CAST(N'1987-10-02' AS Date), 5, 5)
INSERT into Ventas_x_Producto
    (IDVentas,IDProducto,CantidadProducto,PrecioProducto)
VALUES
    (1, 1, 1, 1000)
INSERT into Ventas_x_Producto
    (IDVentas,IDProducto,CantidadProducto,PrecioProducto)
VALUES
    (2, 1, 2, 1000)