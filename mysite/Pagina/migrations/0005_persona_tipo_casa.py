# Generated by Django 2.1.2 on 2018-10-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0004_perro'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='Tipo_casa',
            field=models.CharField(choices=[('G', 'Patio Grande'), ('P', 'Patio Pequeño'), ('D', 'Departamento'), ('S', 'Sin Patio')], default='R', max_length=1),
        ),
    ]
