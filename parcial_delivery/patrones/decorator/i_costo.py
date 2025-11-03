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