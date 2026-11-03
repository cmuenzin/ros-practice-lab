# ROS practice lab (SER, WS 2026)

Simulated task execution on a mobile manipulator with ROS 2 Humble.
One package per robot action, each exposing one action server, plus a
`robot` package that runs a task (an ordered sequence of actions).

| Package | Action server | Owner |
|---|---|---|
| `action_interfaces` | shared interface `Frog` | Nikita |
| `move` | `/move` | Caspar |
| `perceive_plane` | `/perceive_plane` | Adil |
| `pick` | `/pick` | Nikita |
| `place` | `/place` | Nikita |
| `robot` | client, runs the task (builder pattern) | open |

## Interface `action_interfaces/action/Frog`

```
string order     # goal: what to do, e.g. "table"
---
string status    # result: "completed"
---
string resulit   # feedback: "executing"
```

## Conventions

- Action server name = package name (`/move`, `/pick`, ...).
- Each action package depends on `action_interfaces` (`<depend>` in
  `package.xml`) and registers its node in `setup.py` under
  `console_scripts`, e.g. `'move_node = move.move_node:main'`.
- `move/move/move_node.py` is the template for the other action nodes.

## Setup

Clone into the `src` folder of a ROS 2 workspace:

```bash
cd ~/ros2_ws/src && git clone https://github.com/cmuenzin/ros-practice-lab.git ser_lab
```

Build and source (in every new terminal, source again after each build):

```bash
cd ~/ros2_ws && colcon build --symlink-install --base-paths src/ser_lab
```

```bash
source ~/ros2_ws/install/setup.bash
```

## Try one action

```bash
ros2 run move move_node
```

```bash
ros2 action send_goal --feedback /move action_interfaces/action/Frog "{order: table}"
```
