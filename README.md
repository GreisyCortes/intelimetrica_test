Proyecto Django CRUD
Descripción
Este proyecto es una aplicación web de Django que implementa las operaciones básicas de CRUD (Crear, Leer, Actualizar, Eliminar) para la gestión de un Restaurante.

Requisitos
Para ejecutar este proyecto, necesitas tener instalados los siguientes programas:

Python 3.12
pip (gestor de paquetes de Python)
virtualenv (opcional pero recomendado)
Instalación
Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

Crea y activa un entorno virtual (opcional pero recomendado):

sh
Copy code
python -m venv env
source env/bin/activate   # En Windows usa `env\Scripts\activate`
Instala las dependencias:

sh
Copy code
pip install -r requirements.txt

Realiza las migraciones de la base de datos:

sh
Copy code
python manage.py makemigrations
python manage.py migrate
Crea un superusuario para acceder al panel de administración:

sh
Copy code
python manage.py createsuperuser
Ejecuta el servidor de desarrollo:

sh
Copy code
python manage.py runserver
Accede a la aplicación:
Abre tu navegador y ve a http://127.0.0.1:8000.


Uso
Una vez que el servidor esté en ejecución, puedes acceder a las siguientes URLs:

http://127.0.0.1:8000/admin/: Panel de administración de Django.
http://127.0.0.1:8000/api/all/: Obtiene todos los restaurantes.
http://127.0.0.1:8000/api/create/: Creas un nuevo restaurante, el id no es requerido.
http://127.0.0.1:8000/api/update/: Actualizas un restaurante, el id es requerido y todos los datos igual.
http://127.0.0.1:8000/api/delete/: Eliminas un restaurante dado el id.
http://127.0.0.1:8000/restaurants/statistics?latitude=19.4400570537131&longitude=-99.1270470974249&radius=0.005: Obtienes el conteo de los restaurantes, promedio y desviación estandar
