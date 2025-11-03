# /parcial_delivery/servicios/pedidos/servicio_pedidos.py
from typing import List, Optional
from parcial_delivery.entidades.pedidos.pedido import Pedido
# ¡NUEVA IMPORTACIÓN!
from parcial_delivery.patrones.observer.observer import IObservador

class ServicioPedidos:
    """
    Capa Controlador (Servicio de Dominio).
    Maneja la lógica de negocio para operar con Pedidos.
    """
    
    def __init__(self):
        print("ServicioPedidos inicializado.")
        self._pedidos: List[Pedido] = []
        self._proximo_id = 101

    def crear_pedido(self, cliente: str, items: List[str], costo_base: float) -> Pedido:
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

    # ... (los métodos avanzar_estado_pedido, cancelar_pedido, get_estado_pedido se mantienen igual) ...
    def avanzar_estado_pedido(self, id_pedido: int):
        pedido = self._buscar_pedido(id_pedido)
        if pedido:
            print(f"SERVICIO: Avanzando estado del pedido {id_pedido}...")
            pedido.avanzar()
        else:
            print(f"SERVICIO: ERROR - Pedido {id_pedido} no encontrado.")

    def cancelar_pedido(self, id_pedido: int):
        pedido = self._buscar_pedido(id_pedido)
        if pedido:
            print(f"SERVICIO: Intentando cancelar pedido {id_pedido}...")
            pedido.cancelar()
        else:
            print(f"SERVICIO: ERROR - Pedido {id_pedido} no encontrado.")

    def get_estado_pedido(self, id_pedido: int) -> str:
        pedido = self._buscar_pedido(id_pedido)
        if pedido:
            return pedido.get_estado()
        return "No encontrado"

    # --- ¡NUEVO MÉTODO PARA OBSERVER! ---
    def suscribir_a_pedido(self, id_pedido: int, observador: IObservador):
        """
        (Controlador) Conecta un Observador a un Pedido (Sujeto).
        """
        pedido = self._buscar_pedido(id_pedido)
        if pedido:
            print(f"SERVICIO: Suscribiendo observador al pedido {id_pedido}.")
            # El Controlador le habla al Modelo (Pedido) para suscribir
            pedido.suscribir(observador)
        else:
            print(f"SERVICIO: ERROR - Pedido {id_pedido} no encontrado.")
    # -----------------------------------

    def _buscar_pedido(self, id_pedido: int) -> Optional[Pedido]:
        """Helper interno para encontrar un pedido."""
        for p in self._pedidos:
            if p.id_pedido == id_pedido:
                return p
        return None