from datetime import date
from Conductor import Conductor

class Sistema_alerta:
    def __init__(self):
        pass
    
    def verificar_licencia_proxima_vencimiento(self, conductor: Conductor) -> dict:
        hoy = date.today()
        fecha_vencimiento = conductor.licencia.fecha_expiracion
        dias_restantes = (fecha_vencimiento - hoy).days 
        
        # Verificar en orden: vencidas primero, luego por vencer
        if dias_restantes < 0:
            return {
                "conductor": conductor.nombre,
                "dias_restantes": dias_restantes,
                "estado": "Vencida",
                "mensaje": f"La licencia del conductor {conductor.nombre} venció hace {abs(dias_restantes)} días."
            }
        elif dias_restantes == 0:
            return {
                "conductor": conductor.nombre,
                "dias_restantes": dias_restantes,
                "estado": "Vence hoy",
                "mensaje": f"La licencia del conductor {conductor.nombre} vence hoy."
            }
        elif dias_restantes <= 30:
            return {
                "conductor": conductor.nombre,
                "dias_restantes": dias_restantes,
                "estado": "Por vencer",
                "mensaje": f"La licencia del conductor {conductor.nombre} vence en {dias_restantes} días."
            }
        else:
            # Licencia vigente (más de 30 días) - no retornar alerta
            return None
    
    def listar_licencias_por_vencer(self, conductores: list) -> list:
        por_vencer = []
        for conductor in conductores:
            alerta = self.verificar_licencia_proxima_vencimiento(conductor)
            if alerta and alerta["estado"] == "Por vencer":
                por_vencer.append(alerta)
        return por_vencer
    
    def listar_licencias_vencidas(self, conductores: list) -> list:
        vencidas = []
        for conductor in conductores:
            alerta = self.verificar_licencia_proxima_vencimiento(conductor)
            if alerta and alerta["estado"] == "Vencida":
                vencidas.append(alerta)
        return vencidas
    
    def obtener_vehiculos_sin_conductor(self, vehiculos: list) -> list:
        sin_conductor = []
        for vehiculo in vehiculos:
            if vehiculo.conductor is None:
                sin_conductor.append(vehiculo)
        return sin_conductor
    
    def generar_reporte_conductores(self, conductores: list) -> list:
        reporte = []
        if not conductores:
            print("No hay conductores registrados en el sistema.")
            return reporte
        for conductor in conductores:
            reporte.append({
                "nombre": conductor.nombre,
                "cedula": conductor.cedula,
                "categoria licencia": conductor.licencia.categoria,
                "dias restantes": (conductor.licencia.fecha_expiracion - date.today()).days
            })
        return reporte