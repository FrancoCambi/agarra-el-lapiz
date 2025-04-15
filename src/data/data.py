import json
import os

from models import Materia, TipoData

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Data():
    """Esta clase sera la encargada de guardar y cargar los datos
    del programa.
    """
    
    def __init__(self):

        self.data: dict[str, list] = {TipoData.MATERIAS: []}

    def agregar_materia(self, materia: Materia) -> None:
        """Esta funcion recibe una materia y la agrega a la lista
        de materias.

        Args:
            materia (Materia):
        """

        self.data[TipoData.MATERIAS].append(materia)

    def eliminar_materia(self, materia: Materia) -> None:
        """Esta funcion recibe una materia y la elimina de la
        lista de materias.

        Args:
            materia (Materia):
        """

        self.data[TipoData.MATERIAS].remove(materia)

    def guardar(self) -> None:
        """Esta funcion guarda todos los datos en un .txt en formato
        de json.
        """

        ruta = os.path.join(BASE_DIR, "guardado.txt")

        with open(ruta, "w") as file:
            json.dump({
                "materias" : [m.to_dict() for m in self.data[TipoData.MATERIAS]]
            }, file, indent=4)

    def cargar(self) -> None:
        """Esta funcion carga los datos guardados y crea
        todos los objetos
        """

        ruta = os.path.join(BASE_DIR, "guardado.txt")

        with open(ruta, "r") as f:
            contenido = json.load(f)
            self.data[TipoData.MATERIAS] = [Materia.from_dict(m) for m in contenido["materias"]]

