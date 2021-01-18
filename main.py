#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
l_motor = Motor(Port.B)
r_motor = Motor(Port.C)
ml_motor = Motor(Port.D)
mr_motor = Motor(Port.A)
r_color = ColorSensor(Port.S3)
l_color = ColorSensor(Port.S2)
gyro = GyroSensor(Port.S4)

while True:
    if ev3.buttons.pressed():

        r_motor.run_time(200,2500, wait = False)
        l_motor.run_time(200,2500)

        c = range(41)
        for i in c: 
            first_val = r_color.reflection() - 25
            if first_val > 0:
                l_motor.run_time(200,4*(first_val+20), wait = False)
                r_motor.run_time(200,1*(first_val+20))
            elif first_val < 0:
                r_motor.run_time(200,5*abs(first_val-50), wait = False)
                l_motor.run_time(200,2*abs(first_val-50))
            else:
                r_motor.run_time(200,120, wait = False)
                l_motor.run_time(200,120)

        gyro.reset_angle(0)
        while True:
            if gyro.angle() >= 67:
                break
            else:
                ev3.screen.print(gyro.angle())
                r_motor.run_time(100,100,wait = False)

        c = range(39)
        for i in c: 
            first_val = r_color.reflection() - 25
            if first_val > 0:
                l_motor.run_time(200,4*(first_val+20), wait = False)
                r_motor.run_time(200,1*(first_val+20))
            elif first_val < 0:
                r_motor.run_time(200,5*abs(first_val-50), wait = False)
                l_motor.run_time(200,2*abs(first_val-50))
            else:
                r_motor.run_time(200,120, wait = False)
                l_motor.run_time(200,120)

        c = range(70)
        for i in c: 
            first_val = r_color.reflection() - 25
            if first_val > 0:
                l_motor.run_time(100,3*(first_val+20), wait = False)
                r_motor.run_time(100,1*(first_val+20))
            elif first_val < 0:
                r_motor.run_time(100,3*abs(first_val-40), wait = False)
                l_motor.run_time(100,1*abs(first_val-50))
            else:
                r_motor.run_time(200,120, wait = False)
                l_motor.run_time(200,120)       

        r_motor.run_time(100,2000)

        r_motor.run_time(100,100, wait = False)
        l_motor.run_time(100,100)

        gyro.reset_angle(0)
        while True:
            if gyro.angle() <= -1:
                break
            else:
                ev3.screen.print(gyro.angle())
                l_motor.run_time(100,100,wait = False)
                r_motor.run_time(0,0)

        ml_motor.run_time(600,7500)

        # r_motor.run_time(200,5*abs(first_val-50), wait = False)
        # l_motor.run_time(200,2*abs(first_val-50))
        # The code above also works but is a bit inaccurate

        r_motor.run_time(-200,200, wait = False)
        l_motor.run_time(-200,200)

        ml_motor.run_time(-400,5500)

        r_motor.run_time(-200,700, wait = False)
        l_motor.run_time(-200,700)

        gyro.reset_angle(0)
        while True:
            if gyro.angle() <= -3:
                break
            else:
                ev3.screen.print(gyro.angle())
                r_motor.run_time(-100,100,wait = False)

        r_motor.run_time(100,1740, wait = False)
        l_motor.run_time(100,1740)

        r_motor.run_time(-100,1000, wait = False)
        l_motor.run_time(-100,1000)

        
        gyro.reset_angle(0)
        while True:
            if gyro.angle() <= -21:
                break
            else:
                ev3.screen.print(gyro.angle())
                r_motor.run_time(-100,100,wait = False)
        

        r_motor.run_time(200,400, wait = False)
        l_motor.run_time(200,400)

        ml_motor.run_time(400,3800)
        
        r_motor.run_time(-200,2300, wait = False)
        l_motor.run_time(-200,2300)

        gyro.reset_angle(0)
        while True:
            if gyro.angle() <= -40:
                break
            else:
                ev3.screen.print(gyro.angle())
                l_motor.run_time(100,100,wait = False)
                r_motor.run_time(0,0)

        r_motor.run_time(200,3400, wait = False)
        l_motor.run_time(200,3400)

        mr_motor.run_time(-500,4700) 

        mr_motor.run_time(500,2800)

        gyro.reset_angle(0)
        while True:
            if gyro.angle() >= 7:
                break
            else:
                ev3.screen.print(gyro.angle())
                l_motor.run_time(-100,100,wait = False)
                r_motor.run_time(0,0)

        r_motor.run_time(-200,2200, wait = False)
        l_motor.run_time(-200,2200)
        
        r_motor.run_time(-200,400)
        l_motor.run_time(200,400)

        r_motor.run_time(-200,5000, wait = False)
        l_motor.run_time(-200,5000)

        gyro.reset_angle(0)
        while True:
            if gyro.angle() <= -52:
                break
            else:
                ev3.screen.print(gyro.angle())
                r_motor.run_time(-100,100,wait = False)
                l_motor.run_time(0,0)               

        r_motor.run_time(-400,3700, wait = False)
        l_motor.run_time(-400,3700)


    else:
        sleep(0.01)

