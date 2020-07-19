--- Store procedure file
-- use sventaropa
-- Datos (CUIL,EMAIL) de Cliente por Numero de CUIL
-- create procedure SP_Cliente_CUIL(
--     @CUIL int
-- )
-- as
-- BEGIN
--     select C.Email, C.CUIL
--     from Cliente as C
--     where C.CUIL = CUIL
-- end

-- exec SP_Cliente_CUIL 20333

-- Store proceduce para obtener el dato de cantidad de stock por 
-- nombre de producto 
-- create PROCEDURE SP_cantidad_stock_producto(
--     @Descripcion varchar(100)
-- )
-- AS
-- BEGIN
--     select P.Stock
--     from Producto as P
--     where P.Descripcion = Descripcion
-- end

-- exec SP_cantidad_stock_producto 'pantalon'
