import time
import rclpy
from rclpy.node import  Node
import numpy as np
from geometry_msgs.msg import Twist
import sys
import termios
import tty


msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   q    w    e
   a    s    d
   z         c

x : stop 

t : up (+z)
b : down (-z)



i/k : increase/decrease max speeds by 10%
o/l : increase/decrease only linear speed by 10%
p/; : increase/decrease only angular speed by 10%

CTRL-C to quit
"""

moveBindings = {
        'w':(1,0,0,0),
        'e':(1,0,0,-1),
        'a':(0,0,0,1),
        'd':(0,0,0,-1),
        'q':(1,0,0,1),
        's':(-1,0,0,0),
        'c':(-1,0,0,1),
        'z':(-1,0,0,-1),
        'x':(0,0,0,0)
}

speedBindings={
        'i':(1.1,1.1),
        'k':(.9,.9),
        'o':(1.1,1),
        'l':(.9,1),
        'p':(1,1.1),
        ';':(1,.9),
    }


class ControllerNode(Node):
    def __init__(self):
        super().__init__("controller")

        self.controller_publisher_ = self.create_publisher(Twist, "cmd_vel", 1)
        self.controller_timer_ = self.create_timer(0.5, self.publish_controller)
    
    def publish_controller(self):
        velo = self.converter()
        self.controller_publisher_.publish(velo)
    
    def converter(self):
        key = get_key()
        speed = 1.0
        turn = 1.0
        X = 0
        Y = 0
        Z = 0 
        th = 0
        if key in moveBindings.keys():
            X = moveBindings[key][0]
            Y = moveBindings[key][1]
            Z = moveBindings[key][2]
            th = moveBindings[key][3]
        elif key in speedBindings.keys():
            speed = speed * speedBindings[key][0]
            turn = turn * speedBindings[key][1]
        
        vel = Twist()
        vel.linear.x = X*speed
        vel.linear.y = Y*speed
        vel.linear.z = Z*speed
        vel.angular.x = 0.0
        vel.angular.y = 0.0
        vel.angular.z = th*turn 

        return vel  
def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def main(args=None):
    print(msg)
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
