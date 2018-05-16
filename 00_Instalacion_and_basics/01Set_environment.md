# PARA INSTALAR DJANGO 

## PIP
- [Documentacion de pip](https://pip.pypa.io/en/stable/installing/#using-linux-package-managers)
    ```console
    $ python get-pip.py 
	```
- Es el sistema de gestion de paquetes en python
- NOTA : PARA USAR pip con python3.x su usa **PIP3**
- Para conocer pip de manera mas general [documentacion](https://pip.pypa.io/en/stable/installing/)
## Virtualenv
- [documentacion](https://virtualenv.pypa.io/en/stable/)
- [guia de python](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
- Nos permite crear ambientes de desarrollo en python el cual maneja paquetes de manera aislada al resto.
- Instalacion:
    ```console
    $ pip install virtualenv

    // ejemplo para python3 en especifico
    // porque podria variar por la version actual de python que maneje el SO
    $ pip3 install virtualenv
    ```
- Crear y activar un ambiente virtual:
    ```console
    $ virtualenv -p python3 <nombre-del-ambiente>
    // de forma general virtualenv [OPCIONES] Env_directory
    $ source <nombre-del-ambiente>/bin/activate //para linux
    ```
- Para desactivar el ambiente virtual:
    ```console
    $ deactivate
    ```
- Para ver los modulos que se tiene actualmente en el ambiente virtual se ejecuto lo siguente
    ```console
    $ pip freeze
    ```

## VirtualEnvWrapper
- Para que sirve? para potenciar el virtualenv con unas extensiones compiladas de paquetes de python
- Instalacion
    ```console
    $ sudo pip install virtualenvwrapper
    //Una vez instalado, debemos editar el archivo ~/.bashrc (o ~/.zshrc si usa zsh) y agregar lo siguiente al final el archivo sin los $:
    $ export WORKON_HOME=~/.virtualenvs
    $ source /usr/local/bin/virtualenvwrapper.sh
```
- Para crear un virtualenv con virtualenvwrapper usamos este comando
    ```console
    mkvirtualenv --python=direccion donde esta python  <nombre>
    ```

## Para instalar Django2.0
- Instalar django -> [Documentacion](https://docs.djangoproject.com/en/2.0/)
    ```console
  	$ sudo pip install Django==<version>  (1.6.2 por ejemplo) 
    ```
- Iniciar un proyecto en Django
    ```console
    $ django-admin.py startproject <nombre del proyecto>
    esto nos crea una carpeta con los sgtes archivos
        |
        |-> <nombre del proyecto>
	      | |
	      | |-> __init__.py
	      | |
	      | |-> settings.py
	      | |
	      | |-> urls.py
	      | |
	      | |-> wsgi.py
	      |
	      |
	      |-> manage.py

	```
- Iniciar un servidor en django
    ```console
    $ python manage.py runserver   (al crearse el server estara por defecto en 127.0.0.1:8000)
	$ python manage.py runserver <#> (para sea el numero 80 como suele ser )
	// tambien con
	$ django-admin runserver --settings==mysite.settings
	``












