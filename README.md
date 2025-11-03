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

## 4. Arquitectura del Sistema

### Principios Arquitectónicos

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

El proyecto sigue una arquitectura limpia de N-Capas, donde la comunicación fluye en una sola dirección (Vista -> Controlador -> Modelo).

Asistente de programación
Aquí tienes el código Markdown exacto para la sección "Arquitectura del Sistema", incluyendo los principios SOLID y el diagrama de capas.

Cópialo y pégalo directamente en tu archivo README.md.

Markdown
## 4. Arquitectura del Sistema

### Principios Arquitectónicos

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

+------------------------------+ | PRESENTACION (main.py) | | (Demostracion CLI / Vista) | +------------------------------+ | v +------------------------------+ | SERVICIOS (Controlador) | | (ServicioPedidos, | | ServicioLogistica, | | ServicioUsuarios) | +------------------------------+ | v +------------------------------+ | ENTIDADES (Modelo) | | (Pedido, Cliente, Repartidor)| +------------------------------+ | v +------------------------------+ | PATRONES / UTILIDADES | | (State, Observer, Factory, | | Decorator, Strategy) | +------------------------------+