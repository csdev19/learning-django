
'''
    B  A  S  E   V  I  E  W  S


Las vistas base estas compuestas por las clases:

View: Vista maestra TODAS las demas heredan de esta
|
|-> tiene http_method_names = ['get','post','put','delete','patch','head','options','trace']
|
|-> metodos:
|   |-> as_view(**initkwargs)
|   |-> dispatch(request,*args,**kwargs)
|   |-> http_method_not_allow(request,*args,**kwargs)
|   |-> options(request,*args,**kwargs)
|
|

-TemplateView
-RedirectView


La vista View es el padre de todas las demas Class-Based-Views
'''
from django.views.generic import View
from django.shortcuts import render

class ThisIsAView(View):

    def get(self,request,*args,**kwargs):
        return render(request, 'template_name.html')

    def post(self,request,*args,**kwargs):
        return render(request, 'template_name.html')
#----------------------------------------------

'''
    T  E  M  P  L  A  T  E   V  I  E  W


Esta vista hereda de:
-TemplateResponseMixin: Da la funcionalidad para renderizaun template
-ContextMixin: Da la funcionalidad para tomar un contexto y pasarlo al template
-View: La vista padre
'''

#   urls.py

#   views.py
from django.views.generic import TemplateView

class ThisIsATemplateView(TemplateView):
    template_name= 'nombre-del-html.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['variable'] = Model.objects.all()
        return context



# name.html
'''
<head>
    <title>TemplateView </title>
</head>
<body>
    <h1>Este es TemplateView</h1>
<!-- aqui podemos ver que solo debemos llamarlo por su nombreen el diccionario 'context'-->
    <p> {{ variable }} </p>
</body>
'''
#----------------------------------------------
'''
    D  E  T  A  I  L   V  I  E  W

Es la vista que nos permite obtener un solo objeto del modelo
|
|-> por defecto solo funcionara si enviamos un pk o un slug

'''
#urls.py
#path('<slug:slug>') o path('<int:pk>')


#views.py
from django.views.generic import DetaielView
# que debe ser importado
#-> from <ruta>.models import Modelo


class ThisIsADetailView(DetaielView):
    #obliga a poner el nombre del modelo
    model = Modelo
    # y devuelve la informacion como una variable 'object'
    template_name = 'nombre-del-template.html'
    slug_field = 'atributo'
    # esto hace que enves de toma el slug/pk tomara el atributo indicado el cual puede ser incluso un atributo del modelo como name, lastname, etc
    context_object_name = 'nombre-del-contexto-del-objeto'
    # es para que podamos personalizar el nombre

# <>.html
'''
<html>
<head>
    <title>detail view </title>
</head>
<body>
    <h1>Detail View</h1>
    {{ object.atribute }}
</body>
'''
#----------------------------------------------
'''
    L  I  S  T   V  I  E  W

Es la vista que nos permite obtener una lista de objetos de un modelo

'''
#urls.py
path('<nombre>/')

#views.py
from django.views.generic import ListView
#from <nombre>.models import Modelo


class ThisIsAListView(ListView):
    model = Modelo
    #devuelve un 'object_list' el cual podemos iterar
    template_name = 'nombre-del-template.html'
    context_object_name = 'para-cambiar-el-nombre-de-object_list'
    # para hacer una consulta
    queryset = Modelo.objects.filter('<inserta querys>')
    # y este queryset se enviara al context_object_name

# <>.html
'''
<html>
<head>
    <title>list view </title>
</head>
<body>
    <h1>List View</h1>
    {% for object in object_list %}
    {{ object.atribute }}
    {% endfor %}
</body>
'''

#
#
# Y NO OLVIDAR QUE EN ESTAS VISTAS POR LA HERENCIA PODEMOS USAR LOS METODOS PASADOS
# 
#
#


