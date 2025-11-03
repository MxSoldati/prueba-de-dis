# /parcial_delivery/patrones/observer/observer.py
from abc import ABC, abstractmethod

class IObservador(ABC):
    """
    La Interfaz 'Observador' (o Suscriptor).
    Define el método 'actualizar' que el Sujeto llamará.
    """
    @abstractmethod
    def actualizar(self, evento: str, datos: any):
        """Recibe la notificación del Sujeto."""
        pass