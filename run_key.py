from A_init_heavy import *
from pybricks.hubs import PrimeHub
from pybricks.tools import wait


speed(1000)
straight(500)
curve(380, 45, True)
module_motor_right.run_angle(500, 1000)
wait(1000)
straight(-225, True)
turn(-80)
straight(-600)
