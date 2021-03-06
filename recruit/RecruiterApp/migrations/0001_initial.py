# Generated by Django 4.0.1 on 2022-02-22 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=30)),
                ('nombre_manager', models.CharField(max_length=30)),
                ('telefono', models.FloatField(default=0)),
                ('email', models.EmailField(default='', max_length=30)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='nombre', max_length=30, null=True)),
                ('apellido', models.CharField(default='apellido', max_length=30, null=True)),
                ('direccion', models.CharField(default='direccion', max_length=30, null=True)),
                ('email', models.EmailField(default='email', max_length=30)),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RecruiterApp.empresas')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Puestos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_puesto', models.CharField(max_length=30)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('fecha_validacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudDePosicion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_de_carga', models.DateTimeField(auto_now_add=True, null=True)),
                ('estado', models.CharField(choices=[('Aprobado', 'Aprobado'), ('Esperando', 'Esperando'), ('Denegado', 'Denegado')], default='Esperando', max_length=30)),
                ('etapa', models.CharField(choices=[('Administracion', 'Administracion'), ('Aprobacion', 'Aprobacion'), ('Entrevista', 'Entrevista'), ('Ingresado', 'Ingresado'), ('Descartado', 'Descartado')], default='Aprobacion', max_length=30, null=True)),
                ('seniority', models.CharField(choices=[('Junior', 'Junior'), ('Semi Senior', 'Semi Senior'), ('Senior', 'Senior'), ('Gerente', 'Gerente')], max_length=30, null=True)),
                ('nota', models.TextField(default='Escriba informaci??n breve de utilidad en torno a la posici??n', max_length=300)),
                ('cargar_archivos', models.FileField(blank=True, null=True, upload_to='media/')),
                ('nombre', models.CharField(default='nombre', max_length=30, null=True)),
                ('apellido', models.CharField(default='apellido', max_length=30, null=True)),
                ('direccion', models.CharField(default='direccion', max_length=30, null=True)),
                ('email', models.EmailField(default='email@mail.com', max_length=30, null=True)),
                ('empresas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RecruiterApp.empresas')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RecruiterApp.managers')),
                ('puesto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RecruiterApp.puestos')),
            ],
        ),
    ]
