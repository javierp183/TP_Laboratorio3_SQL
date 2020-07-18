-- Script para listar la edad y nombre  y apellido de los clientes
select C.Nombres, C.Apellidos, cast(datediff(day,C.FechaNac,getdate())/365.25 as Int) as Edad
from Cliente as C

-- Script para listar la edad media de los clientes
select avg(cast(datediff(day,C.FechaNac,getdate())/365.25 as Int)) as [Media de Edad]
from Cliente as C