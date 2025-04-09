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

    # TESTS TP

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



test_agregar_evaluable()