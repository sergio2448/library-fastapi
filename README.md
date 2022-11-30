# Biblioteca UdeA

_Se desarrolla un sistema (API) para la atención de préstamos de libros, con esta representación se logra modelar la atención a un usuario y almacenar su servicio histórico de préstamo, la misma cuenta con rutas (endpoints) para crear usuarios, registro y prestamos de libros y un sistema de multas._

### Instalación y ejecución 🔧

_Se sugiere el uso de un entorno virtual [venv](https://docs.python.org/es/3/tutorial/venv.html)_

_Una vez activado el entorno virtual corremos el siguiente comando para instalar requerimientos:_

```
python -m pip install -r requirements.txt
```

_Levantamos el servidor con:_

```
uvicorn main:app --reload
```

_Si todo salió bien en la ruta *http://localhost:8000/docs* debemos tener lo siguiente:_

![Screenshot from 2022-11-30 08-59-34](https://user-images.githubusercontent.com/84557725/204815970-ab05052a-fd7e-4d92-bf79-867cd1317aef.png)


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
