# Guía de pruebas del proyecto — DjangoInicial

Este documento sirve para **todas las semanas del curso** (Semana 1 a Semana 16).
Contiene:
1. Los pasos fijos para levantar el proyecto (no cambian de semana a semana).
2. Una sección **"Semana actual"** que debes actualizar cada semana con la app y las
   rutas nuevas que quieras probar.
3. Un prompt listo para pegar en Claude Code (VSCode) que automatiza todo lo anterior.

---

## 🔧 Pasos fijos (siempre iguales)

Desde `django_project/`:

```bash
# 1. Crear el entorno virtual (solo la primera vez)
python -m venv venv

# 2. Activarlo
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

# 3. Instalar dependencias
python -m pip install -r requirements.txt

# 4. Entrar a src/ y migrar (crea/actualiza la base de datos de las apps que la usan)
cd src
python manage.py migrate

# 5. Levantar el servidor
python manage.py runserver
```

Servidor disponible en `http://127.0.0.1:8000/`.

---

## 📅 Semana actual

> Actualiza esta sección cada semana antes de pedirle a Claude Code que pruebe el proyecto.

- **Semana:** 2
- **App nueva de esta semana:** `Semana2` (ejemplo TechParts — catálogo de componentes)
- **Rutas a probar:**
  - `GET /` → listado de `Item` (App `core`, Semana 1)
  - `GET /components/` → listado de componentes (App `Semana2`)
  - `GET /components/nuevo/` → formulario de creación
  - `POST /components/nuevo/` → crea un componente y redirige a `/components/`
- **¿Usa base de datos?** `core` sí (SQLite + migraciones). `Semana2` no (datos estáticos en memoria).
- **Notas:** los componentes creados desde el formulario se pierden al reiniciar el servidor (dato en memoria, no en BD) — esto es esperado.

---

## 🤖 Prompt para Claude Code

Copia y pega esto en Claude Code (VSCode), estando parado en la raíz del repo. Ya usa la
sección **"Semana actual"** de arriba, así que solo actualiza esa sección cada semana y
este mismo prompt te sirve sin cambios:

```
Lee la sección "Semana actual" de TESTING.md en la raíz de este repo para saber qué
app y qué rutas debes probar esta semana. Luego:

1. Crea el entorno virtual si no existe y actívalo.
2. Instala requirements.txt.
3. Entra a src/ y corre las migraciones (python manage.py migrate).
4. Arranca el servidor con runserver en segundo plano.
5. Prueba con curl cada una de las rutas listadas en "Rutas a probar":
   - Para rutas GET: confirma que responden 200 y que el HTML contiene el
     contenido esperado (por ejemplo, el título de la página o algún texto clave).
   - Para rutas POST con formulario: envía datos de prueba válidos según los
     campos del Form/ModelForm correspondiente, confirma que redirige (302) y
     que el registro aparece luego en el listado (GET posterior).
   - Si "¿Usa base de datos?" dice que no, recuerda que los datos son en memoria:
     no esperes que persistan tras reiniciar el servidor.
6. Repórtame en una tabla qué ruta probaste, qué esperabas y qué obtuviste
   (OK / FALLÓ y por qué).
7. Detén el servidor al final.

Si encuentras un error, no lo corrijas automáticamente: dime primero qué
encontraste y espera mi confirmación antes de modificar código.
```

---

## ✅ Pasos manuales (si prefieres probarlo tú mismo en el navegador)

1. Sigue los "Pasos fijos" de arriba hasta tener el servidor corriendo.
2. Abre en el navegador cada ruta listada en "Rutas a probar" de la semana actual.
3. Para las rutas con formulario, completa los campos y confirma que:
   - El envío no muestra errores de validación con datos correctos.
   - Vuelves al listado y ves el nuevo registro reflejado.
4. Si algo no funciona, anota el error exacto (mensaje en el navegador o en la
   terminal donde corre `runserver`) antes de pedir ayuda.

---

## 🗂️ Historial de semanas probadas

> Ve agregando una línea cada semana para llevar registro.

| Semana | App | Resultado | Fecha |
|---|---|---|---|
| 1 | core | ✅ OK | — |
| 2 | Semana2 (TechParts) | — | — |
