"""
Sistema de Gestión de Vehículos y Conductores
Transporte Seguro S.A.

Demuestra todas las funcionalidades del sistema:
- Creación de conductores con validación de licencias
- Creación de vehículos (Moto, Carro, Camión)
- Asignación de conductores a vehículos
- Inicio y finalización de jornadas
- Sistema de alertas para licencias próximas a vencer
- Relaciones de Composición (Motor, Licencia) y Agregación (Conductor-Vehículo)
"""

from datetime import date
from Conductor import Conductor
from Moto import Moto
from Carro import Carro
from Camion import Camion
from Sistema_alerta import Sistema_alerta


def demo_creacion_conductores():
    """Demuestra la creación de conductores con diferentes estados de licencia"""
    print("\n\n1. CREACIÓN DE CONDUCTORES\n")
    
    # Conductor 1: Licencia vigente (vence en marzo 2026)
    conductor1 = Conductor(
        nombre="Juan Pérez",
        cedula="1234567890",
        categoria="A2",
        fecha_expedicion=date(2024, 1, 15),
        fecha_expiracion=date(2026, 3, 15)
    )
    print(f"Conductor creado: {conductor1.nombre}")
    print(f"   Cédula: {conductor1.cedula}")
    print(f"   Licencia: {conductor1.licencia.categoria}")
    print(f"   Vence: {conductor1.licencia.fecha_expiracion}")
    
    # Conductor 2: Licencia por vencer (febrero 2026)
    conductor2 = Conductor(
        nombre="María González",
        cedula="0987654321",
        categoria="C1",
        fecha_expedicion=date(2024, 6, 1),
        fecha_expiracion=date(2026, 2, 1)
    )
    print(f"\nConductor creado: {conductor2.nombre}")
    print(f"   Cédula: {conductor2.cedula}")
    print(f"   Licencia: {conductor2.licencia.categoria}")
    print(f"   Vence: {conductor2.licencia.fecha_expiracion}")
    
    # Conductor 3: Licencia vigente para camión (mayo 2026)
    conductor3 = Conductor(
        nombre="Carlos Ramírez",
        cedula="1122334455",
        categoria="C2",
        fecha_expedicion=date(2023, 3, 10),
        fecha_expiracion=date(2026, 5, 10)
    )
    print(f"\nConductor creado: {conductor3.nombre}")
    print(f"   Cédula: {conductor3.cedula}")
    print(f"   Licencia: {conductor3.licencia.categoria}")
    print(f"   Vence: {conductor3.licencia.fecha_expiracion}")
    
    return [conductor1, conductor2, conductor3]


def demo_creacion_vehiculos():
    """Demuestra la creación de diferentes tipos de vehículos"""
    print("\n\n2. CREACIÓN DE VEHÍCULOS\n")
    
    # MOTO
    print("MOTO:")
    moto = Moto(
        marca="Yamaha",
        modelo="FZ-16",
        anio=2023,
        placa="ABC123",
        cilindraje=150,
        tipo_combustible="gasolina",
        potencia=14.5,
        casco=True
    )
    print(f"   Marca: {moto.marca} {moto.modelo}")
    print(f"   Placa: {moto.placa}")
    print(f"   Motor: {moto.motor.cilindraje}cc, {moto.motor.potencia}HP")
    print(f"   Casco: {'Sí' if moto.casco else 'No'}")
    print(f"   Licencia requerida: A2")
    
    # CARRO
    print("\nCARRO:")
    carro = Carro(
        marca="Toyota",
        modelo="Corolla",
        anio=2022,
        placa="XYZ789",
        cilindraje=1800,
        tipo_combustible="gasolina",
        potencia=140,
        fecha_revision_tecnomecanica=date(2026, 4, 15)
    )
    print(f"   Marca: {carro.marca} {carro.modelo}")
    print(f"   Placa: {carro.placa}")
    print(f"   Motor: {carro.motor.cilindraje}cc, {carro.motor.potencia}HP")
    print(f"   Revisión técnica vence: {carro.fecha_revision_tecnomecanica}")
    print(f"   Licencia requerida: C1")
    
    # CAMIÓN
    print("\nCAMIÓN:")
    camion = Camion(
        marca="Freightliner",
        modelo="Cascadia",
        anio=2021,
        placa="TRK456",
        cilindraje=6700,
        tipo_combustible="diesel",
        potencia=450,
        planilla_carga="PC-2026-001234",
        peso_maximo=20.5
    )
    print(f"   Marca: {camion.marca} {camion.modelo}")
    print(f"   Placa: {camion.placa}")
    print(f"   Motor: {camion.motor.cilindraje}cc, {camion.motor.potencia}HP")
    print(f"   Planilla: {camion.planilla_carga}")
    print(f"   Peso máximo: {camion.peso_maximo} toneladas")
    print(f"   Licencia requerida: C2 o C3")
    
    return [moto, carro, camion]


def demo_asignacion_conductores(vehiculos, conductores):
    """Demuestra la asignación de conductores a vehículos"""
    print("\n\n3. ASIGNACIÓN DE CONDUCTORES A VEHÍCULOS\n")
    
    moto, carro, camion = vehiculos
    conductor1, conductor2, conductor3 = conductores
    
    # Asignar conductor a moto
    print("Asignando conductor a MOTO...")
    moto.asignar_conductor(conductor1)
    print(f"   {conductor1.nombre} asignado a moto {moto.placa}")
    print(f"   Puede conducirla: {moto.puede_ser_conducido_por(conductor1)}")
    
    # Asignar conductor a carro
    print("\nAsignando conductor a CARRO...")
    carro.asignar_conductor(conductor2)
    print(f"   {conductor2.nombre} asignado a carro {carro.placa}")
    print(f"   Puede conducirlo: {carro.puede_ser_conducido_por(conductor2)}")
    
    # Asignar conductor a camión
    print("\nAsignando conductor a CAMIÓN...")
    camion.asignar_conductor(conductor3)
    print(f"   {conductor3.nombre} asignado a camión {camion.placa}")
    print(f"   Puede conducirlo: {camion.puede_ser_conducido_por(conductor3)}")


def demo_jornadas_trabajo(vehiculos):
    """Demuestra inicio y finalización de jornadas"""
    print("\n\n4. JORNADAS DE TRABAJO\n")
    
    moto, carro, camion = vehiculos
    
    # Iniciar jornadas
    print("INICIANDO JORNADAS:\n")
    
    moto.iniciar_jornada()
    carro.iniciar_jornada()
    camion.iniciar_jornada()
    
    # Demostrar movimiento (polimorfismo)
    print("\nVEHÍCULOS EN MOVIMIENTO (Polimorfismo):\n")
    for vehiculo in vehiculos:
        print(f"   {vehiculo.mover()}")
    
    # Finalizar jornadas
    print("\nFINALIZANDO JORNADAS:\n")
    
    moto.finalizar_jornada()
    carro.finalizar_jornada()
    camion.finalizar_jornada()


def demo_sistema_alertas(vehiculos, conductores):
    """Demuestra el sistema de alertas"""
    print("\n\n5. SISTEMA DE ALERTAS\n")
    
    sistema = Sistema_alerta()
    
    # Verificar licencias individuales
    print("VERIFICACIÓN DE LICENCIAS:\n")
    for conductor in conductores:
        alerta = sistema.verificar_licencia_proxima_vencimiento(conductor)
        if alerta:
            print(f"   {alerta['mensaje']}")
        else:
            dias = (conductor.licencia.fecha_expiracion - date.today()).days
            print(f"   {conductor.nombre}: Licencia vigente ({dias} días)")
    
    # Listar licencias por vencer
    print("\nLICENCIAS POR VENCER (30 días o menos):\n")
    por_vencer = sistema.listar_licencias_por_vencer(conductores)
    if por_vencer:
        for alerta in por_vencer:
            print(f"   {alerta['conductor']}: {alerta['dias_restantes']} días")
    else:
        print("   No hay licencias por vencer")
    
    # Vehículos sin conductor
    print("\nVEHÍCULOS SIN CONDUCTOR:\n")
    sin_conductor = sistema.obtener_vehiculos_sin_conductor(vehiculos)
    if sin_conductor:
        for v in sin_conductor:
            print(f"   {v.__class__.__name__} {v.placa}")
    else:
        print("   Todos los vehículos tienen conductor asignado")
    
    # Reporte de conductores
    print("\nREPORTE DE CONDUCTORES:\n")
    reporte = sistema.generar_reporte_conductores(conductores)
    for info in reporte:
        print(f"   {info['nombre']} ({info['cedula']})")
        print(f"   Licencia: {info['categoria licencia']}")
        print(f"   Vence en: {info['dias restantes']} días\n")


def main():
    """Función principal que ejecuta todas las demostraciones"""
    print("\n" + "="*60)
    print("  SISTEMA DE GESTIÓN DE VEHÍCULOS Y CONDUCTORES")
    print("  Transporte Seguro S.A.")
    print("="*60)
    
    # 1. Crear conductores
    conductores = demo_creacion_conductores()
    
    # 2. Crear vehículos
    vehiculos = demo_creacion_vehiculos()
    
    # 3. Asignar conductores
    demo_asignacion_conductores(vehiculos, conductores)
    
    # 4. Jornadas de trabajo
    demo_jornadas_trabajo(vehiculos)
    
    # 5. Sistema de alertas
    demo_sistema_alertas(vehiculos, conductores)
    
 
    print(" \n\n DEMOSTRACIÓN COMPLETADA EXITOSAMENTE")
    

if __name__ == "__main__":
    main()