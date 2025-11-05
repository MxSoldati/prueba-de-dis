"""
Archivo integrador generado automaticamente
Directorio: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/pedidos
Fecha: 2025-11-03 20:15:08
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/pedidos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: pedido.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/pedidos/pedido.py
# ================================================================================

# /parcial_delivery/entidades/pedidos/pedido.py
from dataclasses import dataclass, field
from typing import Optional, List, Tuple # ¡Añadir Tuple!

# ... (importaciones de State y Observer) ...
from parcial_delivery.patrones.state.i_estado_pedido import IEstadoPedido
from parcial_delivery.patrones.state.impl.estado_pendiente import EstadoPendiente
from parcial_delivery.patrones.observer.observable import Observable

@dataclass
class Pedido(Observable): 
    # ... (atributos id_pedido, cliente, items, costo_base) ...
    id_pedido: int
    cliente: str 
    items: List[str]
    costo_base: float
    
    # --- NUEVO CAMPO PARA PATRÓN STRATEGY ---
    ubicacion_restaurante: Tuple[int, int] = field(default=(0, 0))
    # ----------------------------------------
    
    estado_actual: Optional[IEstadoPedido] = field(init=False, repr=False, default=None)

    # ... (el resto de la clase: __post_init__, transicionar_a, etc. quedan igual) ...
    def __post_init__(self):
        Observable.__init__(self) 
        if self.estado_actual is None:
            self.transicionar_a(EstadoPendiente(self))

    def transicionar_a(self, nuevo_estado: IEstadoPedido):
        nombre_estado = "desconocido"
        if nuevo_estado:
            nombre_estado = nuevo_estado.get_nombre_estado()
        print(f"PEDIDO {self.id_pedido}: Transicionando a -> {nombre_estado}")
        self.estado_actual = nuevo_estado
        self.notificar(evento="CAMBIO_ESTADO", datos=self)

    def avanzar(self):
        self.estado_actual.avanzar_estado()

    def cancelar(self):
        self.estado_actual.cancelar_pedido()

    def get_estado(self) -> str:
        return self.estado_actual.get_nombre_estado()

