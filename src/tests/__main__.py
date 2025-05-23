from datetime import date, timedelta
import unittest

from models import Materia, Evaluable, TipoEvaluable, TipoData
from data import Data

class MyTestCase(unittest.TestCase):

    def test_agregar_evaluable(self):

        materia = Materia("Testname")

        parcial1 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 5, 15))
        materia.agregar_evaluable(parcial1)

        self.assertEqual(materia.evaluables_pendientes[TipoEvaluable.PARCIAL][0], parcial1)

        parcial2 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 5, 12))
        parcial3 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 5, 17))

        materia.agregar_evaluable(parcial2)
        materia.agregar_evaluable(parcial3)

        self.assertEqual(materia.evaluables_pendientes[TipoEvaluable.PARCIAL][0], parcial2)
        self.assertEqual(materia.evaluables_pendientes[TipoEvaluable.PARCIAL][1], parcial1)
        self.assertEqual(materia.evaluables_pendientes[TipoEvaluable.PARCIAL][2], parcial3)

        # TESTS TPs

        tp1 = Evaluable(TipoEvaluable.TP, date(2025, 5, 10))
        materia.agregar_evaluable(tp1)

        self.assertEqual(materia.evaluables_pendientes[TipoEvaluable.TP][0], tp1)

        tp2 = Evaluable(TipoEvaluable.TP, date(2025, 5, 5))
        tp3 = Evaluable(TipoEvaluable.TP, date(2025, 5, 20))

        materia.agregar_evaluable(tp2)
        materia.agregar_evaluable(tp3)

        self.assertEqual(materia.evaluables_pendientes[TipoEvaluable.TP][0], tp2)
        self.assertEqual(materia.evaluables_pendientes[TipoEvaluable.TP][1], tp1)
        self.assertEqual(materia.evaluables_pendientes[TipoEvaluable.TP][2], tp3)


    def test_obtener_evaluable(self):

        materia = Materia("test")

        parcial1 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 5, 15))
        parcial2 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 5, 15))

        materia.agregar_evaluable(parcial1)
        materia.agregar_evaluable(parcial2)

        self.assertEqual(materia.obtener_evaluable(TipoEvaluable.PARCIAL, 1), parcial1)
        self.assertEqual(materia.obtener_evaluable(TipoEvaluable.PARCIAL, 2), parcial2)

        # TESTS TPs

        tp1 = Evaluable(TipoEvaluable.TP, date(2025, 5, 15))
        tp2 = Evaluable(TipoEvaluable.TP, date(2025, 5, 15))

        materia.agregar_evaluable(tp1)
        materia.agregar_evaluable(tp2)

        self.assertEqual(materia.obtener_evaluable(TipoEvaluable.TP, 1), tp1)
        self.assertEqual(materia.obtener_evaluable(TipoEvaluable.TP, 2), tp2)


    def test_cargar_nota(self):

        parcial1 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 4, 15))

        parcial1.cargar_nota(8)

        self.assertEqual(parcial1.nota, 8)

        tp1 = Evaluable(TipoEvaluable.TP, date(2025, 6, 7))

        tp1.cargar_nota(7)

        self.assertEqual(tp1.nota, 7)

        self.assertRaises(ValueError, parcial1.cargar_nota, -5)   
        self.assertRaises(ValueError, tp1.cargar_nota, -5)   


    def test_cambiar_fecha(self):

        parcial1 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 4, 16))

        parcial1.cambiar_fecha(date(2025, 4, 18))

        self.assertEqual(parcial1.fecha, date(2025, 4, 18))

        self.assertRaises(ValueError, parcial1.cambiar_fecha, date.today() - timedelta(days=1))


    def test_archivar_evaluable(self):

        materia = Materia("test")

        parcial1 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 7, 15))
        parcial2 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 7, 15))

        materia.agregar_evaluable(parcial1)
        materia.agregar_evaluable(parcial2)

        materia.archivar_evaluable(parcial1)
        materia.archivar_evaluable(parcial2)

        self.assertFalse(len(materia.evaluables_pendientes[TipoEvaluable.PARCIAL]))
        self.assertEqual(len(materia.archivo[TipoEvaluable.PARCIAL]), 2)

        tp1 = Evaluable(TipoEvaluable.TP, date(2025, 7, 15))
        tp2 = Evaluable(TipoEvaluable.TP, date(2025, 7, 15))

        materia.agregar_evaluable(tp1)
        materia.agregar_evaluable(tp2)

        materia.archivar_evaluable(tp1)
        materia.archivar_evaluable(tp2)

        self.assertFalse(len(materia.evaluables_pendientes[TipoEvaluable.TP]))
        self.assertEqual(len(materia.archivo[TipoEvaluable.TP]), 2)

    def test_agregar_materia(self):

        m = Materia("testname")

        data = Data()

        data.agregar_materia(m)

        self.assertEqual(len(data.data[TipoData.MATERIAS]), 1)
        self.assertEqual(data.data[TipoData.MATERIAS][0], m)

    def test_eliminar_materia(self):

        m = Materia("test")

        data = Data()

        data.agregar_materia(m)

        data.eliminar_materia(m)

        self.assertFalse(len(data.data[TipoData.MATERIAS]))

    def test_eliminar_evaluable(self):

        materia = Materia("Testname")

        parcial1 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 5, 15))
        parcial2 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 5, 12))
        parcial3 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 5, 17))

        materia.agregar_evaluable(parcial1)
        materia.agregar_evaluable(parcial2)
        materia.agregar_evaluable(parcial3)

        materia.eliminar_evaluable(parcial1)
        self.assertNotIn(parcial1, materia.evaluables_pendientes[TipoEvaluable.PARCIAL])

        materia.eliminar_evaluable(parcial2)
        self.assertNotIn(parcial2, materia.evaluables_pendientes[TipoEvaluable.PARCIAL])

        materia.eliminar_evaluable(parcial3)
        self.assertNotIn(parcial3, materia.evaluables_pendientes[TipoEvaluable.PARCIAL])

        # TESTS TPs

        tp1 = Evaluable(TipoEvaluable.TP, date(2025, 5, 10))
        tp2 = Evaluable(TipoEvaluable.TP, date(2025, 5, 5))
        tp3 = Evaluable(TipoEvaluable.TP, date(2025, 5, 20))

        materia.agregar_evaluable(tp1)
        materia.agregar_evaluable(tp2)
        materia.agregar_evaluable(tp3)

        materia.eliminar_evaluable(tp1)
        self.assertNotIn(tp1, materia.evaluables_pendientes[TipoEvaluable.TP])

        materia.eliminar_evaluable(tp2)
        self.assertNotIn(tp2, materia.evaluables_pendientes[TipoEvaluable.TP])

        materia.eliminar_evaluable(tp3)
        self.assertNotIn(tp3, materia.evaluables_pendientes[TipoEvaluable.TP])

    def test_promedio(self):

        materia = Materia("test")

        parcial1 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 7, 15))

        parcial1.cargar_nota(8)

        tp1 = Evaluable(TipoEvaluable.TP, date(2025, 6, 7))

        tp1.cargar_nota(7)

        materia.agregar_evaluable(parcial1)
        materia.agregar_evaluable(tp1)
        materia.archivar_evaluable(parcial1)
        materia.archivar_evaluable(tp1)

        self.assertEqual(materia.promedio(), 8)
        self.assertEqual(materia.promedio(tps=True), 7)
        self.assertEqual(materia.promedio(general=True), 7.5)
        self.assertRaises(Exception, materia.promedio, True, True)


    

unittest.main(exit=False)