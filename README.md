##  Contexto del Dominio

### Problema que Resuelve

El sistema de **Gestión de Delivery** aborda los desafíos de la coordinación logística moderna, un dominio que requiere:

* **1. Manejo del Ciclo de Vida del Pedido:**
    * Un pedido no es un objeto estático; transiciona por múltiples estados (`Pendiente`, `En Preparación`, `Listo`, `En Camino`, `Entregado`).
    * Las acciones permitidas (ej. `cancelar`) deben fallar o tener éxito dependiendo del estado actual.

* **2. Coordinación de Actores en Tiempo Real:**
    * Existen tres roles (`Cliente`, `Restaurante`, `Repartidor`) que deben estar sincronizados sin estar fuertemente acoplados.
    * Un cambio de estado en el `Pedido` (hecho por el Restaurante) debe notificar automáticamente al `Cliente` y al `Sistema de Repartidores`.

* **3. Asignación Logística (Recursos):**
    * El sistema debe asignar un `Repartidor` disponible y cercano cuando un pedido está `Listo para Recoger`.
    * Requiere algoritmos intercambiables para decidir la asignación (ej. "más cercano" vs. "con menos pedidos").

* **4. Flexibilidad de Transacciones:**
    * El costo final de un pedido no es fijo; debe permitir agregar "extras" opcionales de forma dinámica (`Envío Prioritario`, `Propina`, `Seguro`).
    * Evitar una "explosión de clases" (`PedidoConPropina`, `PedidoPrioritario`, etc.).

* **5. Trazabilidad y Auditoría:**
    * Almacenamiento del historial de estados de un pedido.
    * Gestión de diferentes tipos de usuarios (`Cliente`, `Repartidor`) con diferentes propiedades.

### Actores del Sistema

* **Cliente:** Crea el pedido, paga, recibe notificaciones y puede (a veces) cancelar.
* **Restaurante:** Acepta el pedido, lo pasa a `En Preparación` y lo marca como `Listo para Recoger`.
* **Repartidor:** Recibe notificaciones de pedidos listos, acepta un viaje, recoge el pedido y lo marca como `Entregado`.
* **Sistema (Backend):** Orquesta la comunicación, ejecuta la lógica de negocio (asignación, cálculo de costos) y persiste los datos.

### Flujo de Operaciones Típico

1.  **CREACIÓN (Factory):** Un `Cliente` crea un `Pedido` a través del sistema.
2.  **TRANSICIÓN (State):** El `Restaurante` acepta el pedido. El estado cambia a `En Preparación`.
3.  **BLOQUEO (State):** El `Cliente` intenta `cancelar` el pedido, pero el sistema lo rechaza porque ya está en preparación.
4.  **TRANSICIÓN (State):** El `Restaurante` termina el pedido. El estado cambia a `Listo para Recoger`.
5.  **NOTIFICACIÓN (Observer):** El `Pedido` (Sujeto) notifica a sus suscriptores:
    * El `Cliente` (Observador) recibe un push: "¡Tu pedido está listo!"
    * El `SistemaLogistico` (Observador) recibe el evento e inicia la asignación.
6.  **ASIGNACIÓN (Strategy):** El sistema usa la `EstrategiaAsignarMasCercano` para encontrar un `Repartidor`.
7.  **ENTREGA (State):** El `Repartidor` acepta, recoge y entrega el pedido. El estado final es `Entregado`.
8.  **CÁLCULO (Decorator):** El sistema calcula el costo final "envolviendo" el costo base con `CostoPropina` y `CostoPrioritario`.
9.  **CIERRE:** El pedido se marca como finalizado.