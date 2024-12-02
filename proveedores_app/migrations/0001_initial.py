# Generated by Django 5.1.2 on 2024-12-02 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('idProveedores', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=50)),
                ('tipoProducto', models.CharField(max_length=30)),
                ('paisOrigen', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('codigoPostal', models.CharField(max_length=50)),
            ],
        ),
    ]
