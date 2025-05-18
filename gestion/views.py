from django.shortcuts import render, get_object_or_404, redirect
from .models import Empleado, Proyecto
from .forms  import EmpleadoForm, ProyectoForm

# — Empleados —
def lista_empleados(request):
    datos = Empleado.objects.all()
    return render(request, 'gestion/empleado_list.html', {'datos': datos})

def crear_empleado(request):
    form = EmpleadoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('empleado_list')
    return render(request, 'gestion/empleado_form.html', {'form': form})

def editar_empleado(request, pk):
    obj  = get_object_or_404(Empleado, pk=pk)
    form = EmpleadoForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('empleado_list')
    return render(request, 'gestion/empleado_form.html', {'form': form})

def borrar_empleado(request, pk):
    obj = get_object_or_404(Empleado, pk=pk)
    if request.method=='POST':
        obj.delete()
        return redirect('empleado_list')
    return render(request, 'gestion/empleado_confirm_delete.html', {'obj': obj})

# — Proyectos —
def lista_proyectos(request):
    datos = Proyecto.objects.select_related('empleado').all()
    return render(request, 'gestion/proyecto_list.html', {'datos': datos})

def crear_proyecto(request):
    form = ProyectoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('proyecto_list')
    return render(request, 'gestion/proyecto_form.html', {'form': form})

def editar_proyecto(request, pk):
    obj  = get_object_or_404(Proyecto, pk=pk)
    form = ProyectoForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('proyecto_list')
    return render(request, 'gestion/proyecto_form.html', {'form': form})

def borrar_proyecto(request, pk):
    obj = get_object_or_404(Proyecto, pk=pk)
    if request.method=='POST':
        obj.delete()
        return redirect('proyecto_list')
    return render(request, 'gestion/proyecto_confirm_delete.html', {'obj': obj})
