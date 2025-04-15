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
    
    def __str__(self):
        """Este metodo sobreescribe a la funcion print() cuando se aplica sobre
        un objeto de tipo materia
        """

        return (f"{self.nombre}:\n"
                f"{len(self.evaluables_pendientes[TipoEvaluable.PARCIAL])} parciales pendientes\n"
                f"{len(self.evaluables_pendientes[TipoEvaluable.TP])} tps pendientes\n"
                f"{len(self.archivo[TipoEvaluable.PARCIAL])} parciales archivados\n"
                f"{len(self.archivo[TipoEvaluable.TP])} tps archivados\n")
    
    def to_dict(self):
        """Este metodo transforma el objeto a un diccionario para ser guardado.

        Returns:
            _type_:
        """

        return {"nombre": self.nombre, 
                "evaluables_pendientes": {
                    tipo.value: [e.to_dict() for e in lista] for tipo, lista in self.evaluables_pendientes.items()
                },
                "archivo": {
                    tipo.value: [e.to_dict() for e in lista] for tipo, lista in self.archivo.items()
                }}
    
    @classmethod
    def from_dict(cls, data):
        """Este metodo toma la data guardada y crea una nueva instancia
        del objeto guardado

        Args:
            data (_type_):

        Returns:
            _type_: _description_
        """
        materia = cls(data["nombre"])
        materia.evaluables_pendientes = {
            TipoEvaluable(k): [Evaluable.from_dict(e) for e in v] for k, v in data["evaluables_pendientes"].items()
        }
        materia.archivo = {
            TipoEvaluable(k): [Evaluable.from_dict(e) for e in v] for k, v in data["archivo"].items()
        }
        return materia
    

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

    def eliminar_evaluable(self, evaluable: Evaluable) -> bool:
        """Este metodo recibe un evaluable y lo elimina de 
        su lista correspondiente.

        Args:
            evaluable (Evaluable): Evaluable a eliminar

        Returns:
            bool: True si fue eliminado, False si no.
            (Si da false, quiere decir que no estaba en la lista)
        """

        # Trato de eliminarlo de la lista
        try:
            self.evaluables_pendientes[evaluable.tipo].remove(evaluable)
        # Si no existe, remove da ValueError, asi que lo cazo
        # y devuelvo False    
        except ValueError:
            return False
    
        # Si no hubo erro, fue eliminado con exito. Ergo, devuelvo True
        return True

    def obtener_evaluable(self, tipo: TipoEvaluable, num: int) -> Evaluable:
        """Esta función recibe un tipo de evaluable y un número, para luego
        devolver el evaluable correspondiente.

        Args:
            tipo (TipoEvaluable): TipoEvaluable.PARCIAL o TipoEvaluable.TP
            num (int): El número de parcial o tp, empezando desde el 1.

        Returns:
            Evaluable: El objecto evaluable correspondiente.
        """

        # Devuelvo el (i-1)-esimo evaluable.
        return self.evaluables_pendientes[tipo][num - 1]

    def archivar_evaluable(self, evaluable: Evaluable) -> None:
        """Esta función recibe un evaluable. Luego, lo remueve de su lista
        correspondiente y lo agrega al diccionario archivo, en su lista
        correspondiente.

        Args:
            evaluable (Evaluable):
        """
    
        # Remuevo el evaluable de la lista correspondiente del diccionario
        # evaluables pendientes.
        self.evaluables_pendientes[evaluable.tipo].remove(evaluable)

        # Agrego el evaluable al archivo de evaluables pasados.
        self.archivo[evaluable.tipo].append(evaluable)

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
            print(f"Parcial {i + 1}:", lista_parciales[i])

        print("------------------------------------------------------------------")

        # Muestro un título
        print(f"Tps:\n")

        lista_tps = self.evaluables_pendientes[TipoEvaluable.TP] if not archivo else self.archivo[TipoEvaluable.TP]
        # Muestro cada tp con su fecha y nota si corresponde.
        for i in range(len(lista_tps)):
            print(f"Tp {i + 1}:", lista_tps[i])

