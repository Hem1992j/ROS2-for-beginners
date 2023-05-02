#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class FirstSubscriberNode(Node):
    def __init__(self):
        super().__init__("my_first_subscriber_node")
        self.hello_subscriber = self.create_subscription(
            String, "hello_publisher", self.listener_callback, 10)
        self.get_logger().info(" Subscriber node has been initiated...")

    def listener_callback(self, msg):
        self.get_logger().info(str(msg.data))


def main(args=None):
    rclpy.init(args=args)
    node = FirstSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
