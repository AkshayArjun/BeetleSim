import rclpy
from rclpy.node import Node
import rclpy.waitable
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.timer import Rate
import math

message = '''laser avoidance system is active'''



class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')
        self.publishers_ = self.create_publisher(Twist, 'cmd_vel', 1)
        self.create_subscription(LaserScan, 'scan', self.listner_callback, 1)
        self.subscription = self.create_subscription


    def listner_callback(self, msg):
        num_points = len(msg.ranges[150:210])
        msg = self.data_cleaner(msg)

        right = sum(msg.ranges[150:180])
        left = sum(msg.ranges[180:210])
        print(right, left)
        print(num_points)
        self.publishers_.publish(self.converter(right, left, msg))
     
        print(num_points)
    
    def data_cleaner(self , msg):
        left = 0
        right = 0 
        k = 150
        for i in msg.ranges[150:210]:
            if i > 12:
                msg.ranges[k] = 12
            k+=1
        
        return msg


    def converter(self, right, left, msg):
        speed = 1.0
        turn = 1.0
        X = 0
        Y = 0
        Z = 0 
        th = 0
        vel = Twist()
        vel.linear.x = X*speed
        vel.linear.y = Y*speed
        vel.linear.z = Z*speed
        vel.angular.x = 0.0
        vel.angular.y = 0.0
        vel.angular.z = th*turn 

        if right < left:
            if sum(msg.ranges[175:185]) < 10.0:
                vel.linear.x = -2.0 
            else:
                vel.angular.z = 1.0
                vel.linear.x = 0.5
        else:
            if sum(msg.ranges[175:185]) < 10.0:
                vel.linear.x = -2.0
            else:
                vel.angular.z = -1.0
                vel.linear.x = 0.5
       
        return vel

def main(args=None):
    print(message)
    rclpy.init(args=args)
    avoider = ObstacleAvoider()
    rclpy.spin(avoider)
    avoider.destroy_node()
    rclpy.shutdown()
    print("obstacle avoidancenode has shutdown")


if __name__ == '__main__':
    main()