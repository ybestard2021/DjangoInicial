from django.shortcuts import render, redirect

from .models import Item


def item_list(request):
    # Semana 2 usaba Item.objects.all() (todos los registros, sin orden
    # explícito). Aquí aplicamos un QuerySet distinto -order_by("-created_at")-
    # para mostrar que se puede cambiar la consulta ORM sin tocar el Template.
    items = Item.objects.order_by('-created_at')
    return render(request, 'core/item_list.html', {'items': items})


def item_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()

        if not name:
            return render(request, 'core/item_form.html', {
                'error': 'El nombre es obligatorio.',
                'name': name,
                'description': description,
            })

        # ORM: Django convierte esta operación Python en un INSERT SQL
        # que finalmente ejecutará SQLite.
        Item.objects.create(name=name, description=description)

        return redirect('item_list')

    return render(request, 'core/item_form.html')
