# Generated by Django 4.0.1 on 2022-02-22 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecruiterApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicituddeposicion',
            name='resolucion',
            field=models.CharField(choices=[('Ingresado', 'Ingresado'), ('Descartado', 'Descartado')], default='Descartado', max_length=30, null=True),
        ),
    ]
