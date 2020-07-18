-- crear y Listar emails de clientes, con nombre y apellido.-

-- use sventaropa

-- --Creacion de vista
-- create view VW_ReporteDeOperadores
-- as
--     select O.Usuario, O.Nombres, O.Apellidos, O.Clave, P.Nombre as [Pais]
--     from Operador as O
--         inner join Pais as P on P.ID = O.IDPais

-- -- Drop de la vista
-- drop view VW_ReporteDeOperadores

-- -- Reporte de la vista
-- select *
-- from VW_ReporteDeOperadores