from django.urls import path

from . import views

urlpatterns = [
    path('components/', views.component_list, name='component_list'),
    path('components/nuevo/', views.component_create, name='component_create'),
]
