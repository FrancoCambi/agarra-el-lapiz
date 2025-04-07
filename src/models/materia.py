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
        self.parciales.append(parcial)

        if len(self.parciales) >= 2:
            self.parciales.sort(key=len)

    def agregar_tp(self, tp: Tp) -> None:
        self.tps.append(tp)

        if len(self.tps) >= 2:
            self.tps.sort(key=len)

    def mostrar_parciales(self) -> None:

        print(f"Parciales de {self.nombre}:\n")

        for i in range(len(self.parciales)):
            print(f"Parcial {i + 1}: {self.parciales[i].fecha}, nota: {self.parciales[i].nota if self.parciales[i].nota != -1 else "No hay nota."}")