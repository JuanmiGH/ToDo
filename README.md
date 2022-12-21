#######################
# To-Do APP en Python #
#######################

Este fue mi primer proyecto medianamente serio hecho en Python tras terminar mi curso.
El objetivo era poner a prueba lo aprendido, sobre todo en el tema de sesiones persistentes de usuario y comunicación con
Base de Datos. La aplicación no hace el CRUD completo en este estado. Se le podría agregar el borrado en un futuro así como
una zona de usuario donde se pudiera modificar ciertos aspectos del perfil del usuario, pero no era ese el objetivo de este
ejercicio por lo que no está añadido en esta versión de la aplicación.

Para hacer funcionar el proyecto hay que crear una base de datos (Yo utilicé una DB SQL) cuyos datos configuraremos en el archivo:
modules/condb.py

Dentro de la DB necesitaremos crear dos tablas: Una para los usuarios y otra para las tareas.

Para los uuarios:
CREATE TABLE usr(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    mail VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    img LONGTEXT NULL
);

Para las tareas:
CREATE TABLE tasks(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    propietario VARCHAR(255) NOT NULL,
    estado VARCHAR(10) NOT NULL,
    t_estimado VARCHAR(10) NULL,
    deadline VARCHAR(255) NULL,
    fdcreacion VARCHAR(255) NOT NULL,
    fdcierre VARCHAR(255) NULL,
    texto LONGTEXT NULL,
    titulo VARCHAR(255) NOT NULL,
);

Respecto a las tareas, si estas están en fecha todavía respecto a su deadline, aparecerán en gris. Si le quedan 10 días o menos
aparecerán en amarillo y si hoy es su deadline o éste ya ha pasado, aparecerán en rojo.
