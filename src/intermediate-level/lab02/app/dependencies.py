from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from .database import SessionLocal
from .security import decode_token

# Endpoint que emite los tokens
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


# ============================================
# Conexión a Base de Datos
# ============================================


def get_db():
    """
    Crea una sesión de base de datos
    y la cierra al finalizar la petición.
    """
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ============================================
# Usuario autenticado
# ============================================


def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Obtiene el usuario a partir
    del JWT enviado en Authorization.
    """

    payload = decode_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    username = payload.get("sub")

    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {"username": username}
