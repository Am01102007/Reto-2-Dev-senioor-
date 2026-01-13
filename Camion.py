from Vehiculo import Vehiculo
from Conductor import Conductor
from Movible import Movible
class Camion(Vehiculo,Movible):
    def __init__(self, marca: str, modelo: str, anio: int, placa: str, cilindraje: int, tipo_combustible: str, potencia: int | float,
            planilla_carga:str,peso_maximo:int | float, conductor: Conductor | None = None) -> None:
        super().__init__(marca, modelo, anio, placa, cilindraje, tipo_combustible, potencia, conductor)
        self._categorias_licencia_requeridas = ['C2', 'C3']
        if not isinstance(planilla_carga, str):
            raise ValueError("La planilla de carga debe ser una cadena de texto.")
        if len(planilla_carga.strip()) < 10:
            raise ValueError("La planilla debe tener al menos 10 caracteres")        
        self._planilla_carga = planilla_carga
        if not isinstance(peso_maximo,(int,float)) or peso_maximo <= 0:
            raise ValueError("El peso máximo debe ser un número entero positivo.")
        self._peso_maximo = peso_maximo
    #Getters para la clase Camion
    @property
    def planilla_carga(self) -> str:
        return self._planilla_carga
    @property
    def peso_maximo(self) -> int | float:
        return self._peso_maximo
    #setter para la clase Camion
    @planilla_carga.setter
    def planilla_carga(self, nueva_planilla: str) -> None:
        if not isinstance(nueva_planilla, str):
            raise ValueError("La planilla de carga debe ser una cadena de texto.")
        if len(nueva_planilla.strip()) < 10:
            raise ValueError("La planilla debe tener al menos 10 caracteres")        
        self._planilla_carga = nueva_planilla
    
    def iniciar_jornada(self) -> None:
        if self.conductor is None:
            raise ValueError("No hay un conductor asignado al camión, por tanto no puede iniciar la jornada")
        if not self.puede_ser_conducido_por(self.conductor):
            raise ValueError("El conductor no tiene la licencia adecuada para conducir este camión.")
        print(f"La jornada de conducción del camión {self.placa} ha comenzado.")
    
    def finalizar_jornada(self) -> None:
        if self.conductor is None:
            raise ValueError("No hay un conductor asignado al camión, por tanto no tiene jornada activa para finalizar")
        if not self.puede_ser_conducido_por(self.conductor):
            raise ValueError("El conductor no tiene la licencia adecuada para conducir este camión, por lo tanto no tiene jornada activa que finalizar.")
        print(f"La jornada de conducción del camión {self.placa} ha finalizado.")
        
    def mover(self) -> str:
       return f"El camión de placas {self.placa} se desplaza transportando carga por la carretera"