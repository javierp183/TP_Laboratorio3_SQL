-- Cantidad total de ventas y Cantidad vendido de producto por operador  ( subconsultas )
-- select O.Nombres, (
--     select sum(V.CantidadTotalProductos)
--     from Ventas as V
--     where O.ID = V.IDOperador
-- ) as [Total Cantidad Ventas],
--     (
--     select sum(V.ValorTotaldeVenta)
--     from Ventas as V
--     where O.ID = V.IDOperador
-- ) as [Total de Ventas]
-- from Operador as O

-- Media de ventas por Operador ( subconsulta ):
-- select O.Usuario,
--     (
--     select avg(V.ValorTotaldeVenta)
--     from Ventas as V
--     where O.ID = V.IDOperador
-- )
-- from Operador as O

-- Operador con mayor cantidad de ventas: todo
-- select O.Nombres, V.CantidadTotalProductos
-- from Operador as O
--     inner join Ventas as V on V.IDOperador = O.ID

-- Operadores activos
-- select *
-- from operador
-- where Alta = 1

-- Listar Operadores
select *
from operador

select O.ID, O.IDPais, O.Usuario, O.Nombres, O.Apellidos, O.Clave, convert(varchar,O.FechaReg)
from Operador as O
where usuario = 'javier';