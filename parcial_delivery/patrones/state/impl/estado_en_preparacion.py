# /parcial_delivery/patrones/state/impl/estado_en_preparacion.py
from parcial_delivery.patrones.state.i_estado_pedido import IEstadoPedido
from typing import TYPE_CHECKING

# (Importaríamos el siguiente estado, ej. EstadoEnCamino)
# from .estado_en_camino import EstadoEnCamino 

if TYPE_CHECKING:
    from parcial_delivery.entidades.pedidos.pedido import Pedido

class EstadoEnPreparacion(IEstadoPedido):
    """
    Implementación del estado 'En Preparación'.
    """
    
    def __init__(self, pedido_contexto: 'Pedido'):
        super().__init__(pedido_contexto)

    def get_nombre_estado(self) -> str:
        return "En Preparación"

    def avanzar_estado(self):
        """
        Lógica para avanzar: El restaurante termina de preparar.
        Pasa de 'En Preparación' a 'En Camino' (o 'Listo para Recoger').
        """
        print(f"ACCIÓN: El pedido {self._pedido.id_pedido} está listo y salió para entrega.")
        # self._pedido.transicionar_a(EstadoEnCamino(self._pedido))
        print("... (Transicionando a 'En Camino') ...")


    def cancelar_pedido(self):
        """
        Lógica para cancelar: ¡NO SE PUEDE! (HU-1)
        Un pedido que ya se está preparando no se puede cancelar.
        Aquí es donde el patrón brilla.
        """
        print(f"ERROR: No se puede cancelar el pedido {self._pedido.id_pedido}, ¡ya está en preparación!")