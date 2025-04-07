from datetime import date

class Tp:
    """Clase que simula un trabajo practico de la facultad, conteniendo su fecha y nota.
    \nDonde:
            Nota = -1 significa que aún no hay nota    
    """
    def __init__(self, fecha: date, nota: int = -1):
        self.fecha = fecha
        self.nota = nota

    def __len__(self):
        """Este metodo sobreescribe a len() para que devuelva cuantos dias faltan para
        la entrega del tp.

        Args:
            Tp (Tp): Tp deseado
        Returns:
            int: Cantidad de dias que faltan para la entrega del tp.
        """
        return (self.fecha - date.today()).days