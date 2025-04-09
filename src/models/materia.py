from .evaluable import Evaluable
from .enums import TipoEvaluable


class Materia:
    """Clase que simula una materia de la facultad, conteniendo su nombre, parciales y tp's.
    """

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.evaluables_pendientes: dict[TipoEvaluable, list[Evaluable]] = {TipoEvaluable.PARCIAL: [], 
                                                                            TipoEvaluable.TP: []}

    def agregar_evaluable(self, evaluable: Evaluable) -> None:
        """Agrega un evaluable a la materia, de manera ordenada segun su fecha.

        Args:
            evaluable (Evaluable):
        """
        # Agrego el parcial a la lista
        self.evaluables_pendientes[evaluable.tipo].append(evaluable)

        # Si hay más de dos, ordeno la lista dependiendo su "len", que devuelve la cantidad de dias
        # que faltan para el parcial
        #Esto se hace para poder printear los parciales en orden cronológico fácilmente.
        if len(self.evaluables_pendientes[evaluable.tipo]) >= 2:
            self.evaluables_pendientes[evaluable.tipo].sort(key=len)

    def cargar_nota(self, evaluable: Evaluable, nota: int) -> None:
        """Esta función recibe un evaluable y una nota. Luego, lo remueve de su lista
        correspondiente y carga la nota.

        Args:
            evaluable (Evaluable):
            nota (int): 
        """
    
        # Si es un parcial, debo trabajar sobre la lista de parciales
        if evaluable.tipo == TipoEvaluable.PARCIAL:
            self.evaluables_pendientes[TipoEvaluable.PARCIAL].remove(evaluable)

        # Si no, es un tp, trabajo sobre la lista de tps
        else:
            self.evaluables_pendientes[TipoEvaluable.Tp].remove(evaluable)

        # Cargo la nota.
        evaluable.nota = nota


    def mostrar_evaluables(self) -> None:
        """Muesta de manera ordenada los evaluables de la materia.
        """

        # Muestro un título
        print(f"Parciales de {self.nombre}:\n")

        lista_parciales = self.evaluables_pendientes[TipoEvaluable.PARCIAL]
        # Muestro cada parcial con su fecha y nota si corresponde.
        for i in range(len(lista_parciales)):
            print(f"Parcial {i + 1}: {lista_parciales[i].fecha}, nota: {lista_parciales[i].nota if lista_parciales[i].nota != -1 else "No hay nota."}")

        print("------------------------------------------------------------------")

        # Muestro un título
        print(f"Tps de {self.nombre}:\n")

        lista_tps = self.evaluables_pendientes[TipoEvaluable.TP]
        # Muestro cada tp con su fecha y nota si corresponde.
        for i in range(len(lista_tps)):
            print(f"Tp {i + 1}: {lista_tps[i].fecha}, nota: {lista_tps[i].nota if lista_tps[i].nota != -1 else "No hay nota."}")
