# /parcial_delivery/entidades/pedidos/pedido.py
from dataclasses import dataclass, field
from typing import Optional, List
# Aún no podemos importar el estado, ¡primero hay que crearlo!
# from parcial_delivery.patrones.state.i_estado_pedido import IEstadoPedido

@dataclass
class Pedido:
    """
    La entidad principal. Usamos @dataclass (idea de miLombock).
    Delegga el comportamiento a su estado.
    """
    id_pedido: int
    cliente: str # Temporal, luego será un objeto Cliente
    items: List[str]
    costo_base: float
    
    # Referencia al estado (Contexto del Patrón State)
    # estado_actual: Optional[IEstadoPedido] = field(init=False, repr=False, default=None)

    def __post_init__(self):
        """
        Se ejecuta después del __init__ de @dataclass.
        """
        print(f"Entidad Pedido {self.id_pedido} creada en memoria.")
        # Aquí es donde asignaremos el estado inicial
        # if self.estado_actual is None:
        #    self.transicionar_a(EstadoPendiente(self))

    # --- Métodos del Patrón State ---
    
    #def transicionar_a(self, nuevo_estado: IEstadoPedido):
    #    print(f"PEDIDO {self.id_pedido}: Transicionando a -> {nuevo_estado.get_nombre_estado()}")
    #    self.estado_actual = nuevo_estado

    #def avanzar(self):
    #    self.estado_actual.avanzar_estado()

    #def cancelar(self):
    #    self.estado_actual.cancelar_pedido()

    #def get_estado(self) -> str:
    #    return self.estado_actual.get_nombre_estado()