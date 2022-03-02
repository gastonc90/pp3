# Recruiter IT

_Pequeño proyecto aún en desarrollo que permite sistematizar el ingreso de postulantes a una empresa_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y/o pruebas._


### Pre-requisitos 📋

```
No es excluyente pero el sistema sólo fué probado en Ubuntu 20.4 LTS. Instalando requeriments.txt no debería haber problemas de compatibilidades
```
```
Python 3.8.10
```
```
Virtualenv 20.0.17
```
```
Pip3 
```
```
Postgres 6.4 o superior
```

### Instalación 🔧

_Tomaremos como base la instalación en un sistema Ubuntu, ya que es el único lugar dónde el sistema ha sido probado.
Si tiene Windows u otro sistema le recomendamos utilizar una máquina virtual o bien adecuar los pasos al sistema operativo de su elección _

_Crear una carpeta para el proyecto _

```
$ mkdir recruiter
```

_Crear un entorno virtual dentro de la carpeta seleccionada_

```
$ cd recruiter 
```

```
recruiter $ virtualenv 'nombre del entorno'
```

_Descargar el repositorio dentro de la carpeta creada en el paso anterior. Dejar únicamente la carpeta "recruit" eliminando el resto.

```
recruiter/nombredelentorno $ git clone https://github.com/gastonc90/pp3/
```
_Activar el entorno virtual_

```
recruiter/nombredelentorno$ source bin/activate
```

_Instalar requeriments.txt_

```
(nombredelentorno)recruiter/nombredelentorno$ pip3 install -r requirements.txt
```

_Iniciar el servidor desde la carpeta descargada del repositorio_

```
(nombredelentorno)recruiter/nombredelentorno/recruit$ python3 manage.py runserver
```

_Lo siguiente es crear una base de datos en Postgres y utilizar esa información para modificar la conexión con la base de datos desde Django_
```
 Dentro del archivo settings.py ubicado en RecruiterApp configurar la conexión con la base de datos de nuestra preferencia, para mayor información consultar la documentación de Django
```
[Django](https://docs.djangoproject.com/en/4.0/ref/databases/) - Docuementación relacionada a la conexión con la base de datos.



## Ejecutando las pruebas ⚙️

_Cualquiera es libre de hacer o deshacer *dentro de su propio sistema*, el proyecto aún está en fase de desarrollo_



## Construido con 🛠️

_Algunas herramientas_

* [Django](https://docs.djangoproject.com/) - Django
* [Apexcharts](https://apexcharts.com/) - Apexcharts
* [Bootstrap](https://getbootstrap.com/) - Boostrap
* [Postgres](https://www.postgresql.org/download/) - Postgres

## Contribuyendo 🖇️

_De momento no están aceptadas_

## Wiki 📖

No wiki YET.



## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Gastón Cejas** - *Trabajo Inicial* - [gastonc90](https://github.com/gastonc90/)
* **Gastón Cejas** - *Documentación* - [gastonc90](https://github.com/gastonc90/)
