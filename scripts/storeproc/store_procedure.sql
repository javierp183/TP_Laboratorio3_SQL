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
--     where P.Descripcion = @Descripcion
-- end

-- exec SP_cantidad_stock_producto 'pantalon'

-- Store procedure para obtener datos de un Operador
-- create PROCEDURE SP_datos_operador(
--     @Username varchar(100)
-- )
-- as
-- BEGIN
--     select O.Usuario, O.Nombres, O.Apellidos, O.Clave
--     from Operador as O
--     where O.Usuario = @Username
-- END

-- drop PROCEDURE SP_datos_operador

-- exec SP_datos_operador 'javier'

-- Store procedure para obtener la fecha de registro de un Cliente
-- create PROCEDURE SP_fecha_registro_cliente(
--     @CUIL
-- )
-- as
-- BEGIN
--     select C.FechaReg
--     from Cliente as C
--     where C.CUIL = @CUIL
-- END

-- drop procedure SP_fecha_registro_cliente

-- exec SP_fecha_registro_cliente 20


-- Store procedure para ingresar un nuevo Operador ( todo )

-- Store procedure para ingresar un nuevo Cliente ( todo )




