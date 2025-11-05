"""
Archivo integrador generado automaticamente
Directorio: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/strategy
Fecha: 2025-11-03 20:15:08
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: i_estrategia_asignacion.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/strategy/i_estrategia_asignacion.py
# ================================================================================

# /parcial_delivery/patrones/strategy/i_estrategia_asignacion.py
from abc import ABC, abstractmethod
from typing import List, Optional
from parcial_delivery.entidades.pedidos.pedido import Pedido
from parcial_delivery.entidades.usuarios.repartidor import Repartidor

class IEstrategiaAsignacion(ABC):
    """
    La Interfaz 'Strategy'.
    Define el método que el 'Contexto' (ServicioLogistica) usará
    para ejecutar un algoritmo de asignación.
    """
    
    @abstractmethod
    def ejecutar_asignacion(self, pedido: Pedido, repartidores_libres: List[Repartidor]) -> Optional[Repartidor]:
        """
        Ejecuta el algoritmo de asignación.
        Devuelve el Repartidor elegido o None si no hay ninguno.
        """
        pass

