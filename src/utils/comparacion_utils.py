from models.parcial import Parcial
from datetime import date

def parcial_len(parcial: Parcial) -> int:
    """Esta función recibe un parcial y devuelve cuantos dias faltan para el mismo,
    para ser usada en la funcion str.sort como key.

    Args:
        parcial (Parcial): Parcial deseado
    Returns:
        int: Cantidad de dias que faltan para el parcial
    """
    return parcial.fecha - date.today()