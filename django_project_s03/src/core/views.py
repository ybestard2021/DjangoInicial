from django.shortcuts import render

from .models import Item


def item_list(request):
    # Semana 2 usaba Item.objects.all() (todos los registros, sin orden
    # explícito). Aquí aplicamos un QuerySet distinto -order_by("-created_at")-
    # para mostrar que se puede cambiar la consulta ORM sin tocar el Template.
    items = Item.objects.order_by('-created_at')
    return render(request, 'core/item_list.html', {'items': items})
