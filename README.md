# Biblioteca UdeA

_Se desarrolla un sistema (API) para la atención de préstamos de libros, con esta representación se logra modelar la atención a un usuario y almacenar su servicio histórico de préstamo, la misma cuenta con rutas (endpoints) para crear usuarios, registro y prestamos de libros y un sistema de multas._

## Diagrama 📁

![diagrama](https://user-images.githubusercontent.com/84557725/204821678-6b5cce1f-75dc-4244-8408-ab053143958f.png)


### Instalación y ejecución 🔧

_Se sugiere el uso de un entorno virtual [venv](https://docs.python.org/es/3/tutorial/venv.html)_

_Una vez activado el entorno virtual corremos el siguiente comando para instalar requerimientos:_

```
python -m pip install -r requirements.txt
```

_Abrimos un entorno de python escribiendo _**python**_ o _**python3**_ en la terminal según sea el caso. Con el siguiente comando importamos el script donde se configuran las tablas de la base de datos:_
```python
from app.v1.scripts.create_tables import create_tables
```

_Ahora las creamos ejecutando:_
```python
create_tables()
```

_Cerramos el ambiente de python y en el entorno virtal levantamos el servidor con:_

```
uvicorn main:app --reload
```

_Si todo salió bien, en la ruta *http://localhost:8000/docs* debemos tener lo siguiente:_

![fastapi-doc](https://user-images.githubusercontent.com/84557725/204815970-ab05052a-fd7e-4d92-bf79-867cd1317aef.png)


_Allí encontraremos la documentación de la API y los endpoints disponibles._


## Construido con 🛠️

* [FastApi](https://fastapi.tiangolo.com/) - Usado para sustentar la estructura del proyecto.
* [Postgres](https://www.postgresql.org/docs/) - Usado para almacenar los datos.
* [Peewee](http://docs.peewee-orm.com/en/latest/) - Usado como ORM.
* [Pydantic](https://pydantic-docs.helpmanual.io/) - Usado para validar y tipar los datos.

## Autores ✒️

* **Randolph Peralta** - [RandolphPeralta](https://github.com/RandolphPeralta)
* **Carolina Lopera** - [CarolinaLop](https://github.com/CarolinaLop)
* **Mateo Soto** - [MateoSA99](https://github.com/MateoSA99)
* **Sergio Arbelaez** - [sergio2448](https://github.com/sergio2448)
