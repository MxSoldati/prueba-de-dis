"""
Archivo integrador generado automaticamente
Directorio: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/strategy/impl
Fecha: 2025-11-03 20:15:08
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: estrategia_asignar_mas_cercano.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/strategy/impl/estrategia_asignar_mas_cercano.py
# ================================================================================

# /parcial_delivery/patrones/strategy/impl/estrategia_asignar_mas_cercano.py
import math
from typing import List, Optional
from parcial_delivery.patrones.strategy.i_estrategia_asignacion import IEstrategiaAsignacion
from parcial_delivery.entidades.pedidos.pedido import Pedido
from parcial_delivery.entidades.usuarios.repartidor import Repartidor

class EstrategiaAsignarMasCercano(IEstrategiaAsignacion):
    """
    Una 'Estrategia Concreta'.
    Busca al repartidor cuya 'ubicacion' esté geográficamente
    más cerca de la 'ubicacion_restaurante' del pedido.
    """
    
    def ejecutar_asignacion(self, pedido: Pedido, repartidores_libres: List[Repartidor]) -> Optional[Repartidor]:
        print("--- (Usando Estrategia: Asignar al MÁS CERCANO) ---")
        if not repartidores_libres:
            return None
        
        mejor_repartidor = None
        distancia_minima = float('inf')
        
        loc_restaurante = pedido.ubicacion_restaurante
        
        for repartidor in repartidores_libres:
            loc_repartidor = repartidor.ubicacion
            # Cálculo simple de distancia Euclideana
            distancia = math.sqrt((loc_restaurante[0] - loc_repartidor[0])**2 + (loc_restaurante[1] - loc_repartidor[1])**2)
            
            print(f"    ... evaluando a {repartidor.nombre} (Distancia: {distancia:.2f})")
            
            if distancia < distancia_minima:
                distancia_minima = distancia
                mejor_repartidor = repartidor
                
        return mejor_repartidor

# ================================================================================
# ARCHIVO 3/3: estrategia_asignar_mas_libre.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/strategy/impl/estrategia_asignar_mas_libre.py
# ================================================================================

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

