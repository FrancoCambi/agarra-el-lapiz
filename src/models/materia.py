from .evaluable import Evaluable
from .enums import TipoEvaluable


class Materia:
    """Clase que simula una materia de la facultad, conteniendo su 
        nombre, parciales y tp's.
    """

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.evaluables_pendientes: dict[TipoEvaluable, list[Evaluable]] = {TipoEvaluable.PARCIAL: [], 
                                                                            TipoEvaluable.TP: []}
        self.archivo: dict[TipoEvaluable, list[Evaluable]] = {TipoEvaluable.PARCIAL: [], 
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

    def obtener_evaluable(self, tipo: TipoEvaluable, num: int) -> Evaluable:
        """Esta función recibe un tipo de evaluable y un número, para luego
        devolver el evaluable correspondiente.

        Args:
            tipo (TipoEvaluable): TipoEvaluable.PARCIAL o TipoEvaluable.TP
            num (int): El número de parcial o tp, empezando desde el 1.

        Returns:
            Evaluable: El objecto evaluable correspondiente.
        """

        return self.evaluables_pendientes[tipo][num - 1]

    def cargar_nota(self, evaluable: Evaluable, nota: int) -> None:
        """Esta función recibe un evaluable y una nota. Luego, lo remueve de su lista
        correspondiente y carga la nota.

        Args:
            evaluable (Evaluable):
            nota (int): 
        """
    
        # Remuevo el evaluable de la lista correspondiente del diccionario
        # evaluables pendientes.
        self.evaluables_pendientes[evaluable.tipo].remove(evaluable)

        # Agrego el evaluable al archivo de evaluables pasados.
        self.archivo[evaluable.tipo].append(evaluable)

        # Cargo la nota.
        evaluable.nota = nota


    def mostrar_evaluables(self, archivo: bool = False) -> None:
        """Muestra de manera ordenada los evaluables pendientes o ya rendidos de una materia.

        Args:
            archivo (bool, optional): Si es falso, se muestran los pendientes.
            Si es verdadero, los ya rendidos. Es falso por defecto.
        """

        # Muestro un título
        print(f"Parciales:\n")

        lista_parciales = self.evaluables_pendientes[TipoEvaluable.PARCIAL] if not archivo else self.archivo[TipoEvaluable.PARCIAL]
        # Muestro cada parcial con su fecha y nota si corresponde.
        for i in range(len(lista_parciales)):
            print(f"Parcial {i + 1}: {lista_parciales[i].fecha}, nota: {lista_parciales[i].nota if lista_parciales[i].nota != -1 else "No hay nota cargada."}")

        print("------------------------------------------------------------------")

        # Muestro un título
        print(f"Tps:\n")

        lista_tps = self.evaluables_pendientes[TipoEvaluable.TP] if not archivo else self.archivo[TipoEvaluable.TP]
        # Muestro cada tp con su fecha y nota si corresponde.
        for i in range(len(lista_tps)):
            print(f"Tp {i + 1}: {lista_tps[i].fecha}, nota: {lista_tps[i].nota if lista_tps[i].nota != -1 else "No hay nota cargada."}")

