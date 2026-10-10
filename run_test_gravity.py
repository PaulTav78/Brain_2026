from A_init_heavy import *

#drive_base.settings(turn_acceleration=1500, turn_rate=1000)
drive_base.use_gyro(True)
hub.imu.reset_heading(0)
yaw = hub.imu.heading()
print(yaw)
drive_base.turn(360)
yaw2 = hub.imu.heading()
print(yaw2)