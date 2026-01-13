from datetime import date

class Licencia:
    def __init__(self,categoria:str,fecha_expedicion:date,fecha_expiracion:date)-> None:
            if categoria not in [ 'A2','C1', 'C2', 'C3']:
                raise ValueError("La categoría de la licencia debe ser una de las siguientes: 'A2', 'C1', 'C2', 'C3'")
            self._categoria = categoria
            if isinstance(fecha_expedicion, date):
                self._fecha_expedicion = fecha_expedicion
            else:
                raise ValueError("La fecha de expedición debe ser una fecha válida.")
            if not isinstance(fecha_expiracion, date):
                raise ValueError("La fecha de expiración debe ser una fecha válida.")
            if fecha_expiracion <= fecha_expedicion:
                raise ValueError("La fecha de expiración debe ser posterior a la fecha de expedición")
            if fecha_expiracion <= date.today():
                raise ValueError("La licencia está vencida. La fecha de expiración debe ser posterior a la fecha actual.")
            self._fecha_expiracion = fecha_expiracion
    #Getters para licencia
    @property
    def categoria(self) -> str:
        return self._categoria
    @property
    def fecha_expedicion(self) -> date:
        return self._fecha_expedicion
    @property 
    def fecha_expiracion(self)-> date:
        return self._fecha_expiracion

class Conductor :
    def __init__(self,nombre:str,cedula:str,categoria:str,fecha_expedicion:date,fecha_expiracion:date)-> None:
        if isinstance(nombre, str) and nombre.strip():
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if isinstance(cedula, str) and cedula.strip() and len(cedula) == 10 and cedula.isdigit():
            self._cedula = cedula
        else:
            raise ValueError("La cédula debe tener exactamente 10 dígitos numéricos.")
        self._licencia = Licencia(categoria,fecha_expedicion,fecha_expiracion)
    #Getters para la clase Conductor
    @property
    def nombre(self) -> str:
        return self._nombre
    @property
    def cedula(self) -> str:
        return self._cedula 
    @property
    def licencia(self) -> Licencia:
        return self._licencia

        