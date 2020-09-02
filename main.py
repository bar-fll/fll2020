#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


#program
l_motor = Motor(Port.B)
r_motor = Motor(Port.C)
ml_motor = Motor(Port.D)
mr_motor = Motor(Port.A)
r_color = ColorSensor(Port.S3)
l_color = ColorSensor(Port.S2)
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
c = range(15)
for i in c: 
    #ev3.screen.print(r_color.reflection())
    first_val = r_color.reflection() - 25
    if first_val > 0:
        l_motor.run_angle(200,0.5*first_val)
        #mult = -0.5
    else:
        r_motor.run_angle(-200,0.8*first_val)
        #mult = -0.8
    #second_val = first_val * mult
    #r_motor.run_angle(400, second_val)

    if abs(first_val)<14:
        r_motor.run_time(150,160, wait = False)
        l_motor.run_time(150,160, wait = 0.001)

l_motor.run_angle(200,90)
r_motor.run_time(75,1400, wait = False)
l_motor.run_time(75,1400)

c = range(150)
for i in c: 
    #ev3.screen.print(r_color.reflection())
    first_val = r_color.reflection() - 25
    if first_val > 0:
        l_motor.run_angle(400,0.5*first_val)
        #mult = -0.5
    else:
        r_motor.run_angle(-400,0.8*first_val)
        #mult = -0.8
    #second_val = first_val * mult
    #r_motor.run_angle(400, second_val)

    if abs(first_val)<14:
        r_motor.run_time(150,160, wait = False)
        l_motor.run_time(150,160, wait = 0.001)


l_motor.run_angle(100,-410)
r_motor.run_time(400,900, wait = False)
l_motor.run_time(400,900)
mr_motor.run_time(-300,300)










