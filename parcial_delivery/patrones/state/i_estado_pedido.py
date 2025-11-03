# /parcial_delivery/patrones/state/i_estado_pedido.py
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# 'TYPE_CHECKING' nos ayuda a evitar un error de "importación circular"
# ya que Pedido (el contexto) y IEstadoPedido se necesitan mutuamente.
if TYPE_CHECKING:
    from parcial_delivery.entidades.pedidos.pedido import Pedido

class IEstadoPedido(ABC):
    """
    La Interfaz (Clase Base Abstracta) para todos los estados de un Pedido.
    Define las acciones que un pedido puede intentar hacer.
    
    Cada estado concreto implementará estas acciones de forma diferente.
    """
    
    def __init__(self, pedido_contexto: 'Pedido'):
        """
        Guarda una referencia de vuelta al Pedido (el contexto) para
        poder cambiar su estado.
        """
        self._pedido = pedido_contexto

    @abstractmethod
    def avanzar_estado(self):
        """Intenta avanzar al siguiente estado del ciclo de vida."""
        pass

    @abstractmethod
    def cancelar_pedido(self):
        """Intenta cancelar el pedido."""
        pass

    @abstractmethod
    def get_nombre_estado(self) -> str:
        """Devuelve el nombre del estado actual."""
        pass