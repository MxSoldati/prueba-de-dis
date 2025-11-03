# /parcial_delivery/patrones/strategy/impl/estrategia_asignar_mas_libre.py
from typing import List, Optional
from parcial_delivery.patrones.strategy.i_estrategia_asignacion import IEstrategiaAsignacion
from parcial_delivery.entidades.pedidos.pedido import Pedido
from parcial_delivery.entidades.usuarios.repartidor import Repartidor

class EstrategiaAsignarMasLibre(IEstrategiaAsignacion):
    """
    Una 'Estrategia Concreta'.
    Busca al repartidor que tenga menos 'pedidos_activos'.
    """
    
    def ejecutar_asignacion(self, pedido: Pedido, repartidores_libres: List[Repartidor]) -> Optional[Repartidor]:
        print("--- (Usando Estrategia: Asignar al MÁS LIBRE) ---")
        if not repartidores_libres:
            return None
        
        # Ordena la lista de repartidores por 'pedidos_activos' (de menor a mayor)
        repartidor_elegido = sorted(repartidores_libres, key=lambda r: r.pedidos_activos)[0]
        
        print(f"    ... evaluando (Repartidor {repartidor_elegido.nombre} tiene {repartidor_elegido.pedidos_activos} pedidos)")
        
        return repartidor_elegido