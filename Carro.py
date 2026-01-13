from Vehiculo import Vehiculo
from Conductor import Conductor
from Movible import Movible
from datetime import date

class Carro(Vehiculo, Movible):

    def __init__(self, marca: str, modelo: str, anio: int, placa: str,
                 cilindraje: int, tipo_combustible: str, potencia: int | float,
                 fecha_revision_tecnomecanica: date,
                 conductor: Conductor | None = None) -> None:

        super().__init__(marca, modelo, anio, placa, cilindraje,
                         tipo_combustible, potencia, conductor)

        self._categorias_licencia_requeridas = ['C1']

        if not isinstance(fecha_revision_tecnomecanica, date):
            raise ValueError("La fecha de revisión tecnomecánica debe ser una fecha válida.")
        if fecha_revision_tecnomecanica <= date.today():
            raise ValueError("La fecha de revisión tecnomecánica debe estar vigente.")

        self._fecha_revision_tecnomecanica = fecha_revision_tecnomecanica

    @property
    def fecha_revision_tecnomecanica(self) -> date:
        return self._fecha_revision_tecnomecanica

    @fecha_revision_tecnomecanica.setter
    def fecha_revision_tecnomecanica(self, nueva_fecha: date) -> None:
        if not isinstance(nueva_fecha, date):
            raise ValueError("La nueva fecha debe ser válida.")
        if nueva_fecha <= date.today():
            raise ValueError("La revisión tecnomecánica debe estar vigente.")
        self._fecha_revision_tecnomecanica = nueva_fecha

    def tecnomecanica_vigente(self) -> bool:
        return self._fecha_revision_tecnomecanica > date.today()

    def mover(self) -> str:
        return f"El carro de placas {self.placa} se está moviendo por la ciudad"

    def iniciar_jornada(self) -> None:
        if self.conductor is None:
            raise ValueError("No hay conductor asignado")
        if not self.puede_ser_conducido_por(self.conductor):
            raise ValueError("Licencia no válida para este carro")
        if not self.tecnomecanica_vigente():
            raise ValueError("Revisión tecnomecánica vencida")
        print(f"La jornada del carro {self.placa} ha comenzado.")

    def finalizar_jornada(self) -> None:
        if self.conductor is None:
            raise ValueError("No hay conductor asignado")
        if not self.puede_ser_conducido_por(self.conductor):
            raise ValueError("Licencia no válida para este carro")
        print(f"La jornada del carro {self.placa} ha finalizado.")