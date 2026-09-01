# Sistema Empresarial — Semana 3
## Django ORM y SQLite

## 1. Objetivo

Este proyecto es una **evolución directa** del proyecto utilizado en la
Semana 2. Reutiliza exactamente la misma arquitectura (`config`, `core`,
modelo `Item`) para que el estudiante no tenga que aprender nada nuevo en
cuanto a estructura, y pueda concentrarse exclusivamente en comprender:

```text
Model
 ↓
Manager
 ↓
QuerySet
 ↓
Django ORM
 ↓
SQL
 ↓
SQLite
```

y el camino inverso, desde la base de datos hasta el navegador:

```text
SQLite
 ↓
Django ORM
 ↓
QuerySet
 ↓
View
 ↓
Context
 ↓
Template
 ↓
Navegador
```

## 2. Requisitos

- Python 3.10 o superior (probado con Python 3.14).
- Django 5.2.x (`Django==5.2.17`).
- SQLite (incluido con Python).
- Windows 11 + PowerShell.

## 3. Estructura principal

```text
django_project_s03/
├── .gitignore
├── requirements.txt
├── README.md
└── src/
    ├── manage.py
    ├── db.sqlite3          # se genera al migrar, no se sube a Git
    ├── config/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    └── core/
        ├── migrations/
        ├── templates/
        │   ├── base.html
        │   └── core/
        │       ├── item_list.html
        │       └── item_form.html
        ├── admin.py
        ├── models.py
        ├── urls.py
        └── views.py
```

Es la misma estructura que `django_project/` (Semana 2), en una carpeta
paralela e independiente. Los paquetes `config` y `core` conservan sus
nombres originales.

## 4. Creación y activación del entorno virtual

Este proyecto usa su **propio** entorno virtual (no el de Semana 2).

Crearlo (solo la primera vez), desde `django_project_s03/`:

```powershell
python -m venv venv
```

Activarlo en PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

## 5. Instalación de dependencias

Con el entorno virtual activado:

```powershell
python -m pip install -r requirements.txt
```

## 6. Base de datos: SQLite

`config/settings.py` define explícitamente SQLite como motor:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

El archivo resultante es `src/db.sqlite3`. No se sube al repositorio
(está excluido en `.gitignore`).

## 7. Migraciones

Desde `django_project_s03/src`:

```powershell
python manage.py makemigrations
python manage.py migrate
```

Flujo conceptual:

```text
models.py
 ↓
makemigrations   (Django detecta cambios en el modelo y genera un archivo)
 ↓
archivo de migración (core/migrations/0001_initial.py)
 ↓
migrate          (aplica ese archivo contra la base de datos)
 ↓
SQLite
```

## 8. Creación del superusuario

Desde `django_project_s03/src`:

```powershell
python manage.py createsuperuser
```

Se solicitarán usuario, correo (opcional) y contraseña de forma
interactiva.

## 9. Ejecución del servidor

Desde `django_project_s03/src`:

```powershell
python manage.py runserver
```

## 10. URLs principales

- `http://127.0.0.1:8000/` — Listado de ítems (`item_list`).
- `http://127.0.0.1:8000/admin/` — Panel de administración de Django.

Usa el Admin (o el Shell, ver sección 13) para cargar algunos `Item` de
prueba, por ejemplo: `Laptop`, `Mouse`, `Teclado`, `Monitor`, `Impresora`.

## 11. Manager, QuerySet y ORM

- **Model** (`Item`): representa la entidad — una tabla de la base de
  datos, expresada como clase Python.
- **Manager** (`Item.objects`): es el punto de acceso habitual al ORM
  para ese Model.
- **QuerySet**: el resultado de una operación como `.filter()` o
  `.all()` — una consulta construida mediante Django, todavía no
  necesariamente ejecutada contra la base de datos.
- **ORM**: la capa que traduce esas operaciones Python a sentencias SQL.
- **SQLite**: el motor que finalmente ejecuta esa SQL y almacena los
  datos.

```text
Item
 ↓
objects
 ↓
filter()
 ↓
QuerySet
 ↓
ORM
 ↓
SQL
 ↓
SQLite
```

## 12. Ejemplos de consultas (QuerySets)

Django ORM evita que el estudiante tenga que escribir manualmente
`SELECT`, `INSERT`, `UPDATE` o `DELETE` en las Views. A modo de
referencia, cada ejemplo incluye el SQL conceptual equivalente — pero el
trabajo real se hace siempre a través del ORM, nunca con SQL manual.

**Obtener todos**

```python
Item.objects.all()
# aprox: SELECT * FROM core_item;
```

**Filtrar**

```python
Item.objects.filter(name="Laptop")
# aprox: SELECT * FROM core_item WHERE name = 'Laptop';
```

**Buscar por contenido**

```python
Item.objects.filter(name__icontains="lap")
# aprox: SELECT * FROM core_item WHERE name LIKE '%lap%';
```

**Ordenar**

```python
Item.objects.order_by("name")
Item.objects.order_by("-created_at")   # el "-" invierte el orden
```

**Obtener uno**

```python
Item.objects.get(id=1)
```

**Contar**

```python
Item.objects.count()
```

**Excluir**

```python
Item.objects.exclude(name__icontains="laptop")
```

No es necesario usar todos estos QuerySets a la vez en la View
principal — el código se mantiene sencillo y didáctico.

## 13. Django Shell: ver el SQL generado

Para ejecutar consultas ORM manualmente y observar el SQL que Django
genera, desde `django_project_s03/src`:

```powershell
python manage.py shell
```

Dentro del shell:

```python
from core.models import Item

items = Item.objects.all()
print(items)

items = Item.objects.filter(name__icontains="a")
print(items.query)   # muestra el SQL generado por Django
```

Esto demuestra:

```text
QuerySet
 ↓
Django ORM
 ↓
SQL generado
 ↓
SQLite
```

## 14. CRUD mediante ORM

**CREATE**

```python
Item.objects.create(name="Laptop", description="Laptop para oficina")
```

```text
Python
 ↓
Django ORM
 ↓
INSERT
 ↓
SQLite
```

**READ**

```python
Item.objects.all()
Item.objects.filter(...)
Item.objects.get(...)
```

**UPDATE**

```python
item = Item.objects.get(id=1)
item.name = "Laptop Gamer"
item.save()
```

```text
get()
 ↓
Objeto Item
 ↓
modificación
 ↓
save()
 ↓
ORM
 ↓
UPDATE
 ↓
SQLite
```

**DELETE**

```python
item = Item.objects.get(id=1)
item.delete()
```

```text
Objeto Item
 ↓
delete()
 ↓
ORM
 ↓
DELETE
 ↓
SQLite
```

Todos estos ejemplos se ejecutan desde `python manage.py shell` — no
forman parte de la View principal, que se mantiene simple.

## 15. La View principal

`core/views.py` mantiene una View muy parecida a la de Semana 2:

```python
def item_list(request):
    items = Item.objects.order_by("-created_at")
    return render(request, "core/item_list.html", {"items": items})
```

En Semana 2 se usaba `Item.objects.all()` (sin orden explícito). Aquí se
usa `order_by("-created_at")` para mostrar los ítems más recientes
primero — un QuerySet distinto, pero conectado exactamente al **mismo
Template**:

```text
SEMANA 2                          SEMANA 3

Item.objects.all()                Item.objects.order_by("-created_at")
       ↓                                 ↓
   Template          ==   mismo  ==   Template
       ↓                                 ↓
 Todos los Items                Items ordenados por fecha
```

La idea central: se puede cambiar **la consulta** sin tener que cambiar
**el Template**.

## 16. Flujo completo (navegador → SQLite → navegador)

```text
NAVEGADOR
   ↓
Request
   ↓
config/urls.py
   ↓
core/urls.py
   ↓
core/views.py
   ↓
Item.objects...
   ↓
Manager
   ↓
QuerySet
   ↓
DJANGO ORM
   ↓
SQL generado
   ↓
SQLite
   ↓
Resultados
   ↓
QuerySet
   ↓
View
   ↓
Context
   ↓
Template
   ↓
HTML Response
   ↓
NAVEGADOR
```

## 17. Ejercicios sugeridos

Para practicar en `python manage.py shell`:

1. Mostrar todos los Items.
2. Ordenarlos alfabéticamente.
3. Mostrar los más recientes primero.
4. Buscar Items cuyo nombre contenga una palabra.
5. Contar cuántos Items existen.
6. Crear un Item mediante Django Shell.
7. Modificar un Item mediante ORM.
8. Eliminar un Item mediante ORM.

## 18. Registro de Items desde la aplicación web

Además de crear `Item` desde el Admin o el Shell, ahora existe un
formulario web simple para insertar un nuevo `Item` sin salir de la
aplicación:

- `http://127.0.0.1:8000/` — Listado, con un botón **Nuevo Item**.
- `http://127.0.0.1:8000/nuevo/` — Formulario de alta (`item_create`).

Este ejercicio usa a propósito un `<form>` HTML plano y `request.POST`
en vez de un `ModelForm`, para que la llamada a `Item.objects.create()`
quede completamente visible en `core/views.py`.

**FLUJO GET** (abrir el formulario)

```text
Navegador
   ↓
GET /nuevo/
   ↓
core/urls.py
   ↓
item_create()
   ↓
item_form.html
   ↓
Formulario
```

**FLUJO POST** (guardar el Item)

```text
Formulario
   ↓
POST /nuevo/
   ↓
core/urls.py
   ↓
item_create()
   ↓
request.POST
   ↓
Item.objects.create(...)
   ↓
Manager
   ↓
Django ORM
   ↓
INSERT
   ↓
SQLite
   ↓
redirect
   ↓
Listado actualizado
```

Si el campo `name` llega vacío, la View **no** llama a
`Item.objects.create()`: vuelve a mostrar `item_form.html` con el
mensaje "El nombre es obligatorio." y lo escrito hasta el momento.

### ¿Qué hace `Item.objects.create()`?

```python
# ORM: Django convierte esta operación Python en un INSERT SQL
# que finalmente ejecutará SQLite.
Item.objects.create(
    name=name,
    description=description
)
```

- **`Item`** = el Model — la entidad/tabla.
- **`objects`** = el Manager — el punto de acceso al ORM para ese Model.
- **`create(...)`** = método del Manager que construye el objeto **y**
  lo guarda de inmediato (equivale a `Item(...)` + `.save()` en un solo
  paso).
- **ORM** = traduce esa llamada Python a SQL.
- **SQLite** = ejecuta el `INSERT` y almacena el registro.

Conceptualmente (no se escribe en el código, solo para entender qué
hace el ORM por debajo):

```sql
INSERT INTO core_item (name, description, created_at)
VALUES (...);
```

Nosotros escribimos Python; Django ORM genera el SQL; SQLite lo
ejecuta. En ningún momento la aplicación usa `cursor`, SQL manual ni
librerías externas.

### ¿Por qué no hizo falta una migración?

`core/models.py` no cambió: el modelo `Item` ya tenía los campos
`name`, `description` y `created_at` desde la Semana 2. Agregar una
View y un formulario no requiere una migración porque la estructura del
modelo `Item` no cambió — las migraciones solo son necesarias cuando
cambia la forma de la tabla (campos nuevos, tipos, etc.), no cuando se
agrega código que usa el modelo existente.

## 19. Semana 2 vs. Semana 3

```text
Semana 2                          Semana 3
────────                          ────────
Arquitectura y flujo de Django    Acceso y manipulación de datos

Request                           Model
 ↓                                 ↓
URL                                Manager
 ↓                                 ↓
View                               QuerySet
 ↓                                 ↓
Model                              Django ORM
 ↓                                 ↓
Template                           SQL
 ↓                                 ↓
Response                           SQLite
```

Misma app `core`, mismo modelo `Item`, mismo Template — la diferencia
está en la funcionalidad y los ejemplos de ORM, no en la arquitectura.
