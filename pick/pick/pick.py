import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
import time

from action_interfaces.action import Frog


class PickServer(Node):

    def __init__(self):
        super().__init__('pick_action_server')
        self._action_server = ActionServer(
            self,
            Frog,
            'pick',
            self.pick_callback)

    def pick_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        obect = goal_handle.request.order

        feedback_msg = Frog.Feedback()
        steps = [
            f'Moving towards {obect}',
            f'Grasping {obect}',
            f'Lifting {obect}'
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

    pick_server = PickServer()

    rclpy.spin(pick_server)
    pick_server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()