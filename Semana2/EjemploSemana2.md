# Ejemplo resuelto — TechParts (tienda de componentes de computadora)

**Material de referencia para el docente. No entregar al estudiante como parte del laboratorio.**

## Ejercicio 1 — Problemática

**TechParts** es una tienda local que vende componentes de computadora (procesadores, tarjetas gráficas, memorias RAM, almacenamiento, fuentes de poder, placas madre) a clientes que arman o actualizan su propia PC. Actualmente el catálogo se maneja en una hoja de cálculo, lo que dificulta consultar rápidamente qué hay disponible y agregar productos nuevos. Se necesita una aplicación web simple que muestre el catálogo y permita registrar nuevos componentes.

## Ejercicio 2 — Requisitos

- El sistema debe mostrar el listado de componentes disponibles en la tienda.
- Cada componente debe mostrar su categoría, marca, precio y stock.
- El usuario debe poder registrar un nuevo componente mediante un formulario.
- El sistema debe validar que el precio y el stock sean valores numéricos válidos antes de guardar.
- El usuario debe poder ver el componente recién agregado reflejado en el listado.

## Ejercicio 3 — Diseño del modelo de datos

Entidad principal: **Componente**

| Campo | Tipo | Obligatorio | Justificación |
|---|---|---|---|
| `name` | texto | Sí | Identifica el producto (ej. "Ryzen 5 5600X") |
| `category` | texto | Sí | Permite organizar el catálogo (CPU, GPU, RAM, etc.) |
| `brand` | texto | Sí | El cliente suele buscar por marca (AMD, NVIDIA, Kingston...) |
| `price` | decimal | Sí | Necesario para mostrar y comparar precios |
| `stock` | entero | Sí | Indica disponibilidad para la venta |

## Ejercicio 4 — Crear la App

```bash
python manage.py startapp components
```

```python
# config/settings.py
INSTALLED_APPS = [
    ...
    'core',
    'components',
]
```

## Ejercicio 5 — Model con datos estáticos

```python
# components/models.py

COMPONENTS = [
    {"id": 1, "name": "Ryzen 5 5600X", "category": "CPU", "brand": "AMD", "price": 189.99, "stock": 12},
    {"id": 2, "name": "GeForce RTX 4060", "category": "GPU", "brand": "NVIDIA", "price": 349.99, "stock": 7},
    {"id": 3, "name": "Fury Beast 16GB DDR4", "category": "RAM", "brand": "Kingston", "price": 42.50, "stock": 25},
    {"id": 4, "name": "NV2 1TB NVMe", "category": "Almacenamiento", "brand": "Kingston", "price": 65.00, "stock": 18},
    {"id": 5, "name": "B550M Pro4", "category": "Placa Madre", "brand": "ASRock", "price": 99.90, "stock": 9},
]
```

## Ejercicio 6 — Listado (View + URL + Template)

```python
# components/views.py
from django.shortcuts import render

from .models import COMPONENTS


def component_list(request):
    return render(request, 'components/component_list.html', {'components': COMPONENTS})
```

```python
# components/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('components/', views.component_list, name='component_list'),
]
```

```python
# config/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('components.urls')),
]
```

```django
{# components/templates/components/component_list.html #}
{% extends "base.html" %}

{% block content %}
  <h2>TechParts — Catálogo de componentes</h2>
  <a href="{% url 'component_create' %}">Agregar componente</a>
  <table border="1">
    <thead>
      <tr><th>Nombre</th><th>Categoría</th><th>Marca</th><th>Precio</th><th>Stock</th></tr>
    </thead>
    <tbody>
      {% for c in components %}
      <tr>
        <td>{{ c.name }}</td>
        <td>{{ c.category }}</td>
        <td>{{ c.brand }}</td>
        <td>${{ c.price }}</td>
        <td>{{ c.stock }}</td>
      </tr>
      {% empty %}
      <tr><td colspan="5">No hay componentes registrados.</td></tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}
```

## Ejercicio 7 — Formulario (Forms)

```python
# components/forms.py
from django import forms

CATEGORY_CHOICES = [
    ("CPU", "CPU"),
    ("GPU", "GPU"),
    ("RAM", "RAM"),
    ("Almacenamiento", "Almacenamiento"),
    ("Placa Madre", "Placa Madre"),
    ("Fuente", "Fuente de poder"),
]


class ComponentForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Categoría")
    brand = forms.CharField(max_length=100, label="Marca")
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0, label="Precio")
    stock = forms.IntegerField(min_value=0, label="Stock")
```

## Ejercicio 8 — Vista de creación

```python
# components/views.py (agregar debajo de component_list)
from django.shortcuts import redirect

from .forms import ComponentForm


def component_create(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            new_id = max(c['id'] for c in COMPONENTS) + 1 if COMPONENTS else 1
            COMPONENTS.append({
                'id': new_id,
                'name': form.cleaned_data['name'],
                'category': form.cleaned_data['category'],
                'brand': form.cleaned_data['brand'],
                'price': float(form.cleaned_data['price']),
                'stock': form.cleaned_data['stock'],
            })
            return redirect('component_list')
    else:
        form = ComponentForm()

    return render(request, 'components/component_form.html', {'form': form})
```

```python
# components/urls.py (actualizado)
urlpatterns = [
    path('components/', views.component_list, name='component_list'),
    path('components/nuevo/', views.component_create, name='component_create'),
]
```

```django
{# components/templates/components/component_form.html #}
{% extends "base.html" %}

{% block content %}
  <h2>Agregar componente</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Guardar</button>
  </form>
{% endblock %}
```

## Ejercicio 9 — Verificación del flujo completo

1. `GET /components/` → `config/urls.py` → `components/urls.py` → `component_list()` → lee `COMPONENTS` de `models.py` → `component_list.html` → HTML con los 5 componentes iniciales.
2. Click en "Agregar componente" → `GET /components/nuevo/` → `component_create()` muestra el formulario vacío.
3. Se envía el formulario → `POST /components/nuevo/` → `form.is_valid()` valida `price`/`stock` como numéricos → se hace `.append()` sobre la lista `COMPONENTS` → `redirect('component_list')`.
4. `GET /components/` nuevamente → el nuevo componente aparece en la tabla, confirmando que `views.py` y `models.py` comparten la misma lista en memoria.
5. Nota para el informe: si se reinicia `runserver`, el componente agregado desaparece porque `COMPONENTS` vive en memoria, no en disco — esto es esperado.

`core` sigue funcionando en paralelo mostrando su propio listado de `Item` en `/`, sin que `components` lo afecte: ambas Apps conviven dentro del mismo Project `config`.

## Ejercicio 10 — Publicar en GitHub

```bash
pip freeze > requirements.txt
git add .
git commit -m "Add components app: catalog + creation form (static data)"
git push
```
