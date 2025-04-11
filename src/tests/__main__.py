from datetime import date
from models import Materia, Evaluable, TipoEvaluable

def test_agregar_evaluable():

    materia = Materia("Testname")

    parcial1 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 4, 15))
    materia.agregar_evaluable(parcial1)

    assert materia.evaluables_pendientes[TipoEvaluable.PARCIAL][0] == parcial1

    parcial2 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 4, 12))
    parcial3 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 4, 17))

    materia.agregar_evaluable(parcial2)
    materia.agregar_evaluable(parcial3)

    assert materia.evaluables_pendientes[TipoEvaluable.PARCIAL][0] == parcial2
    assert materia.evaluables_pendientes[TipoEvaluable.PARCIAL][1] == parcial1
    assert materia.evaluables_pendientes[TipoEvaluable.PARCIAL][2] == parcial3

    # TESTS TPs

    tp1 = Evaluable(TipoEvaluable.TP, date(2025, 5, 10))
    materia.agregar_evaluable(tp1)

    assert materia.evaluables_pendientes[TipoEvaluable.TP][0] == tp1

    tp2 = Evaluable(TipoEvaluable.TP, date(2025, 5, 5))
    tp3 = Evaluable(TipoEvaluable.TP, date(2025, 5, 20))

    materia.agregar_evaluable(tp2)
    materia.agregar_evaluable(tp3)

    assert materia.evaluables_pendientes[TipoEvaluable.TP][0] == tp2
    assert materia.evaluables_pendientes[TipoEvaluable.TP][1] == tp1
    assert materia.evaluables_pendientes[TipoEvaluable.TP][2] == tp3

    print("test_agregar_evaluable passed!")

def test_obtener_evaluable():

    materia = Materia("test")

    parcial1 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 4, 15))
    parcial2 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 5, 15))

    materia.agregar_evaluable(parcial1)
    materia.agregar_evaluable(parcial2)

    assert materia.obtener_evaluable(TipoEvaluable.PARCIAL, 1) == parcial1
    assert materia.obtener_evaluable(TipoEvaluable.PARCIAL, 2) == parcial2

    # TESTS TPs

    tp1 = Evaluable(TipoEvaluable.TP, date(2025, 4, 15))
    tp2 = Evaluable(TipoEvaluable.TP, date(2025, 5, 15))

    materia.agregar_evaluable(tp1)
    materia.agregar_evaluable(tp2)

    assert materia.obtener_evaluable(TipoEvaluable.TP, 1) == tp1 
    assert materia.obtener_evaluable(TipoEvaluable.TP, 2) == tp2

    print("test_obtener_evaluable_passed!")

def test_cargar_nota():

    materia = Materia("test")

    parcial1 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 4, 15))
    parcial2 = Evaluable(TipoEvaluable.PARCIAL, date(2025, 5, 15))

    materia.agregar_evaluable(parcial1)
    materia.agregar_evaluable(parcial2)

    materia.cargar_nota(parcial1, 8)
    materia.cargar_nota(parcial2, 6)

    assert not len(materia.evaluables_pendientes[TipoEvaluable.PARCIAL])
    assert parcial1.nota == 8
    assert parcial2.nota == 6
    assert len(materia.archivo[TipoEvaluable.PARCIAL]) == 2

    tp1 = Evaluable(TipoEvaluable.TP, date(2025, 4, 15))
    tp2 = Evaluable(TipoEvaluable.TP, date(2025, 5, 15))

    materia.agregar_evaluable(tp1)
    materia.agregar_evaluable(tp2)

    materia.cargar_nota(tp1, 8)
    materia.cargar_nota(tp2, 6)

    assert not len(materia.evaluables_pendientes[TipoEvaluable.TP])
    assert tp1.nota == 8
    assert tp2.nota == 6
    assert len(materia.archivo[TipoEvaluable.TP]) == 2

    print("test_cargar_nota passed!")

test_agregar_evaluable()
test_obtener_evaluable()
test_cargar_nota()