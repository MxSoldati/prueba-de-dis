# /parcial_delivery/servicios/pedidos/servicio_pedidos.py
from typing import List
from parcial_delivery.entidades.pedidos.pedido import Pedido

class ServicioPedidos:
    """
    Capa Controlador (Servicio de Dominio).
    Maneja la lógica de negocio para operar con Pedidos.
    """
    
    def __init__(self):
        print("ServicioPedidos inicializado.")
        # (Usaremos una lista en memoria como 'base de datos' temporal)
        self._pedidos: List[Pedido] = []
        self._proximo_id = 101

    def crear_pedido(self, cliente: str, items: List[str], costo_base: float) -> Pedido:
        """
        Lógica de negocio para crear un pedido.
        """
        print(f"\nSERVICIO: Recibida orden para crear pedido para {cliente}.")
        
        nuevo_pedido = Pedido(
            id_pedido=self._proximo_id,
            cliente=cliente,
            items=items,
            costo_base=costo_base
        )
        self._proximo_id += 1
        self._pedidos.append(nuevo_pedido)
        
        print(f"SERVICIO: Pedido {nuevo_pedido.id_pedido} creado.")
        return nuevo_pedido

    def _buscar_pedido(self, id_pedido: int) -> Optional[Pedido]:
        """Helper interno para encontrar un pedido."""
        for p in self._pedidos:
            if p.id_pedido == id_pedido:
                return p
        return None