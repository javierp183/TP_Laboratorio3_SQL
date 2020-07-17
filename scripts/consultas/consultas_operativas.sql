-- Consulta para obtener datos de un usuario para la aplicacion.
-- select O.Usuario, O.Nombres, O.Apellidos, O.Clave
-- from Operador as O
--     inner join Pais as P on P.ID = O.IDPais
-- where O.Usuario = 'javier'

-- Consulta para obtener datos de un cliente para la aplicacion
-- por número de CUIL.
-- select C.Nombres, C.Apellidos, C.Email, C.Sexo, C.FechaNac, C.CUIL
-- from Cliente as C
-- where C.CUIL = '20333'

-- Consulta para obtener datos de stock por descripcion
-- select P.Descripcion, P.Color, P.Precio, P.Stock
-- from Producto as P
-- where P.Descripcion = 'pantalon'