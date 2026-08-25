Lab02: Investigación, requisitos y desarrollo de una App Django

Desarrollo de Aplicaciones Empresariales — Diseño y Desarrollo de Software

Capacidades Terminales
Identificar y formalizar los requisitos de una problemática real como base para el diseño de una aplicación Django.
Diseñar e implementar una nueva App Django (Model con datos estáticos, View, URL, Template) conectada a un proyecto existente, aplicando el patrón MVT.
Implementar formularios (Forms) que capturen datos y los reflejen en el response, sin depender de una base de datos.
Introducción

En las sesiones anteriores construimos y extendimos el proyecto DjangoInicial, comprendiendo cómo Django organiza una aplicación mediante el patrón MVT: Project, Apps, Models, Views, URLs y Templates. En este laboratorio damos un paso más cercano a cómo se trabaja en un proyecto real: en lugar de partir de un modelo ya definido, van a investigar una problemática real, capturar sus requisitos, y traducir esos requisitos en una aplicación Django funcional, construida como una nueva App conectada al proyecto que ya conocen (config/core).

Para mantener el foco en el flujo MVT y en cómo un formulario transforma datos en un response, esta aplicación no usará base de datos: los datos se definirán de forma estática dentro de models.py (por ejemplo, como una lista de diccionarios), y las vistas leerán y agregarán información directamente sobre esa estructura en memoria, sin migraciones ni panel de administración.

Pueden elegir cualquier problemática cotidiana que se preste a una aplicación sencilla: tienda de barrio, biblioteca, veterinaria, alquiler de equipos, reserva de citas, control de asistencia, u otra que les resulte relevante.

Enunciados

Ejercicio 1 — Investigar una problemática real Investiguen una problemática cotidiana que pueda resolverse con una aplicación web (por ejemplo: tienda de barrio, biblioteca, veterinaria, alquiler de equipos, reserva de citas, control de asistencia, u otra de su interés). Redacten en 3-5 líneas en qué consiste el problema y quién lo usaría.

Ejercicio 2 — Capturar los requisitos A partir de la problemática elegida, listen entre 4 y 6 requisitos funcionales del sistema (ejemplo: "el sistema debe permitir registrar un producto", "el usuario debe poder ver el listado de productos disponibles"). Cada requisito debe redactarse como una acción concreta que el sistema debe permitir.

Ejercicio 3 — Diseñar el modelo de datos A partir de los requisitos del Ejercicio 2, identifiquen la entidad principal de su problemática (por ejemplo: Producto, Libro, Cita, Equipo) y definan sus campos (nombre, tipo de dato y si es obligatorio). Justifiquen brevemente por qué cada campo es necesario según los requisitos capturados.

Ejercicio 4 — Crear la nueva App Dentro del proyecto base (config/core), creen una nueva App con un nombre representativo de su problemática (por ejemplo store, library, bookings). Regístrenla en INSTALLED_APPS.

Ejercicio 5 — Implementar el Model con datos estáticos Traduzcan el diseño del Ejercicio 3 en models.py, definiendo los datos como una lista de diccionarios (o de objetos de una clase simple) con al menos 5 registros de ejemplo. No se usan migraciones ni base de datos: esta lista es la única fuente de datos de la aplicación.

Ejercicio 6 — Implementar el listado (View + URL + Template) Creen una vista que recorra la lista definida en models.py y la muestre en un template que herede de base.html, siguiendo el mismo patrón usado en core.

Ejercicio 7 — Implementar el formulario (Forms) Creen un forms.py con un forms.Form (no ModelForm, ya que no hay modelo de base de datos) cuyos campos correspondan a los requisitos capturados en el Ejercicio 2.

Ejercicio 8 — Implementar la vista de creación Creen una vista que muestre el formulario del Ejercicio 7, procese el envío (POST), valide los datos y agregue el nuevo registro a la lista en memoria definida en models.py. Luego redirijan al listado para confirmar que el nuevo dato aparece. Tengan en cuenta que, al no haber base de datos, los datos agregados se pierden al reiniciar el servidor — esto es esperado y debe mencionarse en su documentación.

Ejercicio 9 — Verificación del flujo completo Naveguen su aplicación de principio a fin (listado → crear → volver al listado con el nuevo dato reflejado) y documenten con capturas el recorrido Request → URL → View → Model (datos estáticos) → Template → Response. Expliquen cómo su nueva App convive con core dentro del mismo Project.

Ejercicio 10 — Publicar en GitHub Actualicen requirements.txt y README.md describiendo su problemática, sus requisitos y la App creada. Hagan commit y push al repositorio del equipo.

Entregables
Documento de requisitos: problemática elegida (Ejercicio 1) y lista de requisitos funcionales (Ejercicio 2).
Diseño del modelo de datos: entidad principal, campos, tipos y justificación (Ejercicio 3).
Código fuente completo de la nueva App: models.py (con los datos estáticos), views.py, urls.py, forms.py y templates (listado y formulario).
Capturas de pantalla del flujo funcionando: listado de registros, formulario de creación, y el nuevo registro reflejado en el listado.
Explicación del flujo MVT aplicado a su caso (Ejercicio 9), incluyendo cómo su App se conecta con core dentro del mismo Project.
Repositorio en GitHub actualizado, con requirements.txt, README.md y el código correspondiente a cada integrante del equipo, según el formato de evidencia indicado en las instrucciones del laboratorio (nombre, título, captura, código, explicación y casos de prueba).