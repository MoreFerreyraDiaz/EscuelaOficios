# Sobre el proyecto

Este proyecto consiste en un sitio web basada en una escuela de oficios REAL con un formulario de inscripción hecho con HTML, CSS y JavaScript, conectado a un backend en Python utilizando Flask que guarda la información en una base de datos SQL Server.

# Componentes

*FRONTEND*

El inicio del sitio web contiene una barra de navegación que te ayuda a acceder rápidamente a la sección deseada, información de cada curso a los que se puede inscribir, el formulario para completar tus datos, ubicación y video adjuntos. Todas las imágenes fueron generadas con IA (IStock).

*BACKEND*

En Python usé Flask para poder crear la base de datos y transmitir los datos desde el formulario HTML al SQL Server, guardándose estos en la tabla previamente creada.

# Requisitos

Clonar el repositorio para acceder a los archivos: 'https://github.com/MoreFerreyraDiaz/EscuelaOficios.git'

Para poder ejecutar los archivos Python es necesario escribir la siguiente línea en la terminal de VSCode para instalar ciertas dependencias en caso de no tenerlas:

> pip install -r requirements.txt

Configurar las variables de entorno según los datos de su PC.

DB_SERVER=localhost
DB_NAME=nombre_base_datos
DB_USER=usuario
DB_PASSWORD=contraseña

Ya puede disfrutar del proyecto.

# Carpetas

img: imágenes vinculadas al sitio web.
python: todos los archivos de python (models, routes, git-pull, etc).
sql: archivos con códigos para SQL Server.
statics: CSS y JavaScript.
templates: HTML (main archive).
