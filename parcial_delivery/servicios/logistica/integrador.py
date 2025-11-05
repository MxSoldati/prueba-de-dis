"""
Archivo integrador generado automaticamente
Directorio: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/logistica
Fecha: 2025-11-03 20:15:08
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/logistica/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: servicio_logistica.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/logistica/servicio_logistica.py
# ================================================================================

# /parcial_delivery/servicios/logistica/servicio_logistica.py
from typing import List, Optional
from parcial_delivery.patrones.strategy.i_estrategia_asignacion import IEstrategiaAsignacion
from parcial_delivery.entidades.pedidos.pedido import Pedido
from parcial_delivery.entidades.usuarios.repartidor import Repartidor

class ServicioLogistica:
    """
    Capa Controlador (Servicio de Negocio).
    Actúa como el 'Contexto' del Patrón Strategy.
    """
    
    def __init__(self, estrategia_default: IEstrategiaAsignacion):
        """
        Recibe la estrategia inicial (Inyección de Dependencia).
        """
        print("ServicioLogistica inicializado.")
        self._estrategia_asignacion = estrategia_default

    def set_estrategia_asignacion(self, nueva_estrategia: IEstrategiaAsignacion):
        """
        Permite a la Vista (main.py) cambiar la estrategia en caliente.
        """
        print(f"\nSERVICIO: Cambiando estrategia de asignación...")
        self._estrategia_asignacion = nueva_estrategia

    def asignar_repartidor_a_pedido(self, pedido: Pedido, repartidores_disponibles: List[Repartidor]) -> Optional[Repartidor]:
        """
        (Controlador) Orquesta la asignación.
        Delega la decisión al objeto estrategia.
        """
        print(f"SERVICIO: Buscando repartidor para pedido {pedido.id_pedido}...")
        
        # --- ¡AQUÍ USA EL PATRÓN STRATEGY! ---
        repartidor_elegido = self._estrategia_asignacion.ejecutar_asignacion(
            pedido, 
            repartidores_disponibles
        )
        # ------------------------------------
        
        if repartidor_elegido:
            print(f"SERVICIO: Estrategia eligió a {repartidor_elegido.nombre} (ID: {repartidor_elegido.id_usuario}).")
        else:
            print("SERVICIO: Estrategia no encontró repartidor disponible.")
            
        return repartidor_elegido

