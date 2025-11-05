"""
Archivo integrador generado automaticamente
Directorio: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/excepciones
Fecha: 2025-11-03 20:15:08
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/excepciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: delivery_exception.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/excepciones/delivery_exception.py
# ================================================================================

# /parcial_delivery/excepciones/delivery_exception.py

class DeliveryException(Exception):
    """
    Excepción base para todos los errores controlados
    de la lógica de negocio de nuestro sistema.
    """
    pass

# ================================================================================
# ARCHIVO 3/3: pedido_exception.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/excepciones/pedido_exception.py
# ================================================================================

# /parcial_delivery/excepciones/pedido_exception.py
from .delivery_exception import DeliveryException

class PedidoCancelacionException(DeliveryException):
    """
    Lanzada específicamente cuando se intenta cancelar un pedido
    en un estado que no lo permite (ej. 'En Preparación').
    """
    pass

