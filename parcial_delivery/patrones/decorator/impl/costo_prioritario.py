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