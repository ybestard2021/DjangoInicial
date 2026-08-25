# Proyecto: Sistema Empresarial Django - Laboratorio 01

## Contexto

Este proyecto corresponde al Laboratorio 01 del curso
"Desarrollo de Aplicaciones Empresariales".

El objetivo es construir la primera versión de un Sistema Empresarial
utilizando Django. La aplicación debe gestionar un catálogo simple de
ítems y servirá como base para los siguientes laboratorios del curso.

El entorno de desarrollo es Windows 11 y Visual Studio Code.

## Tecnologías obligatorias

- Python 3.10 o superior.
- Django 5.x.
- HTML5.
- CSS cuando sea necesario.
- JavaScript vanilla únicamente para el reto opcional.
- SQLite como base de datos por defecto de Django.
- Git para control de versiones.
- GitHub para alojar el repositorio.

## Sistema operativo

El proyecto se desarrolla en Windows.

Cuando muestres o ejecutes comandos debes utilizar comandos compatibles
con PowerShell de Windows.

No utilizar comandos exclusivos de Linux como:

source venv/bin/activate

Para activar el entorno virtual en PowerShell utilizar:

.\venv\Scripts\Activate.ps1

## Regla principal

Debes desarrollar el proyecto siguiendo EXACTAMENTE el orden y la
estructura definidos en este documento.

No cambies nombres de carpetas, aplicaciones, modelos, campos, vistas
o archivos salvo que sea técnicamente necesario.

Si encuentras un problema, explica primero el problema y luego propone
la corrección.

## Estructura requerida

El workspace actual MyDjango solamente es el contenedor de trabajo.

Dentro de él debes crear el proyecto del laboratorio con esta estructura:

MyDjango/
│
├── AGENTS.md
│
└── django_project/
    │
    ├── venv/
    │
    ├── requirements.txt
    ├── README.md
    │
    └── src/
        │
        ├── manage.py
        │
        ├── db.sqlite3
        │
        ├── config/
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   ├── asgi.py
        │   └── wsgi.py
        │
        └── core/
            ├── migrations/
            ├── templates/
            │   ├── base.html
            │   └── core/
            │       └── item_list.html
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── models.py
            ├── tests.py
            ├── urls.py
            └── views.py

La carpeta .venv que ya pueda existir en MyDjango NO pertenece al
laboratorio y no debe utilizarse.

## Ejercicio 1 - Preparar el entorno

Crear:

django_project/

Dentro de django_project crear un entorno virtual llamado:

venv

Después crear:

django_project/src/

No instalar paquetes globalmente.

## Ejercicio 2 - Instalar Django

Activar el entorno virtual `venv`.

Instalar Django versión 5.

Verificar la versión instalada.

Utilizar preferentemente:

python -m pip install "Django>=5,<6"

y comprobar con:

python -m django --version

## Ejercicio 3 - Crear proyecto Django

Dentro de:

django_project/src/

crear un proyecto Django llamado:

config

Debe utilizarse una estructura en la que:

django_project/src/manage.py

quede directamente dentro de src y la configuración quede en:

django_project/src/config/

Equivalente a ejecutar desde src:

django-admin startproject config .

## Ejercicio 4 - Aplicación core

Crear una aplicación Django llamada:

core

mediante:

python manage.py startapp core

Registrar `core` en:

src/config/settings.py

dentro de INSTALLED_APPS.

## Ejercicio 5 - Modelo Item

En:

src/core/models.py

crear:

class Item(models.Model)

con exactamente estos campos:

- name: campo de texto.
- description: campo de texto largo y opcional.
- created_at: fecha y hora asignada automáticamente al crearse.

Implementar también __str__ para devolver el nombre del ítem.

Después generar y aplicar las migraciones correspondientes.

## Ejercicio 6 - Vista y URLs

Crear en:

src/core/views.py

una vista llamada:

item_list

La vista debe:

1. Obtener todos los objetos Item.
2. Enviarlos a una plantilla.
3. Utilizar Django ORM.

Crear:

src/core/urls.py

y definir la URL correspondiente.

En:

src/config/urls.py

utilizar include() para conectar las URLs de core.

La página principal:

http://127.0.0.1:8000/

debe mostrar item_list.

## Ejercicio 7 - Templates

Crear:

src/core/templates/base.html

con la estructura HTML general.

Crear:

src/core/templates/core/item_list.html

La plantilla item_list.html debe heredar de base.html.

Utilizar:

{% for %}

para mostrar los ítems.

Utilizar:

{% empty %}

cuando no existan registros.

Debe mostrarse como mínimo:

- nombre
- descripción
- fecha de creación

No utilizar librerías frontend innecesarias para esta primera versión.

## Ejercicio 8 - Administrador

Registrar Item en:

src/core/admin.py

Preparar el proyecto para crear un superusuario.

El administrador debe estar disponible en:

/admin/

El usuario cargará al menos dos Item de prueba desde el administrador.

No inventar automáticamente las credenciales del superusuario.

Si se requiere crear el superusuario, detenerse y pedir al usuario que
introduzca las credenciales cuando Django las solicite.

## Ejercicio 9 - Verificación

Ejecutar:

python manage.py check

y corregir cualquier error.

Después ejecutar las migraciones necesarias.

Comprobar que el servidor pueda iniciarse con:

python manage.py runserver

Comprobar:

http://127.0.0.1:8000/

y:

http://127.0.0.1:8000/admin/

No considerar terminado el proyecto mientras existan errores de Django.

## Ejercicio 10 - Documentación

Crear:

requirements.txt

Debe reflejar las dependencias reales instaladas en el entorno virtual.

Crear:

README.md

El README debe explicar:

1. Nombre y propósito del proyecto.
2. Requisitos.
3. Estructura principal.
4. Creación y activación del entorno virtual.
5. Instalación de dependencias.
6. Migraciones.
7. Creación del superusuario.
8. Ejecución del servidor.
9. URLs principales.

## Git

Crear un archivo:

.gitignore

que excluya como mínimo:

venv/
__pycache__/
*.pyc
db.sqlite3
.vscode/
.env

No incluir contraseñas, tokens ni claves en Git.

No ejecutar `git push` sin autorización explícita del usuario.

Puedes preparar los comandos Git y el repositorio local, pero antes de
publicar información en GitHub debes pedir autorización.

## Reto opcional

No implementar el reto opcional hasta que los ejercicios 1 al 10
funcionen correctamente.

Posteriormente se podrá implementar:

- estilos CSS;
- buscador o filtro mediante JavaScript;
- endpoints API para Item;
- frontend HTML/CSS/JavaScript o React.

## Forma de trabajo de Codex

Antes de modificar el proyecto:

1. Inspecciona el estado actual de los archivos.
2. Determina qué ejercicios ya están completados.
3. No destruyas trabajo existente que sea correcto.
4. Presenta brevemente el plan.
5. Ejecuta los ejercicios en orden.
6. Después de cada etapa verifica que no existan errores.
7. Si un comando falla, analiza el error antes de continuar.

Puedes crear y modificar archivos y ejecutar los comandos necesarios
para desarrollar el proyecto.

## Restricciones importantes

- No utilizar Flask, FastAPI ni otro framework.
- No reemplazar Django Templates por React en la solución principal.
- No utilizar Django REST Framework en los ejercicios obligatorios.
- No cambiar el modelo Item por Product u otro nombre.
- No cambiar `core` por otro nombre.
- No cambiar `config` por otro nombre.
- No cambiar la estructura src/.
- No utilizar una base de datos externa para este laboratorio.
- No implementar funcionalidades que no hayan sido solicitadas.
- Priorizar código sencillo y educativo.

## Objetivo pedagógico

El código debe ser suficientemente claro para que un estudiante pueda
explicar durante una sustentación:

- qué es el proyecto Django;
- qué es una app;
- qué hace settings.py;
- qué hace urls.py;
- qué hace views.py;
- qué es un modelo;
- cómo funcionan las migraciones;
- cómo se comunica una vista con un template;
- cómo funciona el administrador de Django.

Cuando implementes una parte importante, explica brevemente qué hiciste
y por qué, evitando explicaciones innecesariamente complejas.