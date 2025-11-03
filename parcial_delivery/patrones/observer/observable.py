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