# Infracciones 

## Descripción
Este proyecto es una aplicación web que permite crear y visualizar infracciones de tránsito.

## Requerimientos
Para su comodidad usar docker y docker-compose para la instalación de los requerimientos. Esto hará toda la magia.
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

## Frontend
Para visualizar el frontend, ingrese a la url `http://localhost:3000/`

## Documentación para el flujo de trabajo
Para visualizar la documentación de la API, ingrese a la url `http://localhost:8000/`

1.- Crear un super usuario usando el comando antes mencionado, esto creara un usuario (oficial) que podrá crear infracciones.

### Flujo frontend
El oficial (superadmin) una vez creado podrá acceder al sistema desde la url `http://localhost:3000/` y loguearse con el usuario creado. Esto creara un token que se guardara en el localstorage del navegador y permitirá al oficial acceder a la creación de datos.

#### Personas
El oficial logeado puede crear personas usando el botón "Agregar nueva persona" podrá verla en el listado de manera inmediata. Una vez creada la persona podrá editarla usando un modal ó eliminarla.

#### Autos
El oficial logeado puede crear vehículos usando el link "Ver autos" si el usuario cuenta con autos podrá verlos en el listado. Si no existe autos podrá crear uno usando el botón "Agregar auto" que pedirá los datos en un modal una vez agregado podrá verlo en el listado de manera inmediata. Una vez creado el auto podrá editarlo usando un modal ó eliminarlo.

#### Infracciones
Una vez creado un automóvil, el oficial podrá crear infracciones usando el link "Infracciones" si el usuario cuenta con infracciones podrá verlas en el listado. Si no existe infracciones podrá crear una usando el botón "Agregar infracción" que pedirá los datos en un modal una vez agregada podrá verla en el listado de manera inmediata. Las infracciones no se pueden editar ni eliminar.

### Buscar infracciones por email 
El oficial podrá buscar infracciones desde el dashboard usando el campo de búsqueda, si el email existe en la base de datos se mostrarán las infracciones asociadas a ese email.

## Frontend url libre 
El frontend se encuentra en la url `http://localhost:3000/infrigments` y no requiere autenticación para su uso. Esta pagina tiene el mismo comportamiento que buscar Infracciones por email que se encuentra en el dashboard.
