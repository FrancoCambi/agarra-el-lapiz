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
    
    def cargar_nota(self, nota: int) -> None:
        """Este metodo recibe una nota y la asocia al evaluable.

        Args:
            nota (int): Nota del evaluable
        """

        # Se crea este metodo innecesario por ahora, por si luego se necesitan
        # realizar mas cosas al cargar una nota.


        # Cargo la nota
        self.nota = nota
