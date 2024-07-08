import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


msg = '''laser avoidance system is active'''


MAX_RANGE = 0.15


class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')

        self.create_subscription(LaserScan, 'scan', self.listner_callback, 1)
        self.subscription = self.create_subscription

    def listner_callback(self, msg):
        num_points = len(msg.ranges)
        print('number of point: ' , num_points)

        print('angle at 0 :' , msg.ranges[0])
        print('angle at 180 :' , msg.ranges[179])
        print('angle at 360 :' , msg.ranges[359])
def main(args=None):
    rclpy.init(args=args)
    avoider = ObstacleAvoider()
    rclpy.spin(avoider)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    avoider.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()