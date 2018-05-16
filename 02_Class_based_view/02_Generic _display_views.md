# Generic Display View

## Link
- [Documentation django](https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/)

## DetailView
- Es una vista que nos permite obtener **1 solo objeto** de un modelo de acuerdo a lo que pasemos por parametro en la url por defecto.
- Desde la **ulr** **debemos** enviar **pk o un slug**.
- Ancestros
	- django.views.generic.detail.SingleObjectTemplateResponseMixin [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin)
	- django.views.generic.base.TemplateResponseMixin [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin)
	- django.views.generic.detail.BaseDetailView [link]() No existe seugn parece xdxd
	- django.views.generic.detail.SingleObjectMixin [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin)
	- django.views.generic.base.View [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#django.views.generic.base.View)
- Metodos disponibles
	- dispatch()
	- http_method_not_allowed()
	- get_template_names()
	- get_slug_field()
	- get_queryset()
	- get_object()
	- get_context_object_name()
	- get_context_data()
	- get()
	- render_to_response()
- Ejemplo
	- View.py
	```python
	from django.views.generic import DetailView
	from .models import AnyModel
	class ExampleDetailView(DetailView):
		# con este objeto devuelve otro contexto llamado "object" por defecto
		model = Article
		template_name = 'detail_view.html'
		# esto devuelve al template un contexto
		def get_context_data(self, **kwargs):
			context = super().get_context_data(**kwargs)
        	context['hola'] = "que tal"
        	return context
		# nos permite ponerle otro nombre al objeto que devolvemos por defecto
		context_object = 'otro-nombre-de-objeto'
		# nos permite pasarle enves de un pk o slug, desde la url otro tipo de atributo
		# en este caso el campo 'nombre' de nuestro modelo
		slug_field = 'nombre'
	```
	- Models.py
	```python
	from django.db import models
	class AnyModel(models.Model):
		nombre = models.CharField(max_length=233)
		apellido = models.CharField(max_length=233)
	```
	- detail_view.html
	```html
	<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<title>DetailView</title>
		<link rel="stylesheet" href="">
	</head>
	<body>
		<!-- cuando no ponemos slug_field asi debemos llamar a los atributos
		del objeto 
		<h1>Hola {{ object.nombre }} {{ object.apellido}}</h1> -->
		<!-- Esto es con slug_field -->
		<h1>Hola {{ otro-nombre-de-objeto.nombre }} {{ otro-nombre-de-objeto.apellido }}</h1>
		<!-- <p> {{ hola }}</p>   retorna "que tal" como los ejemplos anteriores -->
	</body>
	</html>
	```
- Y como tambien hereda de **VIEW** puede usar su lista de metodos **HTTP**


## ListView
- Es la vista que nos permite obtener una **lista de objetos** de **1 modelo**
- Mientras se este ejecutando, **object_list** contendra la lista de los objetos (que tambien puede ser un queryset)
- Ancestros:
	- django.views.generic.list.MultipleObjectTemplateResponseMixin [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectTemplateResponseMixin)
	- django.views.generic.base.TemplateResponseMixin [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin)
	- django.views.generic.list.BaseListView [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#django.views.generic.list.BaseListView)
	- django.views.generic.list.MultipleObjectMixin [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin)
	- django.views.generic.base.View  [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#django.views.generic.base.View)
- Metodos disponibles:
	- dispatch()
	- http_method_not_allowed()
	- get_template_names()
	- get_queryset()
	- get_context_object_name()
	- get_context_data()
	- get()
	- render_to_response()
- Ejemplo:
	- Views.py
	```python
	from django.views.generic import ListView
	from .models import AnyModel
	class ExampleListView(ListView):
		model = AnyModel
		template_name = 'list_view.html'
		context_object_name = 'personas'
		queryset = AnyModel.objects.filter(<cualquier argumento>)
	```
	- Models.py
	```python
	from django.db import models
	class AnyModel(models.Model):
		nombre = models.CharField(max_length=233)
		apellido = models.CharField(max_length=233)
	```
	- list_view.html
	```html
	<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<title>ListView</title>
		<link rel="stylesheet" href="">
	</head>
	<body>
		<h1></h1>
		<!-- {% for person in object_list %} -->
		{% for persona in personas %}
			<p>{{ persona.nombre }}</p>
			<p>{{ persona.apellido }}</p>
		{% endfor %}
	</body>
	</html>
	```
- Tambien hereda de **View** asi que podemos usar los metodos **HTTP**