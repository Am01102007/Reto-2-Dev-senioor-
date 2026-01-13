from abc import ABC, abstractmethod
from datetime import date
from Conductor import Conductor

class Motor:
    def __init__(self, cilindraje: int, tipo_combustible: str, potencia: int|float):
        if isinstance(cilindraje, int) and 50 <= cilindraje <= 8000:
            self._cilindraje = cilindraje
        else:
            raise ValueError("El cilindraje debe estar entre 50cc y 8000cc.")
        if isinstance(tipo_combustible, str) and tipo_combustible.strip():
            self._tipo_combustible = tipo_combustible
        else:
            raise ValueError("El tipo de combustible debe ser una cadena no vacía.")
        if isinstance(potencia, (int, float)) and potencia > 0:
            self._potencia = potencia
        else:
            raise ValueError("La potencia debe ser un número positivo.")
    #Getters para la clase Motor
    @property
    def cilindraje(self) -> int:
        return self._cilindraje
    @property
    def tipo_combustible(self) -> str:
        return self._tipo_combustible
    @property
    def potencia(self) -> int | float:
        return self._potencia
    
class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str, anio: int, placa: str, cilindraje: int, tipo_combustible: str, potencia: int | float,
             conductor: Conductor | None = None)  -> None:
        
        if isinstance(marca, str) and marca.strip():
            self._marca = marca
        else:
            raise ValueError("La marca debe ser una cadena no vacía.")
        if isinstance(modelo, str) and modelo.strip():
            self._modelo = modelo
        else:
            raise ValueError("El modelo debe ser una cadena no vacía.")
        if isinstance(anio, int) and anio > 1900 and anio <= date.today().year + 1:
            self._anio = anio
        else:
            raise ValueError(f"El año debe ser un entero entre 1900 y {date.today().year + 1}.")
        if isinstance(placa, str) and placa.strip() and 5 <= len(placa) <= 6:
            self._placa = placa
        else:
            raise ValueError("La placa debe ser una cadena no vacía y tener mínimo una longitud de 5 y máximo de 6 caracteres.")
        if isinstance(conductor, Conductor) or conductor is None:
            self._conductor = conductor
        else:
            raise ValueError("El conductor debe ser una instancia de Conductor o None.")
        self._motor = Motor(cilindraje, tipo_combustible, potencia)
        self._categorias_licencia_requeridas = []
    #Getters para la clase Vehiculo  
    @property
    def marca(self) -> str:
        return self._marca
    @property
    def modelo(self) -> str:
        return self._modelo     
    @property
    def anio(self) -> int:
        return self._anio
    @property
    def placa(self) -> str:
        return self._placa
    @property
    def conductor(self) -> Conductor | None:
        return self._conductor
    @property
    def motor(self)-> Motor:
        return self._motor
    
    def asignar_conductor(self, conductor: Conductor) -> None:
        if not isinstance(conductor, Conductor):
            raise ValueError("El conductor debe ser una instancia válida de Conductor.")
        
        if self._conductor is not None:
            raise ValueError("El vehículo ya tiene un conductor asignado")
        
        self._conductor = conductor
        
    def puede_ser_conducido_por(self, conductor: Conductor) -> bool:
        if conductor is None:
            return False
        categoria_conductor = conductor.licencia.categoria
        return categoria_conductor in self._categorias_licencia_requeridas

    @abstractmethod
    def iniciar_jornada(self)-> None:
        pass
    @abstractmethod
    def finalizar_jornada(self)-> None:
        pass
    