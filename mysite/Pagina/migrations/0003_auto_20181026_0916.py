# Generated by Django 2.1.2 on 2018-10-26 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0002_auto_20181026_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='Rut',
            field=models.CharField(max_length=12),
        ),
    ]
