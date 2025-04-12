from datetime import date

from .enums import TipoEvaluable


class Evaluable:
    """Clase que simula un parcial o tp de la facultad, conteniendo su fecha y nota.
    \nDonde:
            Nota = -1 significa que aún no hay nota
    """
    def __init__(self, tipo: TipoEvaluable, fecha: date, nota: int = -1):
        self.tipo = tipo
        self.fecha = fecha
        self.nota = nota

    def __len__(self):
        """Este metodo sobreescribe a len() para que devuelva cuantos dias faltan para
        el percial/tp.

        Args:
            evaluable (Evaluable): evaluable deseado
        Returns:
            int: Cantidad de dias que faltan para el parcial/tp
        """
        return (self.fecha - date.today()).days
    
    def __str__(self):
        """Este metodo sobreescribe a print() para que cuando se trata de
        printear un objeto de tipo Evaluable, se ejecute este codigo
        """

        return f"Fecha: {self.fecha}, nota: {self.nota if self.nota else "No hay nota"}"
    
    def to_dict(self):
        """Transforma un evaluable a diccionario

        Returns:
            _type_:
        """

        return {"tipo": self.tipo.value,
                "fecha": self.fecha.isoformat(),
                "nota": self.nota}
    
    @classmethod
    def from_dict(cls, data):
        tipo = TipoEvaluable(data["tipo"])
        fecha = date.fromisoformat(data["fecha"])
        nota = data["nota"]
        return cls(tipo, fecha, nota)
    
    def cargar_nota(self, nota: int) -> None:
        """Este metodo recibe una nota y la asocia al evaluable.

        Args:
            nota (int): Nota del evaluable
        """

        # Se crea este metodo (un tanto innecesario por ahora), por si luego se necesitan
        # realizar mas cosas al cargar una nota.

        # Si se pasa una nota sin sentido, se da un error
        if nota < 0:
            raise ValueError("La nota de un evaluable no puede ser negativa")

        # Cargo la nota
        self.nota = nota

    def cambiar_fecha(self, nueva_fecha: date) -> None:
        """Este metodo funciona de setter de fecha.

        Args:
            nueva_fecha (date): Fecha que reemplaza la anterior
        """

        # Si el dia ya paso, damos un error.
        if (nueva_fecha < date.today()):
            raise ValueError("La nueva fecha del evaluable no puede ser un dia que ya paso.")
        
        # Cambiamos la fecha
        self.fecha = nueva_fecha

        