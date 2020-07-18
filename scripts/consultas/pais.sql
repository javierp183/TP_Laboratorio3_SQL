-- Listar cantidad de clientes por cada País.- ( subconsulta ):
-- select P.Nombre,
--     (
--         select count(C.ID)
--     from Cliente as C
--     where C.IDPais = P.ID
-- ) as [Cantidad de Clientes]
-- from Pais as P


-- Listar suma total vendida por cada País.- ( subconsulta ):
-- select P.Nombre,
--     (
--     select sum(V.ValorTotaldeVenta)
--     from Operador as O
--         inner join Ventas as V on V.IDOperador = O.ID
--     where P.ID = O.IDPais
-- ) as [Venta total por Pais]
-- from Pais as P