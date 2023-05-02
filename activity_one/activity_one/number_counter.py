#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool


class NumberSubscriberNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.node_name = "number_counter"
        self.counter = 0
        self.reset_service = self.create_service(
            SetBool, "reset_counter", self.reset_counter_callback)
        self.number_subscriber = self.create_subscription(
            Int64, "number", self.listener_callback, 10)
        self.number_publisher = self.create_publisher(
            Int64, "number_count", 10)
        self.get_logger().info(f"{self.node_name} has been initiated...")

    def listener_callback(self, msg):
        self.counter += msg.data
        new_msg = Int64()
        new_msg.data = self.counter
        self.number_publisher.publish(new_msg)

    def reset_counter_callback(self, request, response):
        if request.data:
            self.counter = 0
            response.success = True
            response.message = "The counter has been set to zero again..."
            return response
        else:
            response.success = False
            return response


def main(args=None):
    rclpy.init(args=args)
    node = NumberSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
