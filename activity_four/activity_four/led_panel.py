#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_custom_interfaces.msg import LedStatesArray
from my_custom_interfaces.srv import SetLed


class LedPanelNode(Node):
    def __init__(self):
        super().__init__("led_panel_node")
        self.led_states_ = [0, 0, 0]
        self.led_state_publisher = self.create_publisher(
            LedStatesArray, "led_states", 10)
        self.led_pub_timer = self.create_timer(4.0, self.publish_led_states)
        self.set_led_service = self.create_service(
            SetLed, "set_led", self.callback_set_led)
        self.get_logger().info("Led panel node is started.....")

    def publish_led_states(self):
        msg = LedStatesArray()
        msg.led_states = self.led_states_
        self.led_state_publisher.publish(msg)

    def callback_set_led(self, request, response):
        led_number = request.led_number
        states = request.led_state

        if led_number > len(self.led_states_) or led_number <= 0:
            response.success = False
            return response

        if states not in [0, 1]:
            response.success = False
            return response

        self.led_states_[led_number-1] = states
        response.success = True
        # we will publish the state of the led once we change the state of the led.
        self.publish_led_states()
        return response


def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
