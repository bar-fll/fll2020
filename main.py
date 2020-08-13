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

l_motor = Motor(Port.B)
r_motor = Motor(Port.C)
r_color = ColorSensor(Port.S4)
l_color = ColorSensor(Port.S1)
r_touch = TouchSensor(Port.S3)
l_touch = TouchSensor(Port.S2)

while True:
    if r_touch.pressed() or l_touch.pressed():
        if r_touch.pressed():
            while True:
                if l_touch.pressed():
                    l_motor.run_time(0,0)
                    r_motor.run_time(0,0)
                    break
                else:
                    l_motor.run_time(300,300)
        else:
            while True:
                if r_touch.pressed():
                    l_motor.run_time(0,0)
                    r_motor.run_time(0,0)
                    break
                else:
                    r_motor.run_time(300,300)
    else:
        l_motor.run_time(50,200, wait=False)
        r_motor.run_time(50,200)
        

        
