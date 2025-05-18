from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # Redirige "/" a "/empleados/"
    path('', RedirectView.as_view(pattern_name='empleado_list', permanent=False)),

    # Empleados
    path('empleados/',        views.lista_empleados,    name='empleado_list'),
    path('empleados/nuevo/',  views.crear_empleado,     name='empleado_new'),
    path('empleados/edita/<int:pk>/', views.editar_empleado,  name='empleado_edit'),
    path('empleados/borra/<int:pk>/', views.borrar_empleado, name='empleado_delete'),

    # Proyectos
    path('proyectos/',        views.lista_proyectos,    name='proyecto_list'),
    path('proyectos/nuevo/',  views.crear_proyecto,     name='proyecto_new'),
    path('proyectos/edita/<int:pk>/', views.editar_proyecto,  name='proyecto_edit'),
    path('proyectos/borra/<int:pk>/', views.borrar_proyecto, name='proyecto_delete'),
]
