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

#------------------------FONCTIONS------------------------#

def straight(distance, shouldStop=False):
    """Avancer tout droit d'une distance, sans modifier l'accélération en douce"""
    # On choisit juste le mode d'arrêt selon shouldStop
    stop_behavior = Stop.COAST_SMART if shouldStop else Stop.NONE
    
    drive_base.straight(distance, then=stop_behavior)

def turn(angle):
    drive_base.turn(angle)

def straight_motor_left(distance, motor_speed, motor_angle, shouldStop=False):
    drive_base.settings(straight_acceleration=1000)
    module_motor_left.run_angle(motor_speed, motor_angle, then=Stop.HOLD, wait=False)
    initial = drive_base.distance()
    
    # Détermine la vitesse du robot selon le sens (positif = avance, négatif = recule)
    robot_speed = -200 if distance < 0 else 200
    
    while not module_motor_left.done() or abs(drive_base.distance() - initial) < abs(distance):
        
        if abs(drive_base.distance() - initial) < abs(distance):
            drive_base.drive(robot_speed, 0)
        else:
            drive_base.drive(0, 0)  

        wait(10)
    drive_base.stop()


def straight_motor_right(distance, motor_speed, motor_angle, shouldStop=False):
    drive_base.settings(straight_acceleration=700)
    module_motor_right.run_angle(motor_speed, motor_angle, then=Stop.HOLD, wait=False)
    initial = drive_base.distance()
    
    # Détermine la vitesse du robot selon le sens
    robot_speed = -500 if distance < 0 else 500
    
    while not module_motor_right.done() or abs(drive_base.distance() - initial) < abs(distance):

        if abs(drive_base.distance() - initial) < abs(distance):
            drive_base.drive(robot_speed, 0)
        else:
            drive_base.drive(0, 0)  

        wait(10)
    drive_base.stop()


def all_motor(distance,
              left_speed, left_angle,
              right_speed, right_angle,
              shouldStop=False):

    drive_base.settings(straight_acceleration=700)

    module_motor_left.run_angle(left_speed, left_angle, then=Stop.HOLD, wait=False)
    module_motor_right.run_angle(right_speed, right_angle, then=Stop.HOLD, wait=False)

    initial = drive_base.distance()
    
    # Détermine la vitesse du robot selon le sens
    robot_speed = -200 if distance < 0 else 200

    while True:

        if abs(drive_base.distance() - initial) < abs(distance):
            drive_base.drive(robot_speed, 0)
        else:
            drive_base.drive(0, 0) 

        # Condition d’arrêt :
        # Les DEUX moteurs doivent avoir terminé ET la distance doit être atteinte
        if module_motor_left.done() and module_motor_right.done() and abs(drive_base.distance() - initial) >= abs(distance):
            break

        wait(10)

    drive_base.stop()


def curve(radius, angle, shouldStop=False):
    """Faire une courbe avec en 1ère argument le rayon puis l'angle"""
    if shouldStop == True:
        drive_base.settings(straight_acceleration=(700))
        drive_base.curve(radius, angle, then=Stop.COAST_SMART)
    else:
        drive_base.settings(straight_acceleration=(1000))
        drive_base.curve(radius, angle, then=Stop.NONE)

def set_precision_mode():
    """Mode ultra-précis pour les approches finales et alignements"""
    drive_base.settings(
        straight_speed=150,
        straight_acceleration=500,
        turn_rate=45,
        turn_acceleration=150
    )

def set_classic_mode():
    """Mode polyvalent pour 80% des déplacements du match"""
    drive_base.settings(
        straight_speed=400,
        straight_acceleration=1200,
        turn_rate=120,
        turn_acceleration=400
    )

def set_fast_mode():
    """Mode rapide pour traverser la table sans patiner"""
    drive_base.settings(
        straight_speed=650,  # Limite physique réelle des moteurs sans engrenage
        straight_acceleration=1800,
        turn_rate=200,
        turn_acceleration=600
    )


def wall_homing(speed=-200, load_threshold=150, timeout_ms=3000):
    """
    Fait bouger le robot jusqu'à ce qu'il bute contre un mur 
    (détecté par la charge des moteurs).
    """
    drive_base.drive(speed, 0)
    
    from pybricks.tools import StopWatch
    watch = StopWatch()
    
    while watch.time() < timeout_ms:
        # Si l'un des moteurs principaux force (bloqué par le mur)
        if abs(left_motor.load()) > load_threshold or abs(right_motor.load()) > load_threshold:
            break
        wait(10)
        
    drive_base.stop()
    # On remet à zéro la distance parcourue et le gyroscope pour repartir sur de bonnes bases
    drive_base.reset()
    hub.imu.reset_heading(0)


def speed(speed):
    drive_base.settings(straight_speed=speed)

