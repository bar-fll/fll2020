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


#porgram
l_motor = Motor(Port.B)
r_motor = Motor(Port.C)
r_color = ColorSensor(Port.S3)
l_color = ColorSensor(Port.S2)

#l_color will find the black line
r_motor.reset_angle(0)
l_motor.reset_angle(0)
while True:
    if l_color.ambient()<=5 or r_color.ambient()<=5 :
        r_motor.run_time(0,0)
        l_motor.run_time(0,0)
        ev3.screen.print(r_color.ambient())
        ev3.screen.print(l_color.ambient())
        wait(50)
        ev3.screen.print()
        break
    else:
        l_motor.run_time(50,200,wait=False)
        r_motor.run_time(50,200,wait=False) 
        wait(20)
        ev3.screen.print(r_color.ambient())
        ev3.screen.print(l_color.ambient())
        wait(5)
        ev3.screen.print()
#r_color will find the black line
z = l_color.ambient()
q = r_color.ambient()
if z < q:
    r_motor.reset_angle(0)
    while True:
        if r_color.ambient()<=5:
            r_motor.run_time(0,0)
            l_motor.run_time(0,0)
            ev3.screen.print(r_color.ambient())
            wait(50)
            ev3.screen.print()
            break
        else:
            r_motor.run_time(50,200) 
            l_motor.run_time(0,0)
            ev3.screen.print(r_color.ambient())
            wait(50)
            ev3.screen.print()
else:
    r_motor.run_time(0,0)
    l_motor.run_time(0,0)
if z > q:
    l_motor.reset_angle(0)
    while True:
        if l_color.ambient()<=5:
            r_motor.run_time(0,0)
            l_motor.run_time(0,0)
            ev3.screen.print(l_color.ambient())
            wait(50)
            ev3.screen.print()
            break
        else:
            l_motor.run_time(50,200) 
            r_motor.run_time(0,0)
            ev3.screen.print(l_color.ambient())
            wait(50)
            ev3.screen.print()

#r_motor will find the white line in front of the black line

x=2
while x==2:    
#left_motor
    while True:
        if l_color.ambient()>5:

            r_motor.run_time(0,0)
            l_motor.run_time(0,0)
            ev3.screen.print(l_color.ambient())
            wait(50)
            ev3.screen.print()
            break
        else:
            l_motor.run_time(50,100) 
#l_motor will find the white line behind the black line
    l_motor.run_time(-50,800)
    l_motor.reset_angle(0)
    while True:
        if l_color.ambient()>5:

            r_motor.run_time(0,0)
            l_motor.run_time(0,0)
            ev3.screen.print(l_color.ambient())
            wait(500)
            ev3.screen.print()
            break
        else:

            l_motor.run_time(-50,100)
    ev3.screen.print(l_motor.angle())
    wait(50)
    n = l_motor.angle()
    l_motor.run_target(50, -n/2)
    ev3.screen.print(l_color.ambient())
    wait(50)
#r_motor
    while True:
        if r_color.ambient()>5:

            r_motor.run_time(0,0)
            l_motor.run_time(0,0)
            ev3.screen.print(r_color.ambient())
            wait(50)
            ev3.screen.print()
            break
        else:
            r_motor.run_time(50,100)
            ev3.screen.print(r_color.ambient()) 
#r_motor will find the white line behind the black line
    r_motor.run_time(-50,800)
    r_motor.reset_angle(0)
    while True:
        if r_color.ambient()>5:

            r_motor.run_time(0,0)
            l_motor.run_time(0,0)
            ev3.screen.print(r_color.ambient())
            wait(550)
            ev3.screen.print()
            break
        else:

            r_motor.run_time(-50,100)
    ev3.screen.print(r_motor.angle())
    wait(50)
    w = r_motor.angle()
    r_motor.run_target(50, -w/2)
    wait(100) 
    while True:
        if l_color.ambient()>5:

            r_motor.run_time(0,0)
            l_motor.run_time(0,0)
            ev3.screen.print(l_color.ambient())
            wait(50)
            ev3.screen.print()
            break
        else:
            l_motor.run_time(50,100) 
    #l_motor will find the white line behind the black line
    l_motor.run_time(-50,800)
    l_motor.reset_angle(0)
    while True:
        if l_color.ambient()>5:

            r_motor.run_time(0,0)
            l_motor.run_time(0,0)
            ev3.screen.print(l_color.ambient())
            wait(500)
            ev3.screen.print()
            break
        else:

            l_motor.run_time(-50,100)
    ev3.screen.print(l_motor.angle())
    wait(50)
    t = l_motor.angle()
    l_motor.run_target(50, -t/2)
    ev3.screen.print(l_color.ambient())
    wait(50)
    x=x+1



   