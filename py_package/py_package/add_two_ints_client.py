#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial


class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.add_two_ints_client(5, 7)

    def add_two_ints_client(self, a, b):
        # Initialize the client
        client = self.create_client(AddTwoInts, "add_two_ints")

        # wait for the service
        while not client.wait_for_service():
            self.get_logger().warn("Waiting for the server add_two_ints")

        # send request data
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        # wait for the future response
        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_call_add_two_ints, a=a, b=b))

    def callback_call_add_two_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(str(a) + " + " + str(b) + " = " + str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e, ))


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
