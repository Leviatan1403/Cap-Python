# Capacitación Python

## Nivel Intermedio
### Laboratorio 1
 >[!IMPORTANT]
 > Para la ejecución de sebe estar dentro de la ruta: ***/src/intermediate-level/lab01***
 * Comando para la ejecución del Laboratorio: `poetry run python -m app.main`<br/>
> [!NOTE]
> El laboratorio cuenta con una conexión a SQL Server adjunto la base de datos para restaurarla.
> solo se debe modificar la cadena de conexón para poder completar el flujo.

### Laboratorio 2 (Módulo. APIs web con FastAPI (Automatización))
 >[!IMPORTANT]
 > Para la ejecución de sebe estar dentro de la ruta: ***/src/intermediate-level/lab02***
 1. Levantar el API con el comando: `poetry run uvicorn app.main:app --reload`<br/>
 2. URL´s de validación de la documentación<br/> 
    -[http://127.0.0.1:8000/](http://127.0.0.1:8000/)  --> solo muestra la respuesta de que el API responde<br/>
    -[http://127.0.0.1:8000/docs#](http://127.0.0.1:8000/docs#)   --> muestra el swagger<br/>
>[!IMPORTANT]
> La base de datos de este laboratorio esta generada y cargada en el repositorio.
### Laboratorio 3 (Módulo. Pruebas y TDD)
>[!IMPORTANT]
> Para la ejecución de sebe estar dentro de la ruta: ***/src/intermediate-level/lab03***
* Para ejecutar las pruebas: `pytest`<br/>
* Para conocer la covertura: `pytest --cov=app`<br/>
* Para generar el reporte HTML: `pytest --cov=app --cov-report=html`<br/>
  La ruta del reporte es la siguiente: `htmlcov/index.html`
### Laboratorio 4 (Módulo. Concurrencia y rendimiento)
>[!IMPORTANT]
> Para la ejecución de sebe estar dentro de la ruta: ***/src/intermediate-level/lab04***
* Ejecutar versión síncrona con: `python main.py`<br/>
* Modificar el semáforo `async def fetch_all(urls, limit=5):` modificando el parametro ***limit***, prueba con:
    - 1
    - 2
    - 5
    - 10

* Ejecuta las pruebas: `pytest`