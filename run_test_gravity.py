from A_init_heavy import *
'''
#drive_base.settings(turn_acceleration=1500, turn_rate=1000)
drive_base.use_gyro(True)
hub.imu.reset_heading(0)
yaw = hub.imu.heading()
print(yaw)
drive_base.turn(360)
yaw2 = hub.imu.heading()
print(yaw2)'''

print("Test d'avancement")
drive_base.settings(straight_speed=200, straight_acceleration=200)

drive_base.straight(500)
print(f"Arrivé, Angles moteurs - Gauche: {left_motor.angle()}°, Droite: {right_motor.angle()}°")

wait(1000)

drive_base.straight(-500)

print("Test de rotation")
drive_base.settings(turn_rate=100, turn_acceleration=100)

drive_base.turn(360)
print(f"Cap (Heading) IMU après 360° : {hub.imu.heading()}°")
