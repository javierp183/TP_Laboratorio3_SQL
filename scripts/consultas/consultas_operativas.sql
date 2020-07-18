-- Consulta para obtener datos de un usuario para la aplicacion
-- apartir de su UserID
-- select O.Usuario, O.Nombres, O.Apellidos, O.Clave
-- from Operador as O
--     inner join Pais as P on P.ID = O.IDPais
-- where O.Usuario = 'javier'

-- Consulta para obtener datos de un cliente para la aplicacion
-- apartir de numero de CUIL - numero unico e identificatorio
-- por número de CUIL.
-- select C.Nombres, C.Apellidos, C.Email, C.Sexo, C.FechaNac, C.CUIL
-- from Cliente as C
-- where C.CUIL = '20333'

-- Consulta para obtener datos de stock por nombre de producto 
-- Descripcion
-- select P.Descripcion, P.Color, P.Precio, P.Stock
-- from Producto as P
-- where P.Descripcion = 'pantalon'