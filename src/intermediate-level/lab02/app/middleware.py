from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def configure_middleware(app: FastAPI) -> None:
    """
    Configura los middlewares de la aplicación.
    """

    app.add_middleware(
        CORSMiddleware,
        # Dominios permitidos
        allow_origins=["*"],
        # Permite el envío de cookies y cabeceras de autenticación
        allow_credentials=True,
        # Métodos HTTP permitidos
        allow_methods=["*"],
        # Cabeceras permitidas
        allow_headers=["*"],
    )
