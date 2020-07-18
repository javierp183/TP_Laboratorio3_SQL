-- Script para contar cantidad de ventas
-- select Count(*)
-- from ventas;

-- Script sumar el total de todas las ventas
-- select sum(V.ValorTotaldeVenta)
-- from Ventas as V

-- Script para contar la cantidad de ventas para un Operador
-- select count(O.Usuario)
-- from ventas as V
--     inner join Operador as O on O.ID = V.IDOperador
-- where O.Usuario = 'javier'

-- Script para sumar la cantidad de ventas por Operador de Productos
-- select sum(V.cantidadTotalProductos)
-- from ventas as V
--     inner join Operador as O on O.ID = V.IDOperador
-- where O.Usuario = 'javier'

-- Script para contar la cantidad de ventas de una fecha
-- select V.Fecha
-- from Ventas as V
-- where V.Fecha = '1986-10-02'

-- Script para contar la cantidad de ventas de un año
-- select count(V.Fecha)
-- from Ventas as V
-- where YEAR(V.Fecha) = '1986'

-- Script para contar cantidad de ventas por año para un Operador
-- select count(V.Fecha)
-- from Ventas as V
--     inner join Operador as O on O.ID = V.IDOperador
-- where O.Usuario = 'javier' and YEAR(V.Fecha) = '1986'

-- script para sumar el total de ventas por año para un Operador
-- select sum(V.ValorTotaldeVenta)
-- from Ventas as V
--     inner join Operador as O on O.ID = V.IDOperador
-- where O.Usuario = 'javier' and YEAR(V.Fecha) = '1986'

-- Script para sumar el total de ventas a un Cliente
-- select Count(V.IDCliente)
-- from Ventas as V
--     inner join Cliente as C on C.ID = V.IDCliente
-- where C.CUIL = '20333'

-- Script para contar el total de ventas por nombre de un Pais
-- select count(V.ID)
-- from Ventas as V
--     inner join Cliente as C on C.ID = V.IDCliente
--     inner join Pais as P on P.ID = C.IDPais
-- where P.Nombre = 'Argentina'

-- Script para contar el total de productos a un cliente.
-- select sum(V.cantidadTotalProductos)
-- from Ventas as V
--     inner join Cliente as C on C.ID = V.IDCliente
-- where C.CUIL = '20333'


-- Cantidad de ventas por cliente por sexo ( M: Masculino, F: Femenino ).- ( subconsulta )
-- select distinct C.Sexo,
--     (
--     select count(V.ID)
--     from Ventas as V
--     where C.Sexo = 'M'
-- ) as [Sexo Masculino],
--     (
--     select count(V.ID)
--     from Ventas as V
--     where C.Sexo = 'F'
-- ) as [Sexo Femenino]
-- from Cliente as C