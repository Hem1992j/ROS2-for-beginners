#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class NumberSubscriberNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.node_name = "number_counter"
        self.number_subscriber = self.create_subscription(
            Int64, "number", self.listener_callback, 10)
        self.get_logger().info(f"{self.node_name} has been initiated...")

    def listener_callback(self, msg):
        self.get_logger().info("Number node is publishing " + str(msg.data))


def main(args=None):
    rclpy.init(args=args)
    node = NumberSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
