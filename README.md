# ROS practice lab

| Package | Action server | Owner |
|---|---|---|
| `action_interfaces` | shared interface `Frog` | Nikita |
| `move` | `/move` | Caspar |
| `perceive_plane` | `/perceive_plane` | Adil |
| `pick` | `/pick` | Nikita |
| `place` | `/place` | Nikita |
| `robot` | client, runs the task (builder pattern) | tbd |

## Interface `action_interfaces/action/Frog`

```
string order     # goal: what to do, e.g. "table"
---
string status    # result: "completed"
---
string resulit   # feedback: "executing"
```

## Setup

Clone into the `src` folder of a ROS 2 workspace

```bash
cd ~/ros2_ws/src && git clone https://github.com/cmuenzin/ros-practice-lab.git ser_lab
```

Build and source

```bash
cd ~/ros2_ws && colcon build --symlink-install --base-paths src/ser_lab
```

```bash
source ~/ros2_ws/install/setup.bash
```

## Try action

```bash
ros2 run move move_node
```

```bash
ros2 action send_goal --feedback /move action_interfaces/action/Frog "{order: table}"
```
