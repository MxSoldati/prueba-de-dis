# /parcial_delivery/patrones/state/impl/estado_en_preparacion.py
from parcial_delivery.patrones.state.i_estado_pedido import IEstadoPedido
from typing import TYPE_CHECKING
# --- ¡NUEVA IMPORTACIÓN DE EXCEPCIÓN! ---
from parcial_delivery.excepciones.pedido_exception import PedidoCancelacionException

# ... (importación de EstadoEnCamino si la tuvieras) ...

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
        """
        print(f"ACCIÓN: El pedido {self._pedido.id_pedido} está listo y salió para entrega.")
        # self._pedido.transicionar_a(EstadoEnCamino(self._pedido))
        print("... (Transicionando a 'En Camino') ...")


    def cancelar_pedido(self):
        """
        Lógica para cancelar: ¡NO SE PUEDE! (HU-1)
        En lugar de 'print', ahora lanza una excepción.
        """
        # --- ¡CÓDIGO MODIFICADO! ---
        raise PedidoCancelacionException(
            f"No se puede cancelar el pedido {self._pedido.id_pedido}, ¡ya está en preparación!"
        )
        # ---------------------------