# /parcial_delivery/patrones/decorator/impl/costo_base.py
from parcial_delivery.patrones.decorator.i_costo import ICosto
from parcial_delivery.entidades.pedidos.pedido import Pedido

class CostoBasePedido(ICosto):
    """
    El 'Componente Concreto'. Es el objeto base que será envuelto.
    Representa el costo inicial de los items del pedido.
    """
    def __init__(self, pedido: Pedido):
        self._pedido = pedido

    def get_costo(self) -> float:
        # Devuelve el costo base guardado en la entidad Pedido
        return self._pedido.costo_base
    
    def get_descripcion(self) -> str:
        return "Costo base de items"
    