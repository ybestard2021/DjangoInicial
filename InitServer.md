# Cómo arrancar el servidor Django — DjangoInicial

Guía rápida para no repetir los errores de hoy (venv no activo, carpeta equivocada,
Django instalado en el Python equivocado).

Ruta del proyecto:
`D:\Profesor\Cursos\2026-2\Desarrollo de Aplicaciones Empresariales\DjangoInicial`

---

## Pasos (en orden, siempre los mismos)

### 1. Abrir una terminal en la raíz del repo

En VS Code: `Ctrl + ñ` (o el ícono de terminal). Debe verse algo como:

```
D:\Profesor\Cursos\2026-2\Desarrollo de Aplicaciones Empresariales\DjangoInicial>
```

Si no estás ahí, muévete con `cd` hasta esa ruta.

### 2. Activar el entorno virtual

```cmd
.venv\Scripts\activate.bat
```

✅ El prompt **debe cambiar** a:

```
(.venv) D:\Profesor\Cursos\2026-2\Desarrollo de Aplicaciones Empresariales\DjangoInicial>
```

❌ Si NO aparece `(.venv)` al inicio, **no sigas** — repite este paso o revisa que la carpeta `.venv` exista.

### 3. Confirmar que Django está disponible

```cmd
python -m django --version
```

✅ Debe mostrar: `5.2.17`

❌ Si dice `No module named django`, instala las dependencias (con el venv YA activo):

```cmd
pip install -r django_project\requirements.txt
```

y vuelve a correr `python -m django --version` para confirmar.

### 4. Entrar a la carpeta donde vive manage.py

```cmd
cd django_project\src
```

Verifica que estás en el lugar correcto:

```cmd
dir manage.py
```

Debe listarlo sin error "No se encuentra el archivo".

### 5. Aplicar migraciones

```cmd
python manage.py migrate
```

(Solo afecta a la app `core`; la app `Semana2` usa datos en memoria y no necesita esto.)

### 6. Arrancar el servidor

```cmd
python manage.py runserver
```

✅ Verás algo como:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

**Esto es correcto y normal**: el comando se queda "corriendo" en esa terminal a propósito
(no se congeló, no hay que darle Enter ni nada más). Mientras esté así, el servidor está
activo.

### 7. Probar en el navegador

- `http://127.0.0.1:8000/` → listado de Item (core)
- `http://127.0.0.1:8000/components/` → catálogo TechParts (Semana2)
- `http://127.0.0.1:8000/components/nuevo/` → formulario para agregar un componente

### 8. Detener el servidor

En la misma terminal donde corre `runserver`: `Ctrl + C` (o `Ctrl + Break`).

---

## ⚠️ Errores comunes y qué significan

| Mensaje de error | Causa | Solución |
|---|---|---|
| `can't open file '...manage.py'` | Estás en la carpeta equivocada | Ve al paso 4: `cd django_project\src` |
| `ModuleNotFoundError: No module named 'django'` | El venv no está activo, o Django no está instalado ahí | Repite el paso 2, luego el paso 3 |
| El prompt no dice `(.venv)` | El entorno virtual no está activado en esta terminal | Vuelve a correr el paso 2 en **esta misma terminal** (activar es por sesión, no es permanente) |
| `pip install` "success" pero Django sigue sin aparecer | El venv no estaba activo cuando corriste `pip install`: se instaló en el Python del sistema, no en el del proyecto | Activa el venv (paso 2) **antes** de cualquier `pip install` |

**Regla de oro**: antes de escribir `pip install` o `python manage.py` cualquier cosa,
mira el prompt. Si no dice `(.venv)` al inicio, actívalo primero.

---

## Resumen ultra-rápido (una vez que ya sabes que todo funciona)

```cmd
cd "D:\Profesor\Cursos\2026-2\Desarrollo de Aplicaciones Empresariales\DjangoInicial"
.venv\Scripts\activate.bat
cd django_project\src
python manage.py runserver
```