# Generated by Django 4.2.5 on 2023-09-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tabla_load',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=150)),
                ('imagenUrl', models.CharField(max_length=150)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ispaypal', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Tabla info Lentes',
                'db_table': 'Lentes',
            },
        ),
    ]
