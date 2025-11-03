# /parcial_delivery/excepciones/pedido_exception.py
from .delivery_exception import DeliveryException

class PedidoCancelacionException(DeliveryException):
    """
    Lanzada específicamente cuando se intenta cancelar un pedido
    en un estado que no lo permite (ej. 'En Preparación').
    """
    pass