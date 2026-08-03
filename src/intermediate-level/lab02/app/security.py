from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext

# ============================================
# Configuración JWT
# ============================================

SECRET_KEY = "mi_clave_super_secreta_para_laboratorio"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto para hash de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ============================================
# Hash de contraseña
# ============================================


def hash_password(password: str) -> str:
    """
    Genera el hash de una contraseña.
    """
    return pwd_context.hash(password)


# ============================================
# Verificación de contraseña
# ============================================


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica que una contraseña coincida con su hash.
    """
    return pwd_context.verify(plain_password, hashed_password)


# ============================================
# Crear JWT
# ============================================


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Genera un token JWT.
    """

    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# ============================================
# Decodificar JWT
# ============================================


def decode_token(token: str):
    """
    Decodifica un JWT y devuelve su contenido.
    """

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return payload

    except JWTError:
        return None
