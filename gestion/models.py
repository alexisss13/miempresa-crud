from django.db import models

class Empleado(models.Model):
    nombre  = models.CharField(max_length=100)
    cargo   = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    foto    = models.ImageField(upload_to='empleados/')

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    empleado    = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='proyectos')
    nombre      = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado      = models.CharField(max_length=20, choices=[
        ('PENDIENTE','Pendiente'),
        ('EN_CURSO','En curso'),
        ('FINALIZADO','Finalizado'),
    ])
    imagen      = models.ImageField(upload_to='proyectos/')

    def __str__(self):
        return self.nombre
