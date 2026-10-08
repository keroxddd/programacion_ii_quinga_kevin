Programación II - Control de Proyectos y Subproyectos

📌 Descripción

Este proyecto corresponde a la materia Programación II y tiene como objetivo desarrollar una estructura para el control y seguimiento de proyectos y subproyectos, utilizando tecnologías como Python, Django y Odoo.

El sistema permitirá organizar proyectos, subproyectos, responsables, estados, fechas y tareas, manteniendo una estructura ordenada y preparada para trabajar con Git y GitHub.

🎯 Objetivo general

Desarrollar una aplicación para administrar y controlar proyectos y subproyectos, aplicando conceptos de programación, desarrollo web, bases de datos y sistemas empresariales.

🛠️ Tecnologías utilizadas

Python - Lenguaje principal de programación.

Django - Framework para el desarrollo de la aplicación web.

Odoo - Plataforma empresarial para la gestión e integración de módulos.

Git - Control de versiones.

GitHub - Repositorio remoto del proyecto.

SQLite - Base de datos para el desarrollo inicial.

📁 Estructura del proyecto

programacion_ii_quinga_kevin/ │ ├── .gitignore ├── README.md ├── requirements.txt │ ├── python/ │ ├── main.py │ └── models.py │ ├── django_app/ │ ├── manage.py │ │ │ ├── config/ │ │ ├── init.py │ │ ├── settings.py │ │ ├── urls.py │ │ └── wsgi.py │ │ │ └── proyectos/ │ ├── init.py │ ├── admin.py │ ├── apps.py │ ├── models.py │ ├── views.py │ ├── urls.py │ └── migrations/ │ ├── odoo_module/ │ ├── init.py │ ├── manifest.py │ ├── models/ │ ├── views/ │ ├── security/ │ └── data/ │ ├── tests/ ├── docs/ ├── scripts/ └── data/

🐍 Módulo Python

La carpeta python/ contiene la lógica inicial del proyecto.

python/ ├── main.py └── models.py

En esta sección se pueden realizar pruebas de lógica, clases y estructuras de datos antes de integrarlas con Django u Odoo.

🌐 Aplicación Django

La carpeta django_app/ contiene la aplicación web desarrollada con Django.

Funcionalidades previstas

Crear proyectos.

Registrar subproyectos.

Asignar responsables.

Definir fechas de inicio y finalización.

Controlar estados.

Consultar proyectos y subproyectos.

Administrar información desde Django Admin.

Modelo principal

Proyecto

Nombre

Descripción

Responsable

Fecha de inicio

Fecha de finalización

Estado

Subproyecto

Proyecto relacionado

Nombre

Descripción

Estado

🟣 Módulo Odoo

La carpeta odoo_module/ está destinada al desarrollo del módulo personalizado para Odoo.

odoo_module/ ├── init.py ├── manifest.py ├── models/ ├── views/ ├── security/ └── data/

El módulo permitirá posteriormente integrar la gestión de proyectos y subproyectos con las funcionalidades empresariales de Odoo.

🗂️ Carpetas adicionales

tests/

Contiene las pruebas del proyecto para comprobar que las funcionalidades desarrolladas funcionan correctamente.

docs/

Contiene la documentación técnica y académica del proyecto.

scripts/

Contiene scripts auxiliares para automatizar tareas del proyecto.

data/

Contiene datos de prueba o información utilizada durante el desarrollo.

🔐 Git y GitHub

El proyecto utiliza Git para controlar las diferentes versiones del código.

Comandos principales:

git status git add . git commit -m "Descripción del cambio" git push

El archivo .gitignore evita subir archivos innecesarios, temporales o privados al repositorio.

Entre los archivos ignorados se encuentran:

Entornos virtuales.

Caché de Python.

Base de datos SQLite.

Archivos .env.

Archivos temporales.

Configuraciones de editores.

Archivos generados automáticamente.

⚙️ Instalación

Clonar el repositorio
git clone git@github.com:keroxddd/programacion_ii_quinga_kevin.git

Entrar al proyecto
cd programacion_ii_quinga_kevin

Crear un entorno virtual
python3 -m venv .venv

Activar el entorno virtual
En Linux:

source .venv/bin/activate

Instalar las dependencias
pip install -r requirements.txt

▶️ Ejecución de Django

Entrar a la aplicación:

cd django_app

Ejecutar el servidor:

python manage.py runserver

Después se puede acceder al servidor local desde:

http://127.0.0.1:8000/

👨‍💻 Autor

Kevin Quinga

Materia: Programación II

Proyecto académico para el aprendizaje y aplicación de:

Python

Django

Odoo

Git

GitHub

📚 Estado del proyecto

En desarrollo 🚧

El proyecto se encuentra en proceso de construcción. Se irán agregando nuevas funcionalidades, modelos, vistas, pruebas e integración con Odoo durante el desarrollo de la materia.

📄 Licencia

Proyecto académico desarrollado para fines educativos.