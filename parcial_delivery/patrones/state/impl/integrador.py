"""
Archivo integrador generado automaticamente
Directorio: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/state/impl
Fecha: 2025-11-03 20:15:08
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/state/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: estado_en_preparacion.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/state/impl/estado_en_preparacion.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: estado_pendiente.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/state/impl/estado_pendiente.py
# ================================================================================

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

