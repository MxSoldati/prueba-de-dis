# /parcial_delivery/servicios/pedidos/servicio_pedidos.py
from typing import List, Optional
from parcial_delivery.entidades.pedidos.pedido import Pedido
from parcial_delivery.patrones.observer.observer import IObservador
# --- ¡NUEVA IMPORTACIÓN! ---
from parcial_delivery.entidades.usuarios.cliente import Cliente

class ServicioPedidos:
    # ... (el __init__ queda igual) ...
    def __init__(self):
        print("ServicioPedidos inicializado.")
        self._pedidos: List[Pedido] = []
        self._proximo_id = 101

    # --- ¡MÉTODO MODIFICADO! ---
    def crear_pedido(self, cliente: Cliente, items: List[str], costo_base: float) -> Pedido:
        """
        Lógica de negocio para crear un pedido.
        AHORA RECIBE UN OBJETO Cliente.
        """
        print(f"\nSERVICIO: Recibida orden para crear pedido para Cliente {cliente.id_usuario} ({cliente.nombre}).")
        
        nuevo_pedido = Pedido(
            id_pedido=self._proximo_id,
            # Almacenamos el ID del cliente o el objeto entero
            cliente=f"Cliente ID {cliente.id_usuario}", 
            items=items,
            costo_base=costo_base
        )
        self._proximo_id += 1
        self._pedidos.append(nuevo_pedido)
        
        print(f"SERVICIO: Pedido {nuevo_pedido.id_pedido} creado.")
        return nuevo_pedido
    
    # ... (el resto de métodos: avanzar_estado_pedido, cancelar_pedido, etc. quedan igual) ...
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

    def suscribir_a_pedido(self, id_pedido: int, observador: IObservador):
        pedido = self._buscar_pedido(id_pedido)
        if pedido:
            print(f"SERVICIO: Suscribiendo observador al pedido {id_pedido}.")
            pedido.suscribir(observador)
        else:
            print(f"SERVICIO: ERROR - Pedido {id_pedido} no encontrado.")

    def _buscar_pedido(self, id_pedido: int) -> Optional[Pedido]:
        for p in self._pedidos:
            if p.id_pedido == id_pedido:
                return p
        return None