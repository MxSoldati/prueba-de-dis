# /main.py
# -----------------------------------------------------------------
# VISTA (MAIN) - Simulación del Sistema de Delivery
# -----------------------------------------------------------------
# ¡VERSIÓN FINAL CON MANEJO DE EXCEPCIONES!

from parcial_delivery.servicios.pedidos.servicio_pedidos import ServicioPedidos
from parcial_delivery.servicios.usuarios.servicio_usuarios import ServicioUsuarios
from parcial_delivery.servicios.logistica.servicio_logistica import ServicioLogistica
from parcial_delivery.patrones.strategy.impl.estrategia_asignar_mas_cercano import EstrategiaAsignarMasCercano
from parcial_delivery.patrones.strategy.impl.estrategia_asignar_mas_libre import EstrategiaAsignarMasLibre
from parcial_delivery.entidades.usuarios.repartidor import Repartidor
from parcial_delivery.notificaciones.notificador_cliente import NotificadorCliente

# --- ¡NUEVA IMPORTACIÓN PARA CAPTURAR EL ERROR! ---
from parcial_delivery.excepciones.pedido_exception import PedidoCancelacionException
# -------------------------------------------------

def imprimir_encabezado(titulo: str):
    print("\n" + "=" * 80)
    print(f"|| {titulo.upper()} ||")
    print("=" * 80)

def imprimir_patron(nombre: str, descripcion: str):
    print(f"\n   [... Aplicando Patrón {nombre.upper()} ...]")
    print(f"   [... {descripcion} ...]")

# -----------------------------------------------------------------
# INICIO DE LA SIMULACIÓN
# -----------------------------------------------------------------

imprimir_encabezado("Inicio de Simulación: Sistema de Pedidos (TODOS LOS PATRONES)")

# --- 0. Inicializar Controladores ---
print("\n[VISTA] -> Inicializando Controladores...")
servicio_pedidos = ServicioPedidos()
servicio_usuarios = ServicioUsuarios()

# --- 1. Demostración Patrón Factory (HU-4) ---
imprimir_patron("FACTORY METHOD", "HU-4: Creando usuarios (Clientes y Repartidores)")
cliente_1 = servicio_usuarios.crear_usuario(
    tipo="Cliente", nombre="Valentín", email="valentin@email.com",
    direccion="Calle Falsa 123", telefono="261-456-7890"
)
cliente_2 = servicio_usuarios.crear_usuario(
    tipo="Cliente", nombre="Alberto (Profe)", email="alberto@email.com",
    direccion="Av. Siempre Viva 742", telefono="261-111-2222"
)
repartidor_A = servicio_usuarios.crear_usuario(
    tipo="Repartidor", nombre="Repartidor Juan", email="juan@delivery.com",
    tipo_vehiculo="Moto", ubicacion=(10, 10), pedidos_activos=1
)
repartidor_B = servicio_usuarios.crear_usuario(
    tipo="Repartidor", nombre="Repartidor Ana", email="ana@delivery.com",
    tipo_vehiculo="Bicicleta", ubicacion=(2, 2), pedidos_activos=5
)
lista_repartidores = [repartidor_A, repartidor_B]
print(f"[VISTA] -> Clientes y Repartidores creados.")

print("\n" + "-" * 80)

# --- 2. Prueba de cancelación (exitosa) (HU-1) ---
imprimir_patron("STATE", "HU-1: Probando cancelación en estado 'Pendiente'")
pedido_1 = servicio_pedidos.crear_pedido(
    cliente=cliente_1, items=["Pizza Muzza"], costo_base=1000.0, ubicacion_restaurante=(1,1)
)
print(f"\n[VISTA] -> Solicitando al servicio cancelar el pedido {pedido_1.id_pedido}...")
try:
    servicio_pedidos.cancelar_pedido(pedido_1.id_pedido)
except PedidoCancelacionException as e:
    print(f"\n   [¡ERROR CAPTURADO!] -> {e}")
print(f"[VISTA] -> Consultando estado: {servicio_pedidos.get_estado_pedido(pedido_1.id_pedido)}")


print("\n" + "-" * 80)

# --- 3. Prueba de Observer (HU-2) y State (HU-1) ---
imprimir_patron("STATE / OBSERVER", "HU-1 y HU-2: Flujo de pedido con notificaciones")
pedido_2 = servicio_pedidos.crear_pedido(
    cliente=cliente_2, items=["Lomo Completo"], costo_base=1500.0, ubicacion_restaurante=(1,1)
)
print(f"[VISTA] -> Pedido {pedido_2.id_pedido} creado.")

# Suscribir Observer (HU-2)
imprimir_patron("OBSERVER", "HU-2: Suscribiendo un Notificador al pedido 102")
notificador_profe = NotificadorCliente(cliente_telefono=cliente_2.telefono)
print(f"\n[VISTA] -> Solicitando al servicio suscribir el Notificador al pedido 102...")
servicio_pedidos.suscribir_a_pedido(pedido_2.id_pedido, notificador_profe)

# Avanzar Estado (Dispara Observer)
print("\n[VISTA] -> Solicitando al servicio AVANZAR el pedido 102 (Restaurante acepta)...")
servicio_pedidos.avanzar_estado_pedido(102)

# --- ¡SECCIÓN MODIFICADA CON TRY...EXCEPT! ---
# Probar cancelación (HU-1)
print(f"\n[VISTA] -> Solicitando al servicio CANCELAR el pedido {pedido_2.id_pedido} (HU-1)...")
try:
    servicio_pedidos.cancelar_pedido(pedido_2.id_pedido)
except PedidoCancelacionException as e:
    print(f"\n   [¡ERROR CAPTURADO POR LA VISTA!] -> {e}")
# ---------------------------------------------
print(f"[VISTA] -> Consultando estado: {servicio_pedidos.get_estado_pedido(pedido_2.id_pedido)}")

print("\n" + "-" * 80)

# --- 4. Prueba Patrón Decorator (HU-3) ---
imprimir_patron("DECORATOR", "HU-3: Calculando costo final con extras")
print(f"\n[VISTA] -> El costo base del pedido {pedido_2.id_pedido} es ${pedido_2.costo_base}")
extras_a_calcular = [{"tipo": "prioritario"}, {"tipo": "propina", "valor": 0.10}]
costo_final, descripcion = servicio_pedidos.calcular_costo_final(pedido_2.id_pedido, extras_a_calcular)
print(f"[VISTA] -> Cálculo recibido: {descripcion} | Costo Final: ${costo_final}")

print("\n" + "-" * 80)

# --- 5. Prueba Patrón Strategy (HU-5) ---
imprimir_patron("STRATEGY", "HU-5: Asignando repartidor con algoritmos intercambiables")
estrategia_cercania = EstrategiaAsignarMasCercano()
servicio_logistica = ServicioLogistica(estrategia_default=estrategia_cercania)

print(f"\n[VISTA] -> (El Pedido {pedido_2.id_pedido} está en {pedido_2.ubicacion_restaurante})")
print(f"[VISTA] -> (Repartidor Juan está en {repartidor_A.ubicacion} con {repartidor_A.pedidos_activos} pedido)")
print(f"[VISTA] -> (Repartidor Ana está en {repartidor_B.ubicacion} con {repartidor_B.pedidos_activos} pedidos)")

print("\n[VISTA] -> Solicitando asignación con Estrategia 'Más Cercano'...")
repartidor_asignado_1 = servicio_logistica.asignar_repartidor_a_pedido(pedido_2, lista_repartidores)
print(f"[VISTA] -> Repartidor asignado: {repartidor_asignado_1.nombre}")

# Cambiar la estrategia en caliente
estrategia_libres = EstrategiaAsignarMasLibre()
servicio_logistica.set_estrategia_asignacion(estrategia_libres)

print("\n[VISTA] -> Solicitando asignación con Estrategia 'Más Libre'...")
repartidor_asignado_2 = servicio_logistica.asignar_repartidor_a_pedido(pedido_2, lista_repartidores)
print(f"[VISTA] -> Repartidor asignado: {repartidor_asignado_2.nombre}")

# --- FIN DE LA SIMULACIÓN ---
imprimir_encabezado("Fin de la Simulación (TODOS LOS PATRONES Y EXCEPCIONES DEMOSTRADOS)")
print("\n   ✓ Demostrado: El Patrón FACTORY crea diferentes usuarios (Cliente, Repartidor).")
print("   ✓ Demostrado: El Patrón STATE lanza 'PedidoCancelacionException' al intentar cancelar.")
print("   ✓ Demostrado: La VISTA (main.py) captura la excepción de forma controlada.")
print("   ✓ Demostrado: El Patrón OBSERVER notifica automáticamente al cliente.")
print("   ✓ Demostrado: El Patrón DECORATOR 'envuelve' el costo base con extras dinámicos.")
print("   ✓ Demostrado: El Patrón STRATEGY intercambia algoritmos de asignación (Cercano vs. Libre).\n")