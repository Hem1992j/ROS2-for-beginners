#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class FirstPublisherNode(Node):
    def __init__(self):
        super().__init__("my_first_publisher_node")
        # self.counter = 0
        self.hello_publisher = self.create_publisher(String, "hello_publisher", 10)
        self.hello_timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info(" Publisher node has been initiated...")

    def timer_callback(self):
        msg = String()
        msg.data = "Hello ROS2" 
        self.hello_publisher.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)
    node = FirstPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
