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

-- crear y listar clientes con su nombre y apellido y CUIL.-
-- create view VW_ReporteDeClientes
-- as
--     select C.Nombres, C.Apellidos, C.Email, C.Sexo, C.CUIL
--     from Cliente as C

-- drop view VW_ReporteDeClientes

-- select *
-- from VW_ReporteDeClientes

-- -- View para listar la edad media de los clientes

-- create view VW_EdadMediaClientes
-- as
--     select avg(cast(datediff(day,C.FechaNac,getdate())/365.25 as Int)) as [Media de Edad]
--     from Cliente as C

-- drop view VW_EdadMediaClientes

-- select *
-- from VW_EdadMediaClientes

-- -- View para listar los clientes que superen la edad media
-- Dependencia con la vista VW_EdadMediaClientes
-- create view VW_ClientesQueSuperanEdadMedia
-- as
--     select C.nombres, C.Apellidos, C.Email
--     from Cliente as C
--     where cast(datediff(day,C.FechaNac,getdate())/365.25 as Int) > (
--         select *
--     from VW_EdadMediaClientes
--     )

-- Listar los Clientes que superan la edad Media
-- select *
-- from VW_ClientesQueSuperanEdadMedia

-- Reporte de usuarios Operadores que vendieron pantalones
-- create view VW_PantalonesPorOperador
-- as
--     select P.Descripcion, O.Usuario
--     from Ventas_x_Producto as VXP
--         inner join Producto as P on P.ID = VXP.IDProducto
--         inner join Ventas as V on V.ID = VXP.IDVentas
--         inner join Operador as O on O.ID = V.IDOperador
--     where P.Descripcion = 'pantalon'

-- drop view VW_PantalonesPorOperador

-- select *
-- from VW_PantalonesPorOperador

-- Reporte de usuarios de que ID son Clientes Femeninos y que otros Masculinos: todo
-- create view VW_Reporte_Generos
-- as
--     SELECT C.Nombres, C.Apellidos,
--         case C.Sexo
--     when 'M' then 'Masculino'
--     when 'F' then 'Femenino'
-- end as Genero
--     from Cliente as C


-- drop view VW_Reporte_Generos
-- select *
-- from VW_Reporte_Generos


