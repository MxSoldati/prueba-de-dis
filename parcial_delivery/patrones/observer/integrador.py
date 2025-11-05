"""
Archivo integrador generado automaticamente
Directorio: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/observer
Fecha: 2025-11-03 20:15:08
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/observer/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/observer/observable.py
# ================================================================================

# /parcial_delivery/patrones/observer/observable.py
from typing import List
from .observer import IObservador

class Observable:
    """
    La clase 'Sujeto' (o Publicador).
    Mantiene una lista de Observadores y les notifica.
    """
    def __init__(self):
        self._observadores: List[IObservador] = []

    def suscribir(self, observador: IObservador):
        """Añade un observador a la lista."""
        if observador not in self._observadores:
            self._observadores.append(observador)

    def desuscribir(self, observador: IObservador):
        """Quita un observador de la lista."""
        self._observadores.remove(observador)

    def notificar(self, evento: str, datos: any):
        """Notifica a todos los observadores suscritos."""
        print(f"SUJETO: Notificando evento '{evento}' a {len(self._observadores)} observador(es)...")
        for obs in self._observadores:
            obs.actualizar(evento, datos)

# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/observer/observer.py
# ================================================================================

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

