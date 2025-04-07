from .tp import Tp
from .parcial import Parcial


class Materia:
    """Clase que simula una materia de la facultad, conteniendo su nombre, parciales y tp's.
    """

    def __init__(self, nombre: str, parciales: list[Parcial] = [], tps: list[Tp] = []):
        self.nombre = nombre
        self.parciales = parciales
        self.tps = tps

    def agregar_parcial(self, parcial: Parcial) -> None:
        """Agrega un parcial a la materia, de manera ordenada segun su fecha.

        Args:
            parcial (Parcial):
        """

        # Agrego el parcial a la lista
        self.parciales.append(parcial)

        # Si hay más de dos, ordeno la lista dependiendo su "len", que devuelve la cantidad de dias
        # que faltan para el parcial
        if len(self.parciales) >= 2:
            self.parciales.sort(key=len)

    def agregar_tp(self, tp: Tp) -> None:
        """Agrega un tp a la materia, de manera ordenada segun su fecha de entrega.

        Args:
            tp (Tp):
        """

        # Agrego el tp a la lists
        self.tps.append(tp)

        # Si hay más de dos, ordeno la lista dependiendo su "len", que devuelve la cantidad de dias
        # que faltan para su entrega.
        if len(self.tps) >= 2:
            self.tps.sort(key=len)

    def mostrar_parciales(self) -> None:
        """Muesta de manera ordenada los parciales de la materia.
        """

        # Muestro un título
        print(f"Parciales de {self.nombre}:\n")

        # Muestro cada parcial con su fecha y nota si corresponde.
        for i in range(len(self.parciales)):
            print(f"Parcial {i + 1}: {self.parciales[i].fecha}, nota: {self.parciales[i].nota if self.parciales[i].nota != -1 else "No hay nota."}")