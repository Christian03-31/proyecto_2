LINK de GITHUB:

https://github.com/Christian03-31/proyecto_2.git

Misael Ancan
Christian Díaz


requerimientos

pagina web para veterinaria donde podamos atender solo a perros y gatos con previa hora tomada

Objetivos:
1.- front fachero.
2.- parte para tomar horas con nombre de tutor, nombre del animal, perro o gato, edad.
3.- cuenta para trabajadores.
4.- front para trabajadores.
5.- manejo de horas. si es que podemos.

La toma de requerimientos anterior fue la idea principal que tuvimos para hacer la pagina.
Se realizaron en la carpeta templates tenemos las paginas principales que se puede visitar.
Se creo login con verificacion para entrar a los modulos. 
Se le dio style a las paginas con css por pagina que se encuentra en la carpeta static. 
Se generaron unas tablas en base de datos para almacenar los datos de los usuarios, como lo son los usuarios y contraseñas. Tambien se genero una base de datos para almacenar las citas que tomen los pacientes
Se creo una API donde se puede aplicar la funcion get y post a la base de datos.
Adicionalmente se uso una api de maps para simular la ubicacion en el mapa de la vererinaria, se configuro con la direccion de la sede SSUR de INACAP.

Para poder utilizar la API instalamos la siguiente libreria
```bash
py -m pip install djangorestframework
```

A continuacion dejamos Usuarios y Contraseña para los login.
Usuarios y contraseñas:

Trabajador: 
misael
asdasdqwe

Cliente:
roberto
1234asdfqwe

Administrador.
Misaaaa
123456788
