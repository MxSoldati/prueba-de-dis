# /parcial_delivery/notificaciones/notificador_cliente.py
from parcial_delivery.patrones.observer.observer import IObservador
from parcial_delivery.entidades.pedidos.pedido import Pedido

class NotificadorCliente(IObservador):
    """
    Este es un Observador Concreto.
    Su trabajo es "escuchar" los eventos del Pedido y simular
    el envío de una notificación al cliente.
    """
    
    def __init__(self, cliente_telefono: str):
        self._telefono = cliente_telefono

    def actualizar(self, evento: str, datos: Pedido):
        """
        Esta es la acción que el Sujeto (Pedido) llamará.
        """
        if evento == "CAMBIO_ESTADO":
            # Filtramos el evento que nos interesa
            id_pedido = datos.id_pedido
            nuevo_estado = datos.get_estado()
            
            # Simulamos el envío de la notificación
            print(f"--- [NOTIFICADOR CLIENTE] ---")
            print(f"    Simulando envío de SMS al {self._telefono}:")
            print(f"    'Tu pedido {id_pedido} ha cambiado de estado a: {nuevo_estado}'")
            print(f"--- [FIN NOTIFICADOR] ---")