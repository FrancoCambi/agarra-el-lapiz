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