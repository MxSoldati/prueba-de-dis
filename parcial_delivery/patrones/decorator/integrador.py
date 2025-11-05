"""
Archivo integrador generado automaticamente
Directorio: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator
Fecha: 2025-11-03 20:15:08
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: i_costo.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator/i_costo.py
# ================================================================================

# /parcial_delivery/patrones/decorator/i_costo.py
from abc import ABC, abstractmethod

class ICosto(ABC):
    """
    La Interfaz 'Componente' del patrón Decorator.
    Define el método que todos los costos (base y extras) deben implementar.
    """
    @abstractmethod
    def get_costo(self) -> float:
        pass

    @abstractmethod
    def get_descripcion(self) -> str:
        pass

