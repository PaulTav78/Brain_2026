
from A_init_heavy import *

speed(300)

# Distance parcourue au départ
start_distance = drive_base.distance()

# On avance
while abs(drive_base.distance() - start_distance) < 500:

    # Lire l'état du robot
    state = drive_base.state()

    # state = (distance, angle, vitesse, vitesse de rotation)
    current_speed = state[2]

    print("Vitesse :", current_speed, "mm/s")

    # Avancer à 300 mm/s
    drive_base.drive(300, 0)

    wait(50)

# Arrêt
drive_base.stop()

print("Terminé")