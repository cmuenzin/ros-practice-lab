import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_interfaces.action import Frog


class MoveNode(Node):
    def __init__(self):
        super().__init__('move_node')
        self.server = ActionServer(self, Frog, 'move', self.execute)

    def execute(self, goal_handle):
        for _ in range(3):  # simulate 3 s of driving
            goal_handle.publish_feedback(Frog.Feedback(resulit='executing'))
            time.sleep(1)
        goal_handle.succeed()
        return Frog.Result(status='completed')


def main():
    rclpy.init()
    rclpy.spin(MoveNode())
