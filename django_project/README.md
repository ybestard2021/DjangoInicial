# Sistema Empresarial - Laboratorio 01

## 1. Propósito del proyecto

Primera versión de un Sistema Empresarial desarrollado con Django para
el curso "Desarrollo de Aplicaciones Empresariales". Gestiona un
catálogo simple de ítems (`Item`) mediante una vista de listado y el
panel de administración de Django. Sirve como base para los siguientes
laboratorios del curso.

## 2. Requisitos

- Python 3.10 o superior (probado con Python 3.14).
- Django 5.x (`Django>=5,<6`).
- SQLite (incluido con Python, base de datos por defecto de Django).
- Windows 11 + PowerShell.

## 3. Estructura principal

```
django_project/
├── venv/                  # entorno virtual (no se sube a Git)
├── requirements.txt
├── README.md
└── src/
    ├── manage.py
    ├── db.sqlite3
    ├── config/             # configuración del proyecto Django
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    └── core/                # app con el modelo Item
        ├── migrations/
        ├── templates/
        │   ├── base.html
        │   └── core/item_list.html
        ├── admin.py
        ├── models.py
        ├── urls.py
        └── views.py
```

## 4. Creación y activación del entorno virtual

Crear el entorno virtual (solo la primera vez):

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

## 6. Migraciones

Desde `django_project/src`:

```powershell
python manage.py makemigrations
python manage.py migrate
```

## 7. Creación del superusuario

Desde `django_project/src`:

```powershell
python manage.py createsuperuser
```

Se solicitarán usuario, correo (opcional) y contraseña de forma
interactiva.

## 8. Ejecución del servidor

Desde `django_project/src`:

```powershell
python manage.py runserver
```

## 9. URLs principales

- `http://127.0.0.1:8000/` — Listado de ítems (`item_list`).
- `http://127.0.0.1:8000/admin/` — Panel de administración de Django.
