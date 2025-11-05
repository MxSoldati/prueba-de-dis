"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery
Fecha de generacion: 2025-11-03 20:15:08
Total de archivos integrados: 45
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#
# DIRECTORIO: entidades/logistica
#   4. __init__.py
#
# DIRECTORIO: entidades/pedidos
#   5. __init__.py
#   6. pedido.py
#
# DIRECTORIO: entidades/usuarios
#   7. __init__.py
#   8. cliente.py
#   9. repartidor.py
#   10. usuario.py
#
# DIRECTORIO: excepciones
#   11. __init__.py
#   12. delivery_exception.py
#   13. pedido_exception.py
#
# DIRECTORIO: notificaciones
#   14. __init__.py
#   15. notificador_cliente.py
#
# DIRECTORIO: patrones
#   16. __init__.py
#
# DIRECTORIO: patrones/decorator
#   17. __init__.py
#   18. i_costo.py
#
# DIRECTORIO: patrones/decorator/impl
#   19. __init__.py
#   20. costo_base.py
#   21. costo_prioritario.py
#   22. costo_propina.py
#
# DIRECTORIO: patrones/factory
#   23. __init__.py
#   24. usuario_factory.py
#
# DIRECTORIO: patrones/observer
#   25. __init__.py
#   26. observable.py
#   27. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#   28. __init__.py
#
# DIRECTORIO: patrones/state
#   29. __init__.py
#   30. i_estado_pedido.py
#
# DIRECTORIO: patrones/state/impl
#   31. __init__.py
#   32. estado_en_preparacion.py
#   33. estado_pendiente.py
#
# DIRECTORIO: patrones/strategy
#   34. __init__.py
#   35. i_estrategia_asignacion.py
#
# DIRECTORIO: patrones/strategy/impl
#   36. __init__.py
#   37. estrategia_asignar_mas_cercano.py
#   38. estrategia_asignar_mas_libre.py
#
# DIRECTORIO: servicios
#   39. __init__.py
#
# DIRECTORIO: servicios/logistica
#   40. __init__.py
#   41. servicio_logistica.py
#
# DIRECTORIO: servicios/pedidos
#   42. __init__.py
#   43. servicio_pedidos.py
#
# DIRECTORIO: servicios/usuarios
#   44. __init__.py
#   45. servicio_usuarios.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/45: __init__.py
# Directorio: .
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/45: constantes.py
# Directorio: .
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/constantes.py
# ==============================================================================

# /parcial_delivery/constantes.py
"""
Archivo central para constantes del sistema.
"""

# --- Costos (Patrón Decorator) ---
COSTO_ENVIO_PRIORITARIO = 150.0


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/45: __init__.py
# Directorio: entidades
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/logistica
################################################################################

# ==============================================================================
# ARCHIVO 4/45: __init__.py
# Directorio: entidades/logistica
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/logistica/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/pedidos
################################################################################

# ==============================================================================
# ARCHIVO 5/45: __init__.py
# Directorio: entidades/pedidos
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/pedidos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 6/45: pedido.py
# Directorio: entidades/pedidos
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/pedidos/pedido.py
# ==============================================================================

# /parcial_delivery/entidades/pedidos/pedido.py
from dataclasses import dataclass, field
from typing import Optional, List, Tuple # ¡Añadir Tuple!

# ... (importaciones de State y Observer) ...
from parcial_delivery.patrones.state.i_estado_pedido import IEstadoPedido
from parcial_delivery.patrones.state.impl.estado_pendiente import EstadoPendiente
from parcial_delivery.patrones.observer.observable import Observable

@dataclass
class Pedido(Observable): 
    # ... (atributos id_pedido, cliente, items, costo_base) ...
    id_pedido: int
    cliente: str 
    items: List[str]
    costo_base: float
    
    # --- NUEVO CAMPO PARA PATRÓN STRATEGY ---
    ubicacion_restaurante: Tuple[int, int] = field(default=(0, 0))
    # ----------------------------------------
    
    estado_actual: Optional[IEstadoPedido] = field(init=False, repr=False, default=None)

    # ... (el resto de la clase: __post_init__, transicionar_a, etc. quedan igual) ...
    def __post_init__(self):
        Observable.__init__(self) 
        if self.estado_actual is None:
            self.transicionar_a(EstadoPendiente(self))

    def transicionar_a(self, nuevo_estado: IEstadoPedido):
        nombre_estado = "desconocido"
        if nuevo_estado:
            nombre_estado = nuevo_estado.get_nombre_estado()
        print(f"PEDIDO {self.id_pedido}: Transicionando a -> {nombre_estado}")
        self.estado_actual = nuevo_estado
        self.notificar(evento="CAMBIO_ESTADO", datos=self)

    def avanzar(self):
        self.estado_actual.avanzar_estado()

    def cancelar(self):
        self.estado_actual.cancelar_pedido()

    def get_estado(self) -> str:
        return self.estado_actual.get_nombre_estado()


################################################################################
# DIRECTORIO: entidades/usuarios
################################################################################

# ==============================================================================
# ARCHIVO 7/45: __init__.py
# Directorio: entidades/usuarios
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/usuarios/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 8/45: cliente.py
# Directorio: entidades/usuarios
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/usuarios/cliente.py
# ==============================================================================

# /parcial_delivery/entidades/usuarios/cliente.py
from dataclasses import dataclass
from .usuario import Usuario

@dataclass
class Cliente(Usuario):
    """ Entidad Cliente (hereda de Usuario) """
    direccion: str
    telefono: str

# ==============================================================================
# ARCHIVO 9/45: repartidor.py
# Directorio: entidades/usuarios
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/usuarios/repartidor.py
# ==============================================================================

# /parcial_delivery/entidades/usuarios/repartidor.py
from dataclasses import dataclass, field
from .usuario import Usuario
from typing import Tuple # ¡Importante!

@dataclass
class Repartidor(Usuario):
    """ Entidad Repartidor (hereda de Usuario) """
    tipo_vehiculo: str # ej. "Moto", "Bicicleta"
    disponible: bool = True
    
    # --- NUEVOS CAMPOS PARA PATRÓN STRATEGY ---
    # Usamos una tupla (x, y) para simular coordenadas
    ubicacion: Tuple[int, int] = field(default=(0, 0))
    pedidos_activos: int = 0
    # ------------------------------------------

# ==============================================================================
# ARCHIVO 10/45: usuario.py
# Directorio: entidades/usuarios
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/usuarios/usuario.py
# ==============================================================================

# /parcial_delivery/entidades/usuarios/usuario.py
from dataclasses import dataclass

@dataclass
class Usuario:
    """ Clase base para todos los usuarios (Modelo) """
    id_usuario: int
    nombre: str
    email: str


################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 11/45: __init__.py
# Directorio: excepciones
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 12/45: delivery_exception.py
# Directorio: excepciones
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/excepciones/delivery_exception.py
# ==============================================================================

# /parcial_delivery/excepciones/delivery_exception.py

class DeliveryException(Exception):
    """
    Excepción base para todos los errores controlados
    de la lógica de negocio de nuestro sistema.
    """
    pass

# ==============================================================================
# ARCHIVO 13/45: pedido_exception.py
# Directorio: excepciones
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/excepciones/pedido_exception.py
# ==============================================================================

# /parcial_delivery/excepciones/pedido_exception.py
from .delivery_exception import DeliveryException

class PedidoCancelacionException(DeliveryException):
    """
    Lanzada específicamente cuando se intenta cancelar un pedido
    en un estado que no lo permite (ej. 'En Preparación').
    """
    pass


################################################################################
# DIRECTORIO: notificaciones
################################################################################

# ==============================================================================
# ARCHIVO 14/45: __init__.py
# Directorio: notificaciones
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/notificaciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 15/45: notificador_cliente.py
# Directorio: notificaciones
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/notificaciones/notificador_cliente.py
# ==============================================================================

# /parcial_delivery/notificaciones/notificador_cliente.py
from parcial_delivery.patrones.observer.observer import IObservador
from parcial_delivery.entidades.pedidos.pedido import Pedido

class NotificadorCliente(IObservador):
    """
    Este es un Observador Concreto.
    Su trabajo es "escuchar" los eventos del Pedido y simular
    el envío de una notificación al cliente.
    """
    
    def __init__(self, cliente_telefono: str):
        self._telefono = cliente_telefono

    def actualizar(self, evento: str, datos: Pedido):
        """
        Esta es la acción que el Sujeto (Pedido) llamará.
        """
        if evento == "CAMBIO_ESTADO":
            # Filtramos el evento que nos interesa
            id_pedido = datos.id_pedido
            nuevo_estado = datos.get_estado()
            
            # Simulamos el envío de la notificación
            print(f"--- [NOTIFICADOR CLIENTE] ---")
            print(f"    Simulando envío de SMS al {self._telefono}:")
            print(f"    'Tu pedido {id_pedido} ha cambiado de estado a: {nuevo_estado}'")
            print(f"--- [FIN NOTIFICADOR] ---")


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 16/45: __init__.py
# Directorio: patrones
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/decorator
################################################################################

# ==============================================================================
# ARCHIVO 17/45: __init__.py
# Directorio: patrones/decorator
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 18/45: i_costo.py
# Directorio: patrones/decorator
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator/i_costo.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones/decorator/impl
################################################################################

# ==============================================================================
# ARCHIVO 19/45: __init__.py
# Directorio: patrones/decorator/impl
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 20/45: costo_base.py
# Directorio: patrones/decorator/impl
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator/impl/costo_base.py
# ==============================================================================

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
    

# ==============================================================================
# ARCHIVO 21/45: costo_prioritario.py
# Directorio: patrones/decorator/impl
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator/impl/costo_prioritario.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 22/45: costo_propina.py
# Directorio: patrones/decorator/impl
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/decorator/impl/costo_propina.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 23/45: __init__.py
# Directorio: patrones/factory
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/45: usuario_factory.py
# Directorio: patrones/factory
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/factory/usuario_factory.py
# ==============================================================================

# /parcial_delivery/patrones/factory/usuario_factory.py
from parcial_delivery.entidades.usuarios.usuario import Usuario
from parcial_delivery.entidades.usuarios.cliente import Cliente
from parcial_delivery.entidades.usuarios.repartidor import Repartidor

class UsuarioFactory:
    # ... (_id_counter y _next_id quedan igual) ...
    _id_counter = 1
    @staticmethod
    def _next_id() -> int:
        id = UsuarioFactory._id_counter
        UsuarioFactory._id_counter += 1
        return id

    @staticmethod
    def crear_usuario(tipo: str, **kwargs) -> Usuario:
        id_usuario = UsuarioFactory._next_id()
        
        if tipo == "Cliente":
            # ... (esta parte queda igual) ...
            if 'direccion' not in kwargs or 'telefono' not in kwargs:
                raise ValueError("Cliente requiere 'direccion' y 'telefono'")
            return Cliente(
                id_usuario=id_usuario,
                nombre=kwargs['nombre'],
                email=kwargs['email'],
                direccion=kwargs['direccion'],
                telefono=kwargs['telefono']
            )
            
        elif tipo == "Repartidor":
            # --- ¡SECCIÓN MODIFICADA! ---
            if 'tipo_vehiculo' not in kwargs:
                raise ValueError("Repartidor requiere 'tipo_vehiculo'")
            return Repartidor(
                id_usuario=id_usuario,
                nombre=kwargs['nombre'],
                email=kwargs['email'],
                tipo_vehiculo=kwargs['tipo_vehiculo'],
                # Añadimos los nuevos campos (con valores por defecto si no vienen)
                ubicacion=kwargs.get('ubicacion', (0, 0)),
                pedidos_activos=kwargs.get('pedidos_activos', 0)
            )
            # ---------------------------
        else:
            raise ValueError(f"Tipo de usuario '{tipo}' desconocido")


################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 25/45: __init__.py
# Directorio: patrones/observer
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 26/45: observable.py
# Directorio: patrones/observer
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/observer/observable.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 27/45: observer.py
# Directorio: patrones/observer
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/observer/observer.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 28/45: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/observer/eventos/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/state
################################################################################

# ==============================================================================
# ARCHIVO 29/45: __init__.py
# Directorio: patrones/state
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/state/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 30/45: i_estado_pedido.py
# Directorio: patrones/state
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/state/i_estado_pedido.py
# ==============================================================================

# /parcial_delivery/patrones/state/i_estado_pedido.py
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# 'TYPE_CHECKING' nos ayuda a evitar un error de "importación circular"
# ya que Pedido (el contexto) y IEstadoPedido se necesitan mutuamente.
if TYPE_CHECKING:
    from parcial_delivery.entidades.pedidos.pedido import Pedido

class IEstadoPedido(ABC):
    """
    La Interfaz (Clase Base Abstracta) para todos los estados de un Pedido.
    Define las acciones que un pedido puede intentar hacer.
    
    Cada estado concreto implementará estas acciones de forma diferente.
    """
    
    def __init__(self, pedido_contexto: 'Pedido'):
        """
        Guarda una referencia de vuelta al Pedido (el contexto) para
        poder cambiar su estado.
        """
        self._pedido = pedido_contexto

    @abstractmethod
    def avanzar_estado(self):
        """Intenta avanzar al siguiente estado del ciclo de vida."""
        pass

    @abstractmethod
    def cancelar_pedido(self):
        """Intenta cancelar el pedido."""
        pass

    @abstractmethod
    def get_nombre_estado(self) -> str:
        """Devuelve el nombre del estado actual."""
        pass


################################################################################
# DIRECTORIO: patrones/state/impl
################################################################################

# ==============================================================================
# ARCHIVO 31/45: __init__.py
# Directorio: patrones/state/impl
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/state/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 32/45: estado_en_preparacion.py
# Directorio: patrones/state/impl
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/state/impl/estado_en_preparacion.py
# ==============================================================================

# /parcial_delivery/patrones/state/impl/estado_en_preparacion.py
from parcial_delivery.patrones.state.i_estado_pedido import IEstadoPedido
from typing import TYPE_CHECKING
# --- ¡NUEVA IMPORTACIÓN DE EXCEPCIÓN! ---
from parcial_delivery.excepciones.pedido_exception import PedidoCancelacionException

# ... (importación de EstadoEnCamino si la tuvieras) ...

if TYPE_CHECKING:
    from parcial_delivery.entidades.pedidos.pedido import Pedido

class EstadoEnPreparacion(IEstadoPedido):
    """
    Implementación del estado 'En Preparación'.
    """
    
    def __init__(self, pedido_contexto: 'Pedido'):
        super().__init__(pedido_contexto)

    def get_nombre_estado(self) -> str:
        return "En Preparación"

    def avanzar_estado(self):
        """
        Lógica para avanzar: El restaurante termina de preparar.
        """
        print(f"ACCIÓN: El pedido {self._pedido.id_pedido} está listo y salió para entrega.")
        # self._pedido.transicionar_a(EstadoEnCamino(self._pedido))
        print("... (Transicionando a 'En Camino') ...")


    def cancelar_pedido(self):
        """
        Lógica para cancelar: ¡NO SE PUEDE! (HU-1)
        En lugar de 'print', ahora lanza una excepción.
        """
        # --- ¡CÓDIGO MODIFICADO! ---
        raise PedidoCancelacionException(
            f"No se puede cancelar el pedido {self._pedido.id_pedido}, ¡ya está en preparación!"
        )
        # ---------------------------

# ==============================================================================
# ARCHIVO 33/45: estado_pendiente.py
# Directorio: patrones/state/impl
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/state/impl/estado_pendiente.py
# ==============================================================================

# /parcial_delivery/patrones/state/impl/estado_pendiente.py
from parcial_delivery.patrones.state.i_estado_pedido import IEstadoPedido
from typing import TYPE_CHECKING

# Importamos el *siguiente* estado al que podemos avanzar
from .estado_en_preparacion import EstadoEnPreparacion
# (También podríamos importar un EstadoCancelado)

if TYPE_CHECKING:
    from parcial_delivery.entidades.pedidos.pedido import Pedido

class EstadoPendiente(IEstadoPedido):
    """
    Implementación del estado 'Pendiente'.
    Este es el primer estado de un pedido cuando se crea.
    """
    
    def __init__(self, pedido_contexto: 'Pedido'):
        super().__init__(pedido_contexto)

    def get_nombre_estado(self) -> str:
        return "Pendiente de Aprobación"

    def avanzar_estado(self):
        """
        Lógica para avanzar: El restaurante acepta el pedido.
        Pasa de 'Pendiente' a 'En Preparación'.
        """
        print(f"ACCIÓN: El restaurante aprobó el pedido {self._pedido.id_pedido}.")
        # El estado mismo le dice al pedido (contexto) que transicione
        self._pedido.transicionar_a(EstadoEnPreparacion(self._pedido))

    def cancelar_pedido(self):
        """
        Lógica para cancelar: ¡SÍ SE PUEDE! (HU-1)
        Un pedido pendiente puede ser cancelado.
        """
        print(f"ACCIÓN: El cliente canceló el pedido {self._pedido.id_pedido} (estaba pendiente).")
        # (Aquí transicionaríamos a un 'EstadoCancelado' si lo tuviéramos)
        print("... (Pedido marcado como cancelado) ...")


################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 34/45: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 35/45: i_estrategia_asignacion.py
# Directorio: patrones/strategy
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/strategy/i_estrategia_asignacion.py
# ==============================================================================

# /parcial_delivery/patrones/strategy/i_estrategia_asignacion.py
from abc import ABC, abstractmethod
from typing import List, Optional
from parcial_delivery.entidades.pedidos.pedido import Pedido
from parcial_delivery.entidades.usuarios.repartidor import Repartidor

class IEstrategiaAsignacion(ABC):
    """
    La Interfaz 'Strategy'.
    Define el método que el 'Contexto' (ServicioLogistica) usará
    para ejecutar un algoritmo de asignación.
    """
    
    @abstractmethod
    def ejecutar_asignacion(self, pedido: Pedido, repartidores_libres: List[Repartidor]) -> Optional[Repartidor]:
        """
        Ejecuta el algoritmo de asignación.
        Devuelve el Repartidor elegido o None si no hay ninguno.
        """
        pass


################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 36/45: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 37/45: estrategia_asignar_mas_cercano.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/strategy/impl/estrategia_asignar_mas_cercano.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 38/45: estrategia_asignar_mas_libre.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/patrones/strategy/impl/estrategia_asignar_mas_libre.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 39/45: __init__.py
# Directorio: servicios
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/logistica
################################################################################

# ==============================================================================
# ARCHIVO 40/45: __init__.py
# Directorio: servicios/logistica
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/logistica/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 41/45: servicio_logistica.py
# Directorio: servicios/logistica
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/logistica/servicio_logistica.py
# ==============================================================================

# /parcial_delivery/servicios/logistica/servicio_logistica.py
from typing import List, Optional
from parcial_delivery.patrones.strategy.i_estrategia_asignacion import IEstrategiaAsignacion
from parcial_delivery.entidades.pedidos.pedido import Pedido
from parcial_delivery.entidades.usuarios.repartidor import Repartidor

class ServicioLogistica:
    """
    Capa Controlador (Servicio de Negocio).
    Actúa como el 'Contexto' del Patrón Strategy.
    """
    
    def __init__(self, estrategia_default: IEstrategiaAsignacion):
        """
        Recibe la estrategia inicial (Inyección de Dependencia).
        """
        print("ServicioLogistica inicializado.")
        self._estrategia_asignacion = estrategia_default

    def set_estrategia_asignacion(self, nueva_estrategia: IEstrategiaAsignacion):
        """
        Permite a la Vista (main.py) cambiar la estrategia en caliente.
        """
        print(f"\nSERVICIO: Cambiando estrategia de asignación...")
        self._estrategia_asignacion = nueva_estrategia

    def asignar_repartidor_a_pedido(self, pedido: Pedido, repartidores_disponibles: List[Repartidor]) -> Optional[Repartidor]:
        """
        (Controlador) Orquesta la asignación.
        Delega la decisión al objeto estrategia.
        """
        print(f"SERVICIO: Buscando repartidor para pedido {pedido.id_pedido}...")
        
        # --- ¡AQUÍ USA EL PATRÓN STRATEGY! ---
        repartidor_elegido = self._estrategia_asignacion.ejecutar_asignacion(
            pedido, 
            repartidores_disponibles
        )
        # ------------------------------------
        
        if repartidor_elegido:
            print(f"SERVICIO: Estrategia eligió a {repartidor_elegido.nombre} (ID: {repartidor_elegido.id_usuario}).")
        else:
            print("SERVICIO: Estrategia no encontró repartidor disponible.")
            
        return repartidor_elegido


################################################################################
# DIRECTORIO: servicios/pedidos
################################################################################

# ==============================================================================
# ARCHIVO 42/45: __init__.py
# Directorio: servicios/pedidos
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/pedidos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 43/45: servicio_pedidos.py
# Directorio: servicios/pedidos
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/pedidos/servicio_pedidos.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios/usuarios
################################################################################

# ==============================================================================
# ARCHIVO 44/45: __init__.py
# Directorio: servicios/usuarios
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/usuarios/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 45/45: servicio_usuarios.py
# Directorio: servicios/usuarios
# Ruta completa: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/usuarios/servicio_usuarios.py
# ==============================================================================

# /parcial_delivery/servicios/usuarios/servicio_usuarios.py
from typing import List
from parcial_delivery.entidades.usuarios.usuario import Usuario
from parcial_delivery.patrones.factory.usuario_factory import UsuarioFactory

class ServicioUsuarios:
    """
    Capa Controlador (Servicio de Dominio).
    Maneja la lógica de negocio para operar con Usuarios.
    Utiliza el Patrón Factory para la creación.
    """

    def __init__(self):
        print("ServicioUsuarios inicializado.")
        # (Usaremos una lista en memoria como 'base de datos' temporal)
        self._usuarios: List[Usuario] = []

    def crear_usuario(self, tipo: str, **kwargs) -> Usuario:
        """
        (Controlador) Pide a la Fábrica que cree un usuario.
        El servicio no sabe CÓMO se crea, solo pide.
        """
        print(f"SERVICIO: Recibida orden para crear usuario tipo '{tipo}'.")
        
        # --- ¡AQUÍ USA EL PATRÓN FACTORY! ---
        nuevo_usuario = UsuarioFactory.crear_usuario(tipo, **kwargs)
        # ------------------------------------
        
        self._usuarios.append(nuevo_usuario)
        print(f"SERVICIO: Usuario {nuevo_usuario.id_usuario} ({nuevo_usuario.nombre}) creado.")
        return nuevo_usuario


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 45
# Generado: 2025-11-03 20:15:08
################################################################################
