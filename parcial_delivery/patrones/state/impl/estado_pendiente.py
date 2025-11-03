# /parcial_delivery/patrones/state/impl/estado_pendiente.py
from parcial_delivery.patrones.state.i_estado_pedido import IEstadoPedido
from typing import TYPE_CHECKING

# Importamos el *siguiente* estado al que podemos avanzar
from .estado_en_preparacion import EstadoEnPreparacion
# (También podríamos importar un EstadoCancelado)

if TYPE_CHECKING:
    from parcial_delivery.entidades.pedidos.pedido import Pedido

class EstadoPendiente(IEstadoPedido):
    """
    Implementación del estado 'Pendiente'.
    Este es el primer estado de un pedido cuando se crea.
    """
    
    def __init__(self, pedido_contexto: 'Pedido'):
        super().__init__(pedido_contexto)

    def get_nombre_estado(self) -> str:
        return "Pendiente de Aprobación"

    def avanzar_estado(self):
        """
        Lógica para avanzar: El restaurante acepta el pedido.
        Pasa de 'Pendiente' a 'En Preparación'.
        """
        print(f"ACCIÓN: El restaurante aprobó el pedido {self._pedido.id_pedido}.")
        # El estado mismo le dice al pedido (contexto) que transicione
        self._pedido.transicionar_a(EstadoEnPreparacion(self._pedido))

    def cancelar_pedido(self):
        """
        Lógica para cancelar: ¡SÍ SE PUEDE! (HU-1)
        Un pedido pendiente puede ser cancelado.
        """
        print(f"ACCIÓN: El cliente canceló el pedido {self._pedido.id_pedido} (estaba pendiente).")
        # (Aquí transicionaríamos a un 'EstadoCancelado' si lo tuviéramos)
        print("... (Pedido marcado como cancelado) ...")