# Cap-Python

## Nivel Intermedio
### Laboratorio 1
 * Para la ejecución de sebe estar dentro de la ruta ***/src/intermediate-level/lab01***
 * Comando para la ejecución del Laboratorio: `poetry run python -m app.main`<br/>
> [!NOTE]
> El laboratorio cuenta con una conexión a SQL Server adjunto la base de datos para restaurarla.
> solo se debe modificar la cadena de conexón para poder completar el flujo.

### Laboratorio 2 (Módulo. APIs web con FastAPI (Automatización))
 * Para la ejecución de sebe estar dentro de la ruta <sup>/src/intermediate-level/lab02</sup>
 1. Levantar el API con el comando: `poetry run uvicorn app.main:app --reload`<br/>
 2. URL´s de validación de la documentación<br/> 
    -[http://127.0.0.1:8000/](http://127.0.0.1:8000/)  --> solo muestra la respuesta de que el API responde<br/>
    -[http://127.0.0.1:8000/docs#](http://127.0.0.1:8000/docs#)   --> muestra el swagger<br/>
>[!IMPORTANT]
> La base de datos de este laboratorio esta generada y cargada en el repositorio.