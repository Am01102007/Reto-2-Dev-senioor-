from Vehiculo import Vehiculo
from Conductor import Conductor
from Movible import Movible
class Moto(Vehiculo, Movible):
    def __init__(self, marca: str, modelo: str, anio: int, placa: str, cilindraje: int, tipo_combustible: str, potencia: int | float,
            casco:bool, conductor: Conductor | None = None)  -> None:
        super().__init__(marca, modelo, anio, placa, cilindraje, tipo_combustible, potencia, conductor)
        self._categorias_licencia_requeridas = ['A2']
        if isinstance(casco, bool):
            self._casco = casco
        else:
            raise ValueError("El valor de casco debe ser un valor verdadero o falso.")
    #Getter para la clase Moto
    @property
    def casco(self) -> bool:
        return self._casco
    #Setter para la clase Moto
    @casco.setter
    def casco(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self._casco = valor
        else:
            raise ValueError("El valor de casco debe ser verdadero o falso.")
    def iniciar_jornada(self) -> None:
        if self.conductor is None:
            raise ValueError("No hay un conductor asignado a la moto, por tanto no puede iniciar la jornada")
        if not self.puede_ser_conducido_por(self.conductor):
            raise ValueError("El conductor no tiene la licencia adecuada para conducir esta moto.")
        if not self._casco:
            raise ValueError("El conductor debe usar casco para iniciar la jornada de conducción.")
        print(f"La jornada de conducción de la moto {self.placa} ha comenzado.")
        
    def finalizar_jornada(self) -> None:
        if self.conductor is None:
            raise ValueError("No hay un conductor asignado a la moto, por tanto no tiene jornada activa para finalizar")
        if not self.puede_ser_conducido_por(self.conductor):
            raise ValueError("El conductor no tiene la licencia adecuada para conducir esta moto, por lo tanto no tiene jornada activa que finalizar.")
        print(f"La jornada de conducción de la moto {self.placa} ha finalizado.")
        
    def mover(self) -> str:
        return f"La moto {self.placa} se está moviendo"