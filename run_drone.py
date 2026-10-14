from A_init_heavy import *
from pybricks.parameters import Button
from pybricks.tools import wait

speed(400)
straight(450, True)
speed(1000)
straight(-300, True)


while Button.BLUETOOTH not in hub.buttons.pressed():
    wait(10)

speed(400)
straight(640, True)
turn(-65)
turn(60)
straight(-700)