from django.shortcuts import redirect, render

from .forms import ComponentForm
from .models import COMPONENTS


def component_list(request):
    return render(request, 'Semana2/component_list.html', {'components': COMPONENTS})


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

    return render(request, 'Semana2/component_form.html', {'form': form})
