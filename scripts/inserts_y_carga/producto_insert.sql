-- Script de inserción de Producto.
-- Descripción: nombre y descripcion del producto
-- Color: Color del producto
-- Precio: Precio del producto
-- Stock: Cantidad de productos
-- FechaReg: Fecha de registro de producto
insert into Producto
    (Descripcion,Color,Precio, Stock, FechaReg)
VALUES
    ('pantalon', 'gris', 1000, 10, CAST(N'2020-06-19' AS Date))