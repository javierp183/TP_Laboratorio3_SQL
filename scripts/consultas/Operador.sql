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