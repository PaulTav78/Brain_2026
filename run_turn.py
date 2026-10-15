#------------------------IMPORTATION------------------------#
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Side, Color, Button, Stop
from pybricks.pupdevices import ColorSensor
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait

#------------------------INITIALISATION------------------------#
hub = PrimeHub()
hub.display.orientation(up=Side.RIGHT)
print("Battery : ", hub.battery.voltage(), 'mV')

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
module_motor_left = Motor(Port.B)
module_motor_right = Motor(Port.F)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=63, axle_track=140)
drive_base.use_gyro(True)






def turn(angle, speed=2):
    hub.imu.reset_heading(0)
        
    if speed == 1:
        drive_base.settings(turn_acceleration=200, turn_rate=200)
        drive_base.turn(angle)
        
        # Boucle de correction de l'erreur résiduelle
        while True:
            yaw_angle = hub.imu.heading()
            delta = yaw_angle - angle
            
            print(f"Cap réel: {yaw_angle} | Erreur (delta): {delta}")
            
            # Si l'écart est inférieur ou égal à 1 degré, on sort de la boucle
            if abs(delta) <= 1:
                break
                
            # On corrige l'écart restant
            drive_base.turn(-delta)
    if speed == 2:
        drive_base.settings(turn_acceleration=600, turn_rate=400)
        drive_base.turn(angle-3)
        
        # Boucle de correction de l'erreur résiduelle
        while True:
            yaw_angle = hub.imu.heading()
            delta = yaw_angle - angle
            
            print(f"Cap réel: {yaw_angle} | Erreur (delta): {delta}")
            
            # Si l'écart est inférieur ou égal à 1 degré, on sort de la boucle
            if abs(delta) <= 1:
                break
                
            # On corrige l'écart restant
            drive_base.turn(-delta)
    if speed == 3:
        drive_base.settings(turn_acceleration=900, turn_rate=900)
        drive_base.turn(angle-5)
        
        # Boucle de correction de l'erreur résiduelle
        while True:
            yaw_angle = hub.imu.heading()
            delta = yaw_angle - angle
            
            print(f"Cap réel: {yaw_angle} | Erreur (delta): {delta}")
            
            # Si l'écart est inférieur ou égal à 1 degré, on sort de la boucle
            if abs(delta) <= 1:
                break
                
            # On corrige l'écart restant
            drive_base.turn(-delta)

turn(360, 2)

yaw_angle = hub.imu.heading()
print(yaw_angle)

