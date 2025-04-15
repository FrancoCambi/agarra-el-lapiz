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

        # Agrego la materia a la lista de materias dentro del
        # diccionario de datos
        self.data[TipoData.MATERIAS].append(materia)

    def eliminar_materia(self, materia: Materia) -> bool:
        """Esta funcion recibe una materia y la elimina de la
        lista de materias.

        Args:
            materia (Materia):

        Returns:
            bool: True si se pudo eliminar, False si no.
        """

        #Trato de eliminar la materia de la lista.
        try:
            self.data[TipoData.MATERIAS].remove(materia)
        # Si remove da error, es que no existe dentro de la lista.    
        except ValueError:
            return False

        # Si no da error, se pudo eliminar.
        return True


    def mostrar_materias(self) -> None:
        """Esta funcion muestra todas las materias guardadas.
        """

        print(f"Materias guardadas:")
        # Muestro cada nombre de las materias guardadas.
        # NOTA: Se crea una lista totalmente innecesaria para 
        # poder usar el for en una sola linea.
        # Como son seguro son pocos datos, el uso innecesario de memoria da igual.
        [print(m.nombre) for m in self.data[TipoData.MATERIAS]]

    def guardar(self) -> None:
        """Esta funcion guarda todos los datos en un .txt en formato
        de json.
        """

        # Agarro la ruta absoluta del directorio data y le agrego guardado.txt
        ruta = os.path.join(BASE_DIR, "guardado.txt")

        # Abro el archivo y le dumpeo cada materia en formato json.
        with open(ruta, "w") as file:
            json.dump({
                "materias" : [m.to_dict() for m in self.data[TipoData.MATERIAS]]
            }, file, indent=4)

    def cargar(self) -> None:
        """Esta funcion carga los datos guardados y crea
        todos los objetos
        """

        # Agarro la ruta absoluta del directorio data y le agrego guardado.txt
        ruta = os.path.join(BASE_DIR, "guardado.txt")

        # Abro el archivo y agarro todos los datos en formato json
        # y se transforma al diccionario normal.
        with open(ruta, "r") as f:
            contenido = json.load(f)
            self.data[TipoData.MATERIAS] = [Materia.from_dict(m) for m in contenido["materias"]]

