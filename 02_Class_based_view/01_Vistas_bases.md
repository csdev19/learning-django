# Class Based Views (Vistas basadas en clases)

## Links

- [Intro class based views](https://docs.djangoproject.com/en/2.0/topics/class-based-views/intro/)
- [Django Generic Views]()
- [Django class+functions based views](https://medium.com/zeitcode/djangos-views-functional-class-based-generics-e1d1444d1776)
- [Django class based views](https://docs.djangoproject.com/en/2.0/topics/class-based-views/)
- [Built-in class based views](https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-display/)

## Primera vista basica

- Hola mundo con clases
	```python
	<views.py>
	from django.views.generic import Templateview
	class HomeView(Templateview):
		template_name = 'hola.html'
	```
	```html
	<hola.html>
	<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<title>hola</title>
		<link rel="stylesheet" href="">
	</head>
	<body>
		<h1>Hola estas en HomeView</h1>
	</body>
	</html>
	```
	```python
	<urls.py>
	from django.urls import path
	from <nombre-de-app>.views import HomeView
	urlpattern = [
		path('home/', HomeView.as_view())
	]
	```

## BaseViews

Se les dicen vistas bases. Y son **View**, **TemplaView** y **RedirectView**

### View [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#django.views.generic.base.View)
- La clase maestra. Todas las demas clases heredan de esta. 
- Se importa de la siguiente manera
	```python
	from django.views import View
	```
- Metodos bases:
	- dispatch() [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch)
	- http_method_not_allowed() [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed)
	- options() [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#django.views.generic.base.View.options)
- Lista de metodos **HTTP**: **['get', 'post', 'put', 'delete', 'head', 'options', 'trace']**
- Ejemplo:
	```python
	from django.views import View
	class ExampleView(View):
		def get(self, request, *args, **kwargs):
			return render(request, template_name, {})
		def post(self,request, *args, **kwargs):
			return render(request, template_name, {})
	```
- Y para renderizar en URLS.PY se usa **as_view()** 

### Templateview [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#django.views.generic.base.TemplateView)
- Su funcion es renderizar un template.
- Sus ancestros son:
	- django.views.generic.base.TemplateResponseMixin [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin)
	- django.views.generic.base.ContextMixin [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin)
	- django.views.generic.base.View [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.get_context_data)
- Metodos:
	- get_context_data() [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.get_context_data)
	- http_method_not_allowed() [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed)
 	- dispatch() [link](https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch)
- Ejemplo:
	```python
	from django.views.generic import Templateview
	class ExampleTemplateView(Templateview):
		template_name = 'home.html'
		def get_context_data(self, **kwargs):
			context = super(ExampleTemplateView, self).get_context_data(**kwargs)
			context['objeto'] = 'hola soy un objeto'
			return context
	```
	```html
	<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<title>Home</title>
		<link rel="stylesheet" href="">
	</head>
	<body>
		<!-- se renderiza de la siguiente manera -->
		{{ objeto }}
	</body>
	</html>
	```

- **Al heredar de View tambien puede accesar a los metodos HTTP que VIEW tiene**
- Y para renderizar en URLS.PY se usa **as_view()** 

### RedirectView
- Redirecciona hacia otra URL que se especifique.
- Solo hereda de **View**
	```python
	from django.views.generic import Templateview, RedirectView
	class ExampleTemplateView(Templateview):
		template_name = 'home.html'
		def get_context_data(self, **kwargs):
			context = super(ExampleTemplateView, self).get_context_data(**kwargs)
			context['objeto'] = 'hola soy un objeto'
			return context
	class ExampleRedirectView(RedirectView):
		pattern_name = 'home'
		def get_redirect_url(self, *args, **kwargs):
        	return super().get_redirect_url(*args, **kwargs)
	```

### TemplateResponseMixin
- Da la funcionalidad para renderizar un template

### ContextMixin
- Da la funcionalidad para tomar un **contexto** y pasarlo a un template