## Contexto del Dominio

### Problema que Resuelve

El sistema de **Gestión de Delivery** aborda los desafíos de la coordinación logística moderna, un dominio que requiere:

1.  **Manejo del Ciclo de Vida del Pedido:**
    * Un pedido no es un objeto estático; transiciona por múltiples estados (`Pendiente`, `En Preparación`, `Listo`, `En Camino`, `Entregado`).
    * Las acciones permitidas (ej. `cancelar`) deben fallar o tener éxito dependiendo del estado actual.

2.  **Coordinación de Actores en Tiempo Real:**
    * Existen tres roles (`Cliente`, `Restaurante`, `Repartidor`) que deben estar sincronizados sin estar fuertemente acoplados.
    * Un cambio de estado en el `Pedido` (hecho por el Restaurante) debe notificar automáticamente al `Cliente` y al `Sistema de Repartidores`.

3.  **Asignación Logística (Recursos):**
    * El sistema debe asignar un `Repartidor` disponible y cercano cuando un pedido está `Listo para Recoger`.
    * Requiere algoritmos intercambiables para decidir la asignación (ej. "más cercano" vs. "con menos pedidos").

4.  **Flexibilidad de Transacciones:**
    * El costo final de un pedido no es fijo; debe permitir agregar "extras" opcionales de forma dinámica (`Envío Prioritario`, `Propina`, `Seguro`).
    * Evitar una "explosión de clases" (`PedidoConPropina`, `PedidoPrioritario`, etc.).

5.  **Trazabilidad y Auditoría:**
    * Almacenamiento del historial de estados de un pedido.
    * Gestión de diferentes tipos de usuarios (`Cliente`, `Repartidor`) con diferentes propiedades.

### Actores del Sistema

* **Cliente:** Crea el pedido, paga, recibe notificaciones y puede (a veces) cancelar.
* **Restaurante:** Acepta el pedido, lo pasa a `En Preparación` y lo marca como `Listo para Recoger`.
* **Repartidor:** Recibe notificaciones de pedidos listos, acepta un viaje, recoge el pedido y lo marca como `Entregado`.
* **Sistema (Backend):** Orquesta la comunicación, ejecuta la lógica de negocio (asignación, cálculo de costos) y persiste los datos.

### Flujo de Operaciones Típico
~~~
1. CREACIÓN (Factory): Un Cliente crea un "Pedido" a través del sistema.
2. TRANSICIÓN (State): El "Restaurante" acepta el pedido. El estado cambia a "En Preparación".
3. BLOQUEO (State): El "Cliente" intenta "cancelar" el pedido, pero el sistema lo rechaza porque ya está en preparación.
4. TRANSICIÓN (State): El "Restaurante" termina el pedido. El estado cambia a "Listo para Recoger".
5. NOTIFICACIÓN (Observer): El "Pedido" (Sujeto) notifica a sus suscriptores:
    * El "Cliente" (Observador) recibe un push: "¡Tu pedido está listo!"
    * El "SistemaLogistico" (Observador) recibe el evento e inicia la asignación.
6. ASIGNACIÓN (Strategy): El sistema usa la "EstrategiaAsignarMasCercano" para encontrar un "Repartidor".
7. ENTREGA (State): El "Repartidor" acepta, recoge y entrega el pedido. El estado final es "Entregado".
8. CÁLCULO (Decorator): El sistema calcula el costo final "envolviendo" el costo base con "CostoPropina" y "CostoPrioritario".
9. CIERRE: El pedido se marca como finalizado.
~~~

## Características Principales

### Funcionalidades del Sistema

1.  **Gestión del Ciclo de Vida del Pedido (Patrón State)**
    * **Manejo de Transiciones de Estado:**
        * El `Pedido` se gestiona como una Máquina de Estados Finitos (ej. `Pendiente`, `EnPreparacion`, `EnCamino`, `Entregado`).
        * La lógica de negocio y las reglas de cada estado se encapsulan en clases separadas (ej. `EstadoPendiente`, `EstadoEnPreparacion`).
    * **Control de Acciones (Resolución de HU-1):**
        * El estado actual determina qué acciones son válidas.
        * Ejemplo `cancelar_pedido()`:
            * `EstadoPendiente`: La acción es **exitosa**. El pedido se cancela.
            * `EstadoEnPreparacion`: La acción es **rechazada**. El pedido no se puede cancelar.
        * La clase `Pedido` (el Modelo) se mantiene simple, delegando toda esta lógica a su objeto de estado.

2.  **Sistema de Notificaciones en Tiempo Real (Patrón Observer)**
    * **Mecanismo de Suscripción (Publicador/Suscriptor):**
        * El `Pedido` actúa como el "Sujeto" (Observable). Mantiene una lista de suscriptores.
        * Cualquier clase que implemente la interfaz `IObservador` (ej. `NotificadorCliente`, `ModuloLogistica`) puede suscribirse a un pedido.
    * **Desacoplamiento de Componentes (Resolución de HU-2):**
        * Cuando el `Pedido` cambia de estado (ej. `transicionar_a(EstadoEnCamino)`), llama a `notificar()`.
        * El `Pedido` no sabe *cómo* se notifica (push, email, SMS). Solo emite el evento.
        * Permite añadir nuevos "oyentes" (como un `DashboardDeAdmin`) sin modificar *nunca* la clase `Pedido`.

3.  **Gestión y Creación de Entidades (Patrón Factory Method)**
    * **Creación centralizada de Usuarios (Resolución de HU-4):**
        * Se utiliza una `UsuarioFactory` (o fábricas derivadas como `ClienteFactory`, `RepartidorFactory`) para instanciar objetos.
        * El `ServicioUsuarios` (Controlador) pide un usuario a la fábrica (ej. `fabrica.crear_usuario(...)`) sin acoplarse a las clases concretas.
    * **Creación de tipos específicos:**
        * `Cliente`: Creado con `nombre`, `email` y `direccion_predeterminada`.
        * `Repartidor`: Creado con `nombre`, `email`, `id_vehiculo` y `tipo_vehiculo`.
        * `AdminRestaurante`: Creado con `nombre`, `email` y `id_restaurante_asignado`.

4.  **Cálculo de Costos Dinámicos (Patrón Decorator)**
    * **Composición flexible de costos (Resolución de HU-3):**
        * Un `PedidoBase` implementa una interfaz `ICosto` con un método `get_costo()`.
        * El costo final es "envuelto" (decorado) por clases adicionales en tiempo de ejecución.
    * **Ejemplos de Decoradores:**
        * `CostoEnvioPrioritario(ICosto)`: Añade un monto fijo (ej. `$50`) al costo del componente envuelto.
        * `CostoPropina(ICosto)`: Añade un monto porcentual (ej. `10%`) al costo del componente envuelto.
    * **Evita explosión de clases:**
        * Permite apilar costos dinámicamente (ej. `Propina(Prioritario(PedidoBase))`).
        * No se necesita crear clases como `PedidoConPropinaYPrioridad`.

5.  **Lógica de Asignación Logística (Patrón Strategy)**
    * **Algoritmos de asignación intercambiables:**
        * Define una familia de algoritmos (Estrategias) para que el `SistemaLogistico` elija un repartidor.
        * El `ServicioLogistico` (Controlador) puede cambiar la estrategia dinámicamente (ej. usar una estrategia diferente en horas pico).
    * **Estrategias Concretas:**
        * `EstrategiaAsignarMasCercano`: Busca el `Repartidor` con menor distancia geográfica al restaurante.
        * `EstrategiaAsignarMasLibre`: Busca el `Repartidor` con menos pedidos activos en su cola.
        * `EstrategiaAsignarPorRating`: (Opcional) Busca el `Repartidor` mejor calificado disponible.