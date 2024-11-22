from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('detalle/<id_auto>/', views.vista_detalle, name='detalle_auto')
]