-- Script de inserción de Cliente.
-- Descripción:
-- IDPais : Corresponde al ID del País que se obtiene de la tabla país
-- Nombres: Nombre del Operador
-- Apellido: Apellido del Operador
-- Email: Email de contacto
-- Sexo: M -> Masculino , F -> Femenino
-- CUIL: Numero de CUIL
-- FechaNac: Fecha de nacimiento del cliente
-- FechaReg: Fecha de registro del usuario.
INSERT into Cliente
    (IDPais, Apellidos, Nombres, Email, Sexo, CUIL, FechaNac, FechaReg)
VALUES
    (1, 'Dorrego', 'Perez', 'dorrego@gmail.com', 'M', '20111119558', CAST(N'1986-10-02' AS Date), CAST(N'2020-06-19' AS Date))