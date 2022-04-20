from django.db import models

class contacto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100,verbose_name='Nombre',null=True)
    direccion=models.CharField(max_length=100,verbose_name='Direccion',null=True)
    telefono=models.CharField(max_length=100,verbose_name='Telefono',null=True)
    correo=models.CharField(max_length=100,verbose_name='Correo',null=True)
    imagen=models.ImageField(upload_to='imagenes/',verbose_name='Imagen',null=True)
    
