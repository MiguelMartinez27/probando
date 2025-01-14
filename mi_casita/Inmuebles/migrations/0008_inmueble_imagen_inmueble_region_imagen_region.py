# Generated by Django 5.1.3 on 2024-11-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inmuebles', '0007_alter_region_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='imagen_inmueble',
            field=models.ImageField(blank=True, null=True, upload_to='media/inmuebles'),
        ),
        migrations.AddField(
            model_name='region',
            name='imagen_region',
            field=models.ImageField(default='arica.jpg', upload_to='media/regiones'),
        ),
    ]
