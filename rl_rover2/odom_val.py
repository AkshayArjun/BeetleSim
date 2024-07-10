import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class odom_cal(Node):

    def __init__(self):
        super().__init__('odom_val')
        self.create_subscription(Odometry, 'odom/unfiltered', self.timer_callback, 1)
        self.subscription = self.create_subscription

    def timer_callback(self, msg):
        self.filter_msg(msg)
        print('\n')
        print('Received odometry message' , '\n')
        print('Position: [x: {}, y: {}, z: {}]'.format(msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z))
        print('Orientation: [x: {}, y: {}, z: {}, w: {}]'.format(msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w))
        print('linear velocity: [x: {}, y: {}, z: {}]'.format(msg.twist.twist.linear.x, msg.twist.twist.linear.y, msg.twist.twist.linear.z))
        print('angular velocity: [x: {}, y: {}, z: {}]'.format(msg.twist.twist.angular.x, msg.twist.twist.angular.y, msg.twist.twist.angular.z))
        print('\n')
        print('-----------------------------------')
    
    def filter_msg(self, msg):
        msg.pose.pose.position.x = round(msg.pose.pose.position.x, 2)
        msg.pose.pose.position.y = round(msg.pose.pose.position.y, 2)
        msg.pose.pose.position.z = round(msg.pose.pose.position.z, 2)
        msg.pose.pose.orientation.x = round(msg.pose.pose.orientation.x, 2)
        msg.pose.pose.orientation.y = round(msg.pose.pose.orientation.y, 2)
        msg.pose.pose.orientation.z = round(msg.pose.pose.orientation.z, 2)
        msg.pose.pose.orientation.w = round(msg.pose.pose.orientation.w, 2)
        msg.twist.twist.linear.x = round(msg.twist.twist.linear.x, 2)
        msg.twist.twist.linear.y = round(msg.twist.twist.linear.y, 2)
        msg.twist.twist.linear.z = round(msg.twist.twist.linear.z, 2)
        msg.twist.twist.angular.x = round(msg.twist.twist.angular.x, 2)
        msg.twist.twist.angular.y = round(msg.twist.twist.angular.y, 2)
        msg.twist.twist.angular.z = round(msg.twist.twist.angular.z, 2)
        return msg

def main():
    rclpy.init()
    odom_cal_node = odom_cal()
    rclpy.spin(odom_cal_node)
    odom_cal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
# This code is a subscriber that listens to the /odom/unfiltered topic and prints the values of the position and orientation of the robot in the world frame.
