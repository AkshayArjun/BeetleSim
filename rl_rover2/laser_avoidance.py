import rclpy
from rclpy.node import Node
import rclpy.waitable
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.timer import Rate


message = '''laser avoidance system is active'''



class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')
        self.publishers_ = self.create_publisher(Twist, 'cmd_vel', 1)
        self.create_subscription(LaserScan, 'scan', self.listner_callback, 1)
        self.subscription = self.create_subscription


    def listner_callback(self, msg):
        num_points = len(msg.ranges[150:210])
        right = sum(msg.ranges[150:180])
        left = sum(msg.ranges[180:210])
        print(right, left)
        print(num_points)
        self.publishers_.publish(self.converter(right, left))
     
        print(num_points)


    def converter(self, right, left):
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
            vel.angular.z = 0.1
            vel.linear.x = 0.1
        elif right > left:
            vel.angular.z = -0.1
            vel.linear.x = 0.1
        else:
            vel.angular.z = 0.0
            vel.linear.x = 0.1
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