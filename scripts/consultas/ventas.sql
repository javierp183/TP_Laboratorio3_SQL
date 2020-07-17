-- Script para contar cantidad de ventas
-- select Count(*)
-- from ventas;

select *
from ventas


-- Script sumar el total de todas las ventas
-- select sum(V.ValorTotaldeVenta)
-- from Ventas as V

-- Script para contar la cantidad de ventas por Operador
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

-- Script para contar cantidad de ventas por año por Operador
-- select count(V.Fecha)
-- from Ventas as V
--     inner join Operador as O on O.ID = V.IDOperador
-- where O.Usuario = 'javier' and YEAR(V.Fecha) = '1986'