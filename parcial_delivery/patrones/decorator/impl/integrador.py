"""
Archivo integrador generado automaticamente
Directorio: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator/impl
Fecha: 2025-11-03 20:15:08
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: costo_base.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator/impl/costo_base.py
# ================================================================================

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
    

# ================================================================================
# ARCHIVO 3/4: costo_prioritario.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator/impl/costo_prioritario.py
# ================================================================================

# /parcial_delivery/patrones/decorator/impl/costo_prioritario.py
from parcial_delivery.patrones.decorator.i_costo import ICosto
from parcial_delivery.constantes import COSTO_ENVIO_PRIORITARIO # (¡Crearemos este archivo!)

class CostoPrioritario(ICosto):
    """
    Un 'Decorador Concreto'. Añade un costo fijo por envío prioritario.
    """
    def __init__(self, componente_envuelto: ICosto):
        self._componente_envuelto = componente_envuelto

    def get_costo(self) -> float:
        # Añade su propio costo al costo del componente que envuelve
        return COSTO_ENVIO_PRIORITARIO + self._componente_envuelto.get_costo()

    def get_descripcion(self) -> str:
        return f"{self._componente_envuelto.get_descripcion()} + Envío Prioritario (${COSTO_ENVIO_PRIORITARIO})"

# ================================================================================
# ARCHIVO 4/4: costo_propina.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator/impl/costo_propina.py
# ================================================================================

# /parcial_delivery/patrones/decorator/impl/costo_propina.py
from parcial_delivery.patrones.decorator.i_costo import ICosto

class CostoPropina(ICosto):
    """
    Otro 'Decorador Concreto'. Añade un costo porcentual (propina).
    """
    def __init__(self, componente_envuelto: ICosto, porcentaje: float):
        self._componente_envuelto = componente_envuelto
        self._porcentaje = porcentaje # ej. 0.10 para 10%

    def get_costo(self) -> float:
        costo_base = self._componente_envuelto.get_costo()
        costo_propina = costo_base * self._porcentaje
        return costo_base + costo_propina

    def get_descripcion(self) -> str:
        return f"{self._componente_envuelto.get_descripcion()} + Propina ({self._porcentaje * 100}%)"

