from app.database import Base, engine
from app.middleware import configure_middleware
from app.routers import auth, orders
from fastapi import FastAPI

# ============================================
# Crear tablas en la Base de Datos
# ============================================

Base.metadata.create_all(bind=engine)

# ============================================
# Crear aplicación FastAPI
# ============================================

app = FastAPI(
    title="Orders API",
    version="1.0",
    description="Laboratorio FastAPI",
)

# ============================================
# Configurar Middlewares
# ============================================

configure_middleware(app)

# ============================================
# Registrar Routers
# ============================================

app.include_router(auth.router)
app.include_router(orders.router)

# ============================================
# Endpoint raíz
# ============================================


@app.get("/", tags=["Home"])
def home():
    return {"message": "Bienvenido a Orders API", "docs": "/docs", "redoc": "/redoc"}
