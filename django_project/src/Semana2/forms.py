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
