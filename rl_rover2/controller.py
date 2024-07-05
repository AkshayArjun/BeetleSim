#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


import termios
import tty

import sys

from geometry_msgs.msg import Twist

TwistMsg = Twist

msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit
"""

moveBindings = {
        'i':(1,0,0,0),
        'o':(1,0,0,-1),
        'j':(0,0,0,1),
        'l':(0,0,0,-1),
        'u':(1,0,0,1),
        ',':(-1,0,0,0),
        '.':(-1,0,0,1),
        'm':(-1,0,0,-1),
        'k':(0,0,0,0)
}

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
        'w':(1.1,1),
        'x':(.9,1),
        'e':(1,1.1),
        'c':(1,.9),
    }

class controller(Node):

    def __init__(self):
        super().__init__('controller')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 1)
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.th = 0.0
        self.speed = 0.0
        self.turn = 0.0
        self.done = False
    

    def update(self, x, y, z, th, speed, turn):
        self.x = x
        self.y = y
        self.z = z
        self.th = th
        self.speed = speed
        self.turn = turn
    

    def publish(self):
        msg = Twist()
        msg.linear.x = self.x * self.speed
        msg.linear.y = self.y * self.speed
        msg.linear.z = self.z * self.speed
        msg.angular.x = 0
        msg.angular.y = 0
        msg.angular.z = self.th * self.turn
        self.publisher_.publish(msg)

      

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def saveTerminalSettings():
    if sys.platform == 'win32':
        return None
    return termios.tcgetattr(sys.stdin)

def restoreTerminalSettings(old_settings):
    if sys.platform == 'win32':
        return
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

def vels(speed, turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = saveTerminalSettings()
    rclpy.init(args=None)

    controller_run = controller()
    rclpy.spin(controller_run)

    speed = controller_run.speed
    turn = controller_run.turn
    speed_limit = 0.5
    turn_limit = 1.0



    print(msg)
    print(vels(speed, turn))
    x = 0
    y = 0
    z = 0
    th = 0

    controller_run.update(x, y, z, th, speed, turn)
    controller_run.publish()

    while(1):
        key = get_key()
        if key in moveBindings.keys():
            x = moveBindings[key][0]
            y = moveBindings[key][1]
            z = moveBindings[key][2]
            th = moveBindings[key][3]
        elif key in speedBindings.keys():
            speed = speed * speedBindings[key][0]
            turn = turn * speedBindings[key][1]

            if speed > speed_limit:
                speed = speed_limit
            elif speed < -speed_limit:
                speed = -speed_limit

            if turn > turn_limit:
                turn = turn_limit
            elif turn < -turn_limit:
                turn = -turn_limit
        else:
                # Skip updating cmd_vel if key timeout and robot already
                # stopped.
            if key == '' and x == 0 and y == 0 and z == 0 and th == 0:
                continue
            
            x = 0
            y = 0
            z = 0
            th = 0
            if (key == '\x03'):
                break

        controller_run.update(x, y, z, th, speed, turn)
    
    controller_run.destroy_node()
    rclpy.shutdown()
    restoreTerminalSettings(settings)
        

       