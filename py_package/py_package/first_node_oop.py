#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class FirstNode(Node):
    def __init__(self):
        super().__init__("my_first_node")
        self.counter = 0
        self.create_timer(1.0, self.timer_callback)
        self.get_logger().info(" my_first_node has been initiated...")

    def timer_callback(self):
        self.counter += 1
        self.get_logger().info(f"I am printing counter: {self.counter}")


def main(args=None):
    rclpy.init(args=args)
    node = FirstNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
