from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_invoice, name='generate_invoice'),
    path('success/', views.success_view, name='success')
]
