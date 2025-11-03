# /parcial_delivery/entidades/pedidos/pedido.py
from dataclasses import dataclass, field
from typing import Optional, List

# --- Importaciones del Patrón State ---
from parcial_delivery.patrones.state.i_estado_pedido import IEstadoPedido
from parcial_delivery.patrones.state.impl.estado_pendiente import EstadoPendiente

# --- ¡NUEVAS Importaciones del Patrón Observer! ---
from parcial_delivery.patrones.observer.observable import Observable
# --------------------------------------------------

@dataclass
class Pedido(Observable): # <-- ¡AHORA HEREDA DE OBSERVABLE!
    """
    La entidad principal. Actúa como:
    1. Contexto (para el Patrón State)
    2. Sujeto (para el Patrón Observer)
    """
    id_pedido: int
    cliente: str 
    items: List[str]
    costo_base: float
    
    estado_actual: Optional[IEstadoPedido] = field(init=False, repr=False, default=None)

    def __post_init__(self):
        """
        Se ejecuta después del __init__ de @dataclass.
        """
        # Inicializa el 'Observable' (el Sujeto)
        Observable.__init__(self) 
        
        # Asigna el estado inicial
        if self.estado_actual is None:
            self.transicionar_a(EstadoPendiente(self))

    # --- Métodos del Patrón State ---
    
    def transicionar_a(self, nuevo_estado: IEstadoPedido):
        """
        El método central que permite al Pedido (Contexto) cambiar de estado.
        """
        nombre_estado = "desconocido"
        if nuevo_estado:
            nombre_estado = nuevo_estado.get_nombre_estado()
            
        print(f"PEDIDO {self.id_pedido}: Transicionando a -> {nombre_estado}")
        self.estado_actual = nuevo_estado
        
        # --- ¡MAGIA DEL OBSERVER! ---
        # Notifica a todos los suscriptores sobre este cambio de estado.
        self.notificar(evento="CAMBIO_ESTADO", datos=self)
        # -----------------------------

    def avanzar(self):
        self.estado_actual.avanzar_estado()

    def cancelar(self):
        self.estado_actual.cancelar_pedido()

    def get_estado(self) -> str:
        return self.estado_actual.get_nombre_estado()