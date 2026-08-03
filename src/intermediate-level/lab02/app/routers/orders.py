from typing import List

from app.dependencies import get_current_user, get_db
from app.models import Order
from app.schemas import OrderCreate, OrderResponse, OrderUpdate
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/orders", tags=["Orders"])

# ==================================================
# Obtener todas las órdenes
# ==================================================


@router.get("/", response_model=List[OrderResponse])
def get_orders(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """
    Obtiene todas las órdenes.
    """

    return db.query(Order).all()


# ==================================================
# Obtener una orden por ID
# ==================================================


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    """
    Obtiene una orden por su ID.
    """

    order = db.query(Order).filter(Order.id == order_id).first()

    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Orden no encontrada"
        )

    return order


# ==================================================
# Crear una orden
# ==================================================


@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Crea una nueva orden.
    """

    new_order = Order(
        customer=order.customer,
        product=order.product,
        quantity=order.quantity,
        status="Pending",
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


# ==================================================
# Actualizar una orden
# ==================================================


@router.put("/{order_id}", response_model=OrderResponse)
def update_order(
    order_id: int,
    order_data: OrderUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Actualiza una orden existente.
    """

    order = db.query(Order).filter(Order.id == order_id).first()

    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Orden no encontrada"
        )

    order.customer = order_data.customer
    order.product = order_data.product
    order.quantity = order_data.quantity
    order.status = order_data.status

    db.commit()
    db.refresh(order)

    return order


# ==================================================
# Eliminar una orden
# ==================================================


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(
    order_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    """
    Elimina una orden.
    """

    order = db.query(Order).filter(Order.id == order_id).first()

    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Orden no encontrada"
        )

    db.delete(order)
    db.commit()

    return None
