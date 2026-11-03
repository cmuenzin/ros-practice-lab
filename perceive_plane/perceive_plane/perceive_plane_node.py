import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_interfaces.action import Frog


class PerceivePlaneNode(Node):
    def __init__(self):
        super().__init__('perceive_plane_node')
        self.server = ActionServer(self, Frog, 'perceive_plane', self.execute)

    def execute(self, goal_handle):
        self.get_logger().info(f'Perceiving plane: {goal_handle.request.order}')
        for _ in range(2):  # simulate 2 s of scanning for the plane
            goal_handle.publish_feedback(Frog.Feedback(resulit='executing'))
            time.sleep(1)
        goal_handle.succeed()
        self.get_logger().info('Plane perceived')
        return Frog.Result(status='completed')


def main():
    rclpy.init()
    rclpy.spin(PerceivePlaneNode())
