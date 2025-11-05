"""
Archivo integrador generado automaticamente
Directorio: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/pedidos
Fecha: 2025-11-03 20:15:08
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/pedidos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: servicio_pedidos.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/pedidos/servicio_pedidos.py
# ================================================================================

# /parcial_delivery/servicios/pedidos/servicio_pedidos.py
from typing import List, Optional, Dict, Any, Tuple # ¡Añadir Tuple!
from parcial_delivery.entidades.pedidos.pedido import Pedido
from parcial_delivery.patrones.observer.observer import IObservador
from parcial_delivery.entidades.usuarios.cliente import Cliente
# ... (importaciones de Decorator) ...
from parcial_delivery.patrones.decorator.i_costo import ICosto
from parcial_delivery.patrones.decorator.impl.costo_base import CostoBasePedido
from parcial_delivery.patrones.decorator.impl.costo_prioritario import CostoPrioritario
from parcial_delivery.patrones.decorator.impl.costo_propina import CostoPropina

class ServicioPedidos:
    # ... (__init__ queda igual) ...
    def __init__(self):
        print("ServicioPedidos inicializado.")
        self._pedidos: List[Pedido] = []
        self._proximo_id = 101

    # --- ¡MÉTODO MODIFICADO! ---
    def crear_pedido(self, cliente: Cliente, items: List[str], costo_base: float, ubicacion_restaurante: Tuple[int, int]) -> Pedido:
        """
        Lógica de negocio para crear un pedido.
        AHORA RECIBE UN OBJETO Cliente y la Ubicación del Restaurante.
        """
        print(f"\nSERVICIO: Recibida orden para crear pedido para Cliente {cliente.id_usuario} ({cliente.nombre}).")
        
        nuevo_pedido = Pedido(
            id_pedido=self._proximo_id,
            cliente=f"Cliente ID {cliente.id_usuario}", 
            items=items,
            costo_base=costo_base,
            ubicacion_restaurante=ubicacion_restaurante # ¡NUEVO CAMPO!
        )
        self._proximo_id += 1
        self._pedidos.append(nuevo_pedido)
        
        print(f"SERVICIO: Pedido {nuevo_pedido.id_pedido} creado.")
        return nuevo_pedido
    
    # ... (el resto de métodos: avanzar_estado_pedido, cancelar_pedido, etc. quedan igual) ...
    def avanzar_estado_pedido(self, id_pedido: int):
        pedido = self._buscar_pedido(id_pedido)
        if pedido:
            print(f"SERVICIO: Avanzando estado del pedido {id_pedido}...")
            pedido.avanzar()
        else:
            print(f"SERVICIO: ERROR - Pedido {id_pedido} no encontrado.")

    def cancelar_pedido(self, id_pedido: int):
        pedido = self._buscar_pedido(id_pedido)
        if pedido:
            print(f"SERVICIO: Intentando cancelar pedido {id_pedido}...")
            pedido.cancelar()
        else:
            print(f"SERVICIO: ERROR - Pedido {id_pedido} no encontrado.")

    def get_estado_pedido(self, id_pedido: int) -> str:
        pedido = self._buscar_pedido(id_pedido)
        if pedido:
            return pedido.get_estado()
        return "No encontrado"

    def suscribir_a_pedido(self, id_pedido: int, observador: IObservador):
        pedido = self._buscar_pedido(id_pedido)
        if pedido:
            print(f"SERVICIO: Suscribiendo observador al pedido {id_pedido}.")
            pedido.suscribir(observador)
        else:
            print(f"SERVICIO: ERROR - Pedido {id_pedido} no encontrado.")

    def calcular_costo_final(self, id_pedido: int, extras: List[Dict[str, Any]]) -> tuple[float, str]:
        print(f"SERVICIO: Calculando costo final para pedido {id_pedido}...")
        pedido = self._buscar_pedido(id_pedido)
        if not pedido:
            raise ValueError(f"Pedido {id_pedido} no encontrado.")
        costo_calculado: ICosto = CostoBasePedido(pedido)
        for extra in extras:
            if extra["tipo"] == "prioritario":
                costo_calculado = CostoPrioritario(costo_calculado)
            elif extra["tipo"] == "propina":
                porcentaje = extra.get("valor", 0.10) 
                costo_calculado = CostoPropina(costo_calculado, porcentaje)
        costo_final = costo_calculado.get_costo()
        descripcion_final = costo_calculado.get_descripcion()
        print(f"SERVICIO: Cálculo completo. Desc: [{descripcion_final}]")
        return costo_final, descripcion_final
    
    def _buscar_pedido(self, id_pedido: int) -> Optional[Pedido]:
        for p in self._pedidos:
            if p.id_pedido == id_pedido:
                return p
        return None

