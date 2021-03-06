# Recruiter IT

_Peque帽o proyecto a煤n en desarrollo que permite sistematizar el ingreso de postulantes a una empresa_

## Comenzando 馃殌

_Estas instrucciones te permitir谩n obtener una copia del proyecto en funcionamiento en tu m谩quina local para prop贸sitos de desarrollo y/o pruebas._


### Pre-requisitos 馃搵

```
No es excluyente pero el sistema s贸lo fu茅 probado en Ubuntu 20.4 LTS. Instalando requeriments.txt no deber铆a haber problemas de compatibilidades
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

### Instalaci贸n 馃敡

_Tomaremos como base la instalaci贸n en un sistema Ubuntu, ya que es el 煤nico lugar d贸nde el sistema ha sido probado.
Si tiene Windows u otro sistema le recomendamos utilizar una m谩quina virtual o bien adecuar los pasos al sistema operativo de su elecci贸n _

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

_Descargar el repositorio dentro de la carpeta creada en el paso anterior.

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

_Lo siguiente es crear una base de datos en Postgres y utilizar esa informaci贸n para modificar la conexi贸n con la base de datos desde Django_
```
 Dentro del archivo settings.py ubicado en RecruiterApp configurar la conexi贸n con la base de datos de nuestra preferencia, para mayor informaci贸n consultar la documentaci贸n de Django
```
[Django](https://docs.djangoproject.com/en/4.0/ref/databases/) - Docuementaci贸n relacionada a la conexi贸n con la base de datos.



## Ejecutando las pruebas 鈿欙笍

_Cualquiera es libre de hacer o deshacer *dentro de su propio sistema*, el proyecto a煤n est谩 en fase de desarrollo_



## Construido con 馃洜锔?

_Algunas herramientas_

* [Django](https://docs.djangoproject.com/) - Django
* [Apexcharts](https://apexcharts.com/) - Apexcharts
* [Bootstrap](https://getbootstrap.com/) - Boostrap
* [Postgres](https://www.postgresql.org/download/) - Postgres

## Contribuyendo 馃枃锔?

_De momento no est谩n aceptadas_

## Wiki 馃摉

No wiki YET.



## Autores 鉁掞笍

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Gast贸n Cejas** - *Trabajo Inicial* - [gastonc90](https://github.com/gastonc90/)
* **Gast贸n Cejas** - *Documentaci贸n* - [gastonc90](https://github.com/gastonc90/)
