from C_menu_libs import show_menu, store_number
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Side, Color, Button, Stop
from pybricks.pupdevices import ColorSensor
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait


module_motor_left = Motor(Port.B)
module_motor_right = Motor(Port.F)

NB_ITEMS = 4
selected = show_menu(nb_items=NB_ITEMS)

# Based on the selection, run a program.
if selected == "1":
    module_motor_left.run_angle(500, 1000)
if selected == "2":
    module_motor_right.run_angle(500, 1000)
if selected == "3":
    module_motor_right.run_angle(500, -1000)
if selected == "4":
    module_motor_left.run_angle(500, -1000)
store_number(int(selected) % NB_ITEMS) # code du menu, ne pas enlever