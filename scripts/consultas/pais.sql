-- Listar cantidad de clientes por cada País.- ( subconsulta ):
select P.Nombre,
    (
        select count(C.ID)
    from Cliente as C
    where C.IDPais = P.ID
) as [Cantidad de Clientes]
from Pais as P


-- Listar suma total vendida por cada País.- ( subconsulta ): TODO