import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
import time

from action_interfaces.action import Frog


class PlaceServer(Node):

    def __init__(self):
        super().__init__('place_action_server')
        self._action_server = ActionServer(
            self,
            Frog,
            'place',
            self.place_callback)

    def place_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        location = goal_handle.request.order

        feedback_msg = Frog.Feedback()
        steps = [
            f'Looking for {location}',
            f'Navigating towards {location}',
            f'Placeing the object at {location}'
        ]

        for step in steps:
            feedback_msg.resulit = step
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(step)
            time.sleep(1)

        goal_handle.succeed()
        result = Frog.Result()
        result.status = 'DONE'
        return result


def main(args=None):
    rclpy.init(args=args)

    place_server = PlaceServer()

    rclpy.spin(place_server)
    place_server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()