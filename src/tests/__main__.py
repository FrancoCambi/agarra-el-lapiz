from models import Materia, Parcial
from datetime import date

def test_agregar_materia():

    materia = Materia("Testname")

    parcial1 = Parcial(date(2025, 4, 15))
    materia.agregar_parcial(parcial1)

    assert materia.parciales[0] == parcial1

    parcial2 = Parcial(date(2025, 4, 12))
    parcial3 = Parcial(date(2025, 4, 17))

    materia.agregar_parcial(parcial2)
    materia.agregar_parcial(parcial3)

    assert materia.parciales[0] == parcial2
    assert materia.parciales[1] == parcial1
    assert materia.parciales[2] == parcial3

    print("test_agregar_materia passed!")

test_agregar_materia()