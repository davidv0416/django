# Generated by Django 3.2.8 on 2022-04-20 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_auto_20220419_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='correo',
            field=models.CharField(max_length=100, null=True, verbose_name='Correo'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='telefono',
            field=models.CharField(max_length=100, null=True, verbose_name='Telefono'),
        ),
    ]
