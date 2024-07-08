# Infracciones 

## Descripción
Este proyecto es una aplicación web que permite crear y visualizar infracciones de tránsito.

## Requerimientos
Para su comodidad usar docker y docker-compose para la instalación de los requerimientos.
- docker
- docker-compose

## Instalación en local
1. Clonar el repositorio
2. Ejecutar el comando `docker compose -f local.yml up --build` para generar las images y levantar los contenedores
3. Ejecutar el comando `docker compose -f local.yml run --rm django python manage.py migrate` para aplicar las migraciones
4. Ejecutar el comando `docker compose -f local.yml run --rm  django python manage.py createsuperuser` para crear un super usuario
5. Ingresar a la url `http://localhost:8000` para visualizar el API

## Test
Para ejecutar los test unitarios, ejecute el comando `docker compose -f local.yml run --rm django pytest`

