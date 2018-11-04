# Generated by Django 2.1.2 on 2018-10-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rut', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=30)),
                ('Correo', models.CharField(max_length=50)),
                ('Telefono', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
