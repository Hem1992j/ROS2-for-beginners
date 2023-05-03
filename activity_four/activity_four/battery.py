#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_custom_interfaces.srv import SetLed
from functools import partial


class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery_node")
        self.battery_state = "full"
        self.battery_timer = self.create_timer(0.1, self.check_battery_state)
        self.last_time_battery_status_changed = self.get_current_time()
        self.last_time_battery_status = [0, 0, 0]
        self.get_logger().info("the battery node  has been started...")

    def get_current_time(self):
        secs, nsecs = self.get_clock().now().seconds_nanoseconds()
        return secs + nsecs/100000000.0

    def check_battery_state(self):
        time_now = self.get_current_time()
        if self.battery_state == "full":
            if time_now - self.last_time_battery_status_changed > 3.0:
                self.battery_state = "empty"
                self.get_logger().info("the battery is empty..")
                self.last_time_battery_status_changed = time_now
                self.call_set_led_server(3, 1)
        else:
            if time_now - self.last_time_battery_status_changed > 6.0:
                self.battery_state = "full"
                self.get_logger().info("the battery is full again..")
                self.last_time_battery_status_changed = time_now
                self.call_set_led_server(3, 0)

    def call_set_led_server(self, led_number, state):
        led_client = self.create_client(SetLed, "set_led")

        # we will wait for the service to be up and running
        while not led_client.wait_for_service(1.0):
            self.get_logger().warn("the service is not up yet...")

        # send the request
        request = SetLed.Request()
        request.led_number = led_number
        request.led_state = state

        # wait for the response
        future = led_client.call_async(request)
        future.add_done_callback(
            partial(self.callback_call_set_led, led_number=led_number, state=state))

    def callback_call_set_led(self, future, led_number, state):
        try:
            response = future.result()
            self.get_logger().info(str(response.success))
        except Exception as e:
            self.get_logger().info("service call failed %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
