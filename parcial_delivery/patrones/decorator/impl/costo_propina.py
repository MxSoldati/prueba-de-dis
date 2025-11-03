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