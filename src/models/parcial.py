from datetime import date


class Parcial:
    """Clase que simula un parcial de la facultad, conteniendo su fecha y nota.
    \nDonde:
            Nota = -1 significa que aún no hay nota
    """
    def __init__(self, fecha: date, nota: int = -1):
        self.fecha = fecha
        self.nota = nota

    def __len__(self):
        """Este metodo sobreescribe a len() para que devuelva cuantos dias faltan para
        el percial.

        Args:
            parcial (Parcial): Parcial deseado
        Returns:
            int: Cantidad de dias que faltan para el parcial
        """
        return (self.fecha - date.today()).days