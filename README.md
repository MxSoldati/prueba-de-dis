## Contexto del Dominio

### Problema que Resuelve

El sistema de **Gestion de Delivery** aborda los desafios de la coordinacion logistica moderna, un dominio que requiere:

1.  **Manejo del Ciclo de Vida del Pedido:**
    * Un pedido no es un objeto estatico; transiciona por multiples estados (`Pendiente`, `En Preparacion`, `Listo`, `En Camino`, `Entregado`).
    * Las acciones permitidas (ej. `cancelar`) deben fallar o tener exito dependiendo del estado actual.

2.  **Coordinacion de Actores en Tiempo Real:**
    * Existen tres roles (`Cliente`, `Restaurante`, `Repartidor`) que deben estar sincronizados sin estar fuertemente acoplados.
    * Un cambio de estado en el `Pedido` (hecho por el Restaurante) debe notificar automaticamente al `Cliente` y al `Sistema de Repartidores`.

3.  **Asignacion Logistica (Recursos):**
    * El sistema debe asignar un `Repartidor` disponible y cercano cuando un pedido esta `Listo para Recoger`.
    * Requiere algoritmos intercambiables para decidir la asignacion (ej. "mas cercano" vs. "con menos pedidos").

4.  **Flexibilidad de Transacciones:**
    * El costo final de un pedido no es fijo; debe permitir agregar "extras" opcionales de forma dinamica (`Envio Prioritario`, `Propina`, `Seguro`).
    * Evitar una "explosion de clases" (`PedidoConPropina`, `PedidoPrioritario`, etc.).

5.  **Trazabilidad y Auditoria:**
    * Almacenamiento del historial de estados de un pedido.
    * Gestion de diferentes tipos de usuarios (`Cliente`, `Repartidor`) con diferentes propiedades.

### Actores del Sistema

* **Cliente:** Crea el pedido, paga, recibe notificaciones y puede (a veces) cancelar.
* **Restaurante:** Acepta el pedido, lo pasa a `En Preparacion` y lo marca como `Listo para Recoger`.
* **Repartidor:** Recibe notificaciones de pedidos listos, acepta un viaje, recoge el pedido y lo marca como `Entregado`.
* **Sistema (Backend):** Orquesta la comunicacion, ejecuta la logica de negocio (asignacion, calculo de costos) y persiste los datos.

### Flujo de Operaciones Tipico
~~~
1. CREACION (Factory): Un Cliente crea un "Pedido" a traves del sistema.
2. TRANSICION (State): El "Restaurante" acepta el pedido. El estado cambia a "En Preparacion".
3. BLOQUEO (State): El "Cliente" intenta "cancelar" el pedido, pero el sistema lo rechaza porque ya esta en preparacion.
4. TRANSICION (State): El "Restaurante" termina el pedido. El estado cambia a "Listo para Recoger".
5. NOTIFICACION (Observer): El "Pedido" (Sujeto) notifica a sus suscriptores:
    * El "Cliente" (Observador) recibe un push: "¡Tu pedido esta listo!"
    * El "SistemaLogistico" (Observador) recibe el evento e inicia la asignacion.
6. ASIGNACION (Strategy): El sistema usa la "EstrategiaAsignarMasCercano" para encontrar un "Repartidor".
7. ENTREGA (State): El "Repartidor" acepta, recoge y entrega el pedido. El estado final es "Entregado".
8. CALCULO (Decorator): El sistema calcula el costo final "envolviendo" el costo base con "CostoPropina" y "CostoPrioritario".
9. CIERRE: El pedido se marca como finalizado.
~~~

## Caracteristicas Principales

### Funcionalidades del Sistema

1.  **Gestion del Ciclo de Vida del Pedido (Patron State)**
    * **Manejo de Transiciones de Estado:**
        * El `Pedido` se gestiona como una Maquina de Estados Finitos (ej. `Pendiente`, `EnPreparacion`, `EnCamino`, `Entregado`).
        * La logica de negocio y las reglas de cada estado se encapsulan en clases separadas (ej. `EstadoPendiente`, `EstadoEnPreparacion`).
    * **Control de Acciones (Resolucion de HU-1):**
        * El estado actual determina que acciones son validas.
        * Ejemplo `cancelar_pedido()`:
            * `EstadoPendiente`: La accion es **exitosa**. El pedido se cancela.
            * `EstadoEnPreparacion`: La accion es **rechazada**. El pedido no se puede cancelar.
        * La clase `Pedido` (el Modelo) se mantiene simple, delegando toda esta logica a su objeto de estado.

2.  **Sistema de Notificaciones en Tiempo Real (Patron Observer)**
    * **Mecanismo de Suscripcion (Publicador/Suscriptor):**
        * El `Pedido` actua como el "Sujeto" (Observable). Mantiene una lista de suscriptores.
        * Cualquier clase que implemente la interfaz `IObservador` (ej. `NotificadorCliente`, `ModuloLogistica`) puede suscribirse a un pedido.
    * **Desacoplamiento de Componentes (Resolucion de HU-2):**
        * Cuando el `Pedido` cambia de estado (ej. `transicionar_a(EstadoEnCamino)`), llama a `notificar()`.
        * El `Pedido` no sabe *como* se notifica (push, email, SMS). Solo emite el evento.
        * Permite anadir nuevos "oyentes" (como un `DashboardDeAdmin`) sin modificar *nunca* la clase `Pedido`.

3.  **Gestion y Creacion de Entidades (Patron Factory Method)**
    * **Creacion centralizada de Usuarios (Resolucion de HU-4):**
        * Se utiliza una `UsuarioFactory` (o fabricas derivadas como `ClienteFactory`, `RepartidorFactory`) para instanciar objetos.
        * El `ServicioUsuarios` (Controlador) pide un usuario a la fabrica (ej. `fabrica.crear_usuario(...)`) sin acoplarse a las clases concretas.
    * **Creacion de tipos especificos:**
        * `Cliente`: Creado con `nombre`, `email` y `direccion_predeterminada`.
        * `Repartidor`: Creado con `nombre`, `email`, `id_vehiculo` y `tipo_vehiculo`.
        * `AdminRestaurante`: Creado con `nombre`, `email` y `id_restaurante_asignado`.

4.  **Calculo de Costos Dinamicos (Patron Decorator)**
    * **Composicion flexible de costos (Resolucion de HU-3):**
        * Un `PedidoBase` implementa una interfaz `ICosto` con un metodo `get_costo()`.
        * El costo final es "envuelto" (decorado) por clases adicionales en tiempo de ejecucion.
    * **Ejemplos de Decoradores:**
        * `CostoEnvioPrioritario(ICosto)`: Anade un monto fijo (ej. `$50`) al costo del componente envuelto.
        * `CostoPropina(ICosto)`: Anade un monto porcentual (ej. `10%`) al costo del componente envuelto.
    * **Evita explosion de clases:**
        * Permite apilar costos dinamicamente (ej. `Propina(Prioritario(PedidoBase))`).
        * No se necesita crear clases como `PedidoConPropinaYPrioridad`.

5.  **Logica de Asignacion Logistica (Patron Strategy)**
    * **Algoritmos de asignacion intercambiables:**
        * Define una familia de algoritmos (Estrategias) para que el `SistemaLogistico` elija un repartidor.
        * El `ServicioLogistico` (Controlador) puede cambiar la estrategia dinamicamente (ej. usar una estrategia diferente en horas pico).
    * **Estrategias Concretas:**
        * `EstrategiaAsignarMasCercano`: Busca el `Repartidor` con menor distancia geografica al restaurante.
        * `EstrategiaAsignarMasLibre`: Busca el `Repartidor` con menos pedidos activos en su cola.
        * `EstrategiaAsignarPorRating`: (Opcional) Busca el `Repartidor` mejor calificado disponible.

## Arquitectura del Sistema

### Principios Arquitectonicos

El sistema está diseñado siguiendo los principios **SOLID** para asegurar un código mantenible, escalable y robusto:

* **Single Responsibility (SRP):** Cada clase tiene una única razón para cambiar.
    * **Entidades:** Solo contienen datos (DTOs) y estado (ej. `Pedido`, `Cliente`).
    * **Servicios:** Contienen la lógica de negocio reutilizable (ej. `ServicioPedidos`).
    * **Patrones:** Implementaciones aisladas y genéricas (ej. `EstadoEnPreparacion`, `CostoPropina`).

* **Open/Closed (OCP):** Abierto a extensión, cerrado a modificación.
    * **Nuevos Estados:** Se puede agregar un `EstadoEnRevision` implementando `IEstadoPedido` sin modificar la clase `Pedido`.
    * **Nuevas Estrategias:** Se puede agregar `EstrategiaAsignarPorRating` sin modificar el `ServicioLogistica`.
    * **Nuevos Costos:** Se puede agregar un `CostoSeguro` (Patrón Decorator) sin modificar el `Pedido` o los otros costos.

* **Liskov Substitution (LSP):** Subtipos intercambiables.
    * Todos los estados (ej. `EstadoPendiente`, `EstadoEnCamino`) son sustituibles por su interfaz `IEstadoPedido`.
    * Todas las estrategias de asignación (ej. `EstrategiaAsignarMasCercano`) son sustituibles por `IEstrategiaAsignacion`.
    * Todos los decoradores de costo son sustituibles por la interfaz `ICosto`.

* **Interface Segregation (ISP):** Interfaces específicas.
    * `IObservador[T]`: Interfaz genérica para cualquier tipo de evento de notificación.
    * `IEstadoPedido`: Interfaz específica para las acciones y transiciones de un pedido.
    * `ICosto`: Interfaz específica para el cálculo de costos.

* **Dependency Inversion (DIP):** Dependencia de abstracciones, no de implementaciones.
    * El `ServicioLogistica` depende de la abstracción `IEstrategiaAsignacion`, no de una estrategia concreta.
    * El `Pedido` depende de la abstracción `IEstadoPedido`.
    * El `ServicioUsuarios` depende de `UsuarioFactory`, no de `Cliente` o `Repartidor`.

### Separación de Capas

El proyecto sigue una arquitectura limpia de N-Capas, donde la comunicación fluye en una sola dirección (Vista -> Controlador -> Modelo), similar a la estructura de `PythonForestal`.

## Patrones de Diseño Implementados

A continuación, se detallan los 5 patrones de diseño implementados, su ubicación en el código y el problema específico que resuelven dentro del dominio del sistema. Elijo 5 patrones por si hay alguno que no le guste o le parezca basico...

### 1. STATE Pattern (Estado)

**Ubicacion:** `ParcialDelivery/patrones/state/` y `ParcialDelivery/entidades/pedido.py`

**Problema que resuelve:**
* Un `Pedido` tiene un ciclo de vida complejo (`Pendiente`, `EnPreparacion`, `EnCamino`, etc.).
* La lógica de negocio (ej. `cancelar_pedido()`) depende 100% del estado actual.
* Evita un "infierno" de sentencias `if/elif/else` en la clase `Pedido`, lo que violaría los principios de Single Responsibility (SRP) y Open/Closed (OCP).

**Implementacion:**
~~~python
# --- En entidades/pedido.py ---
@dataclass
class Pedido:
    # ...
    # El Pedido (Contexto) guarda una referencia a su estado actual.
    estado_actual: Optional[IEstadoPedido] = field(init=False, default=None)

    def __post_init__(self):
        # Se auto-asigna el estado inicial al nacer
        if self.estado_actual is None:
            self.transicionar_a(EstadoPendiente(self))

    def cancelar(self):
        # Delega la accion al objeto de estado.
        # No hay 'ifs' en la entidad Pedido.
        self.estado_actual.cancelar_pedido()

# --- En patrones/state/estado_en_preparacion.py ---
class EstadoEnPreparacion(IEstadoPedido):
    # ...
    def cancelar_pedido(self):
        # La lógica de negocio vive en el estado.
        print(f"ERROR: No se puede cancelar el pedido {self._pedido.id_pedido}, ¡ya está en preparación!")
~~~

**Uso en el sistema:**
* El `ServicioPedidos` (Controlador) llama a `pedido.cancelar()`.
* El `Pedido` (Modelo/Contexto) re-dirige esa llamada a su estado actual (ej. `EstadoEnPreparacion`).
* `EstadoEnPreparacion` (Patrón) ejecuta la lógica y deniega la cancelación.
* Resuelve la **Historia de Usuario HU-1**.

**Ventajas:**
* **Encapsulación:** La lógica de cada estado está aislada en su propia clase.
* **Extensibilidad (OCP):** Se puede agregar un nuevo estado (ej. `EstadoEnRevision`) sin modificar `Pedido.py`.
* **Código Limpio (SRP):** La clase `Pedido` solo gestiona sus datos; las clases de Estado solo gestionan las transiciones.

---

### 2. OBSERVER Pattern (Observador)

**Ubicacion:** `ParcialDelivery/patrones/observer/`

**Problema que resuelve:**
* Cuando un `Pedido` cambia de estado (ej. de `EnPreparacion` a `EnCamino`), múltiples componentes del sistema (que no se conocen entre sí) necesitan reaccionar.
* El `Cliente` necesita una notificación push.
* El `ModuloLogistica` necesita saber que debe re-calcular la ruta del repartidor.
* El `Pedido` (Sujeto) no debe conocer la lógica interna de `NotificadorCliente` o `ModuloLogistica` (alto acoplamiento).

**Implementacion:**
~~~python
# --- En patrones/observer/observable.py (Sujeto) ---
class Observable: # (Sujeto)
    def __init__(self):
        self._observadores: List[IObservador] = []

    def suscribir(self, observador: IObservador):
        self._observadores.append(observador)

    def notificar(self, evento, datos):
        # Notifica a todos los suscriptores
        for obs in self._observadores:
            obs.actualizar(evento, datos)

# --- En entidades/pedido.py ---
class Pedido(Observable): # Pedido ES un Sujeto Observable
    # ...
    def transicionar_a(self, nuevo_estado: IEstadoPedido):
        self.estado_actual = nuevo_estado
        # ¡Notifica a todos los suscriptores sobre el cambio!
        self.notificar(evento="CAMBIO_ESTADO", datos=self)
~~~

**Uso en el sistema:**
* Se crean instancias de `NotificadorCliente` y `ModuloLogistica` (Observadores).
* Ambos se suscriben al objeto `Pedido` usando `pedido.suscribir(...)`.
* Cuando el `ServicioPedidos` cambia el estado, el `Pedido` llama a `notificar()`, y ambos observadores reaccionan automáticamente.
* Resuelve la **Historia de Usuario HU-2**.

**Ventajas:**
* **Desacoplamiento:** El Sujeto (`Pedido`) y los Observadores (`Cliente`) no se conocen.
* **Dinamismo:** Se pueden agregar y quitar observadores en tiempo de ejecución.
* **Extensibilidad (OCP):** Se puede agregar un `DashboardAdmin` como nuevo observador sin tocar el `Pedido`.

---

### 3. FACTORY METHOD Pattern (Fábrica)

**Ubicacion:** `ParcialDelivery/patrones/factory/usuario_factory.py`

**Problema que resuelve:**
* El sistema necesita crear diferentes tipos de `Usuario` (`Cliente`, `Repartidor`, `AdminRestaurante`).
* Cada tipo tiene un proceso de creación y atributos distintos (ej. `Repartidor` necesita `vehiculo`).
* El `ServicioUsuarios` (Controlador) no debe acoplarse a las clases concretas de usuario (violación de DIP).

**Implementacion:**
~~~python
class UsuarioFactory:
    """
    Define la interfaz para crear usuarios, delegando la
    instanciacion a subclases o metodos estaticos.
    """
    @staticmethod
    def crear_usuario(tipo: str, **kwargs) -> Usuario:
        if tipo == "Cliente":
            # Encapsula la logica de construccion
            return Cliente(nombre=kwargs['nombre'], 
                           email=kwargs['email'], 
                           direccion=kwargs['direccion'])
        elif tipo == "Repartidor":
            return Repartidor(nombre=kwargs['nombre'], 
                              email=kwargs['email'], 
                              vehiculo=kwargs['vehiculo'])
        # ...
        raise ValueError(f"Tipo de usuario '{tipo}' desconocido")
~~~

**Uso en el sistema:**
* La `Vista` (main.py) solicita un nuevo usuario.
* El `ServicioUsuarios` (Controlador) recibe los datos y, en lugar de hacer `new Cliente()`, llama a `UsuarioFactory.crear_usuario("Cliente", ...)`.
* Resuelve la **Historia de Usuario HU-4**.

**Ventajas:**
* **Desacoplamiento (DIP):** El `ServicioUsuarios` solo conoce la `UsuarioFactory`, no los `Cliente` o `Repartidor` concretos.
* **Centralización:** La lógica de *cómo* se construye un usuario está en un solo lugar.
* **Extensibilidad (OCP):** Se puede añadir un `AdminRestarurante` modificando solo la fábrica.

---

### 4. DECORATOR Pattern (Decorador)

**Ubicacion:** `ParcialDelivery/patrones/decorator/`

**Problema que resuelve:**
* Se necesita calcular el costo final de un `Pedido` añadiendo "extras" opcionales y dinámicos (ej. `Envío Prioritario`, `Propina`, `Seguro`).
* Una solución con herencia (ej. `PedidoConPropina`, `PedidoPrioritarioConPropina`) es imposible de mantener (explosión de clases).

**Implementacion:**
~~~python
# --- Interfaz comun ---
class ICosto(ABC):
    @abstractmethod
    def get_costo(self) -> float: pass

# --- Componente Concreto ---
class PedidoBase(ICosto):
    def __init__(self, costo_comida: float):
        self._costo = costo_comida
    def get_costo(self) -> float:
        return self._costo

# --- Decorador Concreto ---
class CostoPrioritario(ICosto): # Tambien es un ICosto
    def __init__(self, componente_envuelto: ICosto):
        self._envuelto = componente_envuelto # "Envuelve" a otro ICosto

    def get_costo(self) -> float:
        # Añade su costo ($50) al costo del objeto envuelto
        return 50.0 + self._envuelto.get_costo()
~~~

**Uso en el sistema:**
* El `ServicioPedidos` instancia el costo base: `costo = PedidoBase(500)`.
* Si el cliente marcó "prioritario", envuelve el objeto: `costo = CostoPrioritario(costo)`.
* Si el cliente añadió 10% de propina: `costo = CostoPropina(costo, 0.10)`.
* Al final, llama a `costo_final = costo.get_costo()`.
* Resuelve la **Historia de Usuario HU-3**.

**Ventajas:**
* **Flexibilidad:** Permite añadir y quitar responsabilidades (costos) en tiempo de ejecución.
* **Evita explosión de clases:** No se necesita una clase por cada combinación de extras.
* **Composición (SRP):** Sigue el principio de composición sobre herencia.

---

### 5. STRATEGY Pattern (Estrategia)

**Ubicacion:** `ParcialDelivery/patrones/strategy/`

**Problema que resuelve:**
* El `SistemaLogistico` debe asignar un `Repartidor` a un `Pedido` listo.
* La "mejor" forma de asignar (el algoritmo) puede variar (ej. "el más cercano" vs. "el que menos pedidos tiene" vs. "el mejor calificado").
* Esta lógica de decisión (algoritmo) no debe estar "cableada" (hardcoded) dentro del `ServicioLogistica`.

**Implementacion:**
~~~python
# --- Interfaz de la Estrategia ---
class IEstrategiaAsignacion(ABC):
    @abstractmethod
    def ejecutar_asignacion(self, pedido, repartidores_libres) -> Repartidor: pass

# --- Estrategia Concreta A ---
class EstrategiaAsignarMasCercano(IEstrategIAAsignacion):
    def ejecutar_asignacion(self, pedido, repartidores_libres):
        # ... logica para encontrar el mas cercano ...
        return repartidor_mas_cercano

# --- El Contexto (El Servicio) ---
class ServicioLogistica:
    def __init__(self, estrategia_default: IEstrategiaAsignacion):
        # Recibe la estrategia por Inyeccion de Dependencia
        self._estrategia = estrategia_default

    def set_estrategia(self, nueva_estrategia: IEstrategiaAsignacion):
        # Permite cambiar la estrategia en caliente
        self._estrategia = nueva_estrategia

    def asignar_repartidor_a_pedido(self, pedido, repartidores_libres):
        # Delega la decision al objeto estrategia
        repartidor_elegido = self._estrategia.ejecutar_asignacion(pedido, repartidores_libres)
        return repartidor_elegido
~~~

**Uso en el sistema:**
* El sistema se inicia e inyecta una estrategia por defecto: `servicio_log = ServicioLogistica(EstrategiaAsignarMasCercano())`.
* Cuando el `ModuloLogistica` (Observer) recibe un evento "ListoParaRecoger", llama a `servicio_log.asignar_repartidor_a_pedido(...)`.
* El servicio delega la decisión a la estrategia `EstrategIAAsignarMasCercano`.

**Ventajas:**
* **Algoritmos Intercambiables (OCP):** Se puede añadir `EstrategiaMejorRating` sin tocar `ServicioLogistica`.
* **Desacoplamiento (DIP):** El servicio depende de la interfaz `IEstrategiaAsignacion`, no de una implementación concreta.
* **Flexibilidad:** Permite cambiar el comportamiento del sistema en tiempo de ejecución (ej. usar una estrategia diferente en horas pico).