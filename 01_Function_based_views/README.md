# Function Based Views (Vistas basadas en funciones)

## Links
- [Writtings Views](https://docs.djangoproject.com/en/2.0/topics/http/views/)
- [Documentacion](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)
- [Django shortcuts functions](https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/)


## Vista basica (hola mundo)
- Como hacer nuestro hola mundo con django
    - Creamos un archivo views.py
    ```python
    from django.http import HttpResponse

    def hello_world(request):
        return HttpResponse("hello world")

    ```
    - En el archivo urls.py
    ```
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^$', views.hello_world)
    ]
    ```
- Como servir html con django y funciones:
    ```python
    from django.shortcuts import render

    def home(request):
        saludo = "hola como estas desde la funcion home"
        context = {
            'saludo' : saludo
        } # es un diccionario que mandaremos al template "hello.html"
        return render(request, 'hello.html', context)
    ```
    ```html
    hello.html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hola es mi primer template</title>
        </head>
        <body>
            <h1>Bienvenido al template</h1>
            <p>{{ saludo }}</p> <!-- devuelve "hola como estas desde la funcion home" -->
        </body>
    </html>
    ```
- Con funciones podemos acceder a metodos HTTP
    ```python
    from django.shortcuts import render

    def my_create_view(request, pk):
        template_name = 'form.html'

        if request.method == 'POST':
            pass // do something

        if request,method == 'GET':
            pass // do something

        return render(request, template_name, {})
    ```

## Django Shortcut functions

1. Render(request, template_name, context=None, content_type=None, status=None, using=None)

- request: el objeto generado para la respuesta. (desde aqui accedes a los metodos basicos HTTP)
- template_name: aqui va el nombre del template (toda la rua)
- context: El contexto que se enviara al template, por defecto en **None**
- El resto esta en la documentacion.

2. Redirect(to, permanent=False,  *args, ** kwargs )

- to : hacia donde queires ser redireccionado
- en la documentacion


3. Get_object_or_404(klass, *args, ** kwargs)

- Klass : El nombre del objeto.


