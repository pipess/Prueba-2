# Generated by Django 2.1.2 on 2018-10-31 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0011_persona_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='Telefono',
            field=models.IntegerField(),
        ),
    ]
