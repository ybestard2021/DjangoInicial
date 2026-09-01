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
    name = forms.CharField(
        max_length=200, label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES, label="Categoría",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    brand = forms.CharField(
        max_length=100, label="Marca",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    price = forms.DecimalField(
        max_digits=10, decimal_places=2, min_value=0, label="Precio",
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
    )
    stock = forms.IntegerField(
        min_value=0, label="Stock",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
