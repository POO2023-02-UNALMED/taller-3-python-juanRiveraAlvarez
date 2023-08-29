from televisores.tv import TV
from televisores.marca import Marca
from televisores.control import Control
from testmetodos import *

if __name__ == "__main__":


    marca = Marca("Mitorola")

    tv1 = TV(marca, True)
    tv1.setVolumen(5)
    tv1.volumenDown()
    tv1.volumenUp()
    tv1.volumenDown()
    tv1.volumenDown()
    tv1.turnOff()
    tv1.volumenUp()

    tv2 = TV(marca, False)
    tv2.setVolumen(3)
    tv2.volumenUp()
    tv2.volumenDown()
    tv2.turnOn()
    tv2.volumenUp()
    tv2.volumenUp()
    tv2.volumenDown()
    tv2.volumenUp()

    tv3 = TV(marca, True)
    tv3.setVolumen(9)
    tv3.volumenUp()

    tv4 = TV(marca, True)
    tv4.setVolumen(-2)
    tv4.volumenDown()

    tv5 = TV(marca, True)
    tv5.setVolumen(0)
    tv5.volumenDown()

    tv6 = TV(marca, True)
    tv6.setVolumen(7)
    tv6.volumenUp()

    tv7 = TV(marca, True)
    tv7.setVolumen(4)
    tv7.volumenDown()
    tv7.setVolumen(15)

    ok = False
    if tv1.getVolumen() == 3 and \
            tv2.getVolumen() == 3 and \
            tv3.getVolumen() == 2 and \
            tv4.getVolumen() == 0 and \
            tv5.getVolumen() == 0 and \
            tv6.getVolumen() == 7 and \
            tv7.getVolumen() == 3:
        ok = True

    print(ok)
    print(tv4.getVolumen())

    marca1 = Marca("Semsung")
    marca2 = Marca("Lj")

    tv1 = TV(marca1, True)
    tv2 = TV(marca2, False)

    tv1.setPrecio(2000)
    tv2.setCanal(90)
    tv1.setCanal(121)
    tv2.setVolumen(7)

    control1 = Control()
    control1.enlazar(tv1)
    control1.turnOff()
    control1.setCanal(50)
    control1.turnOn()
    control1.canalUp()
    control1.volumenUp()

    print(tv2.getCanal())
    print(tv1.getPrecio())
    print(tv1.getMarca().getNombre())
    print(tv1.getCanal())
