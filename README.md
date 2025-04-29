# BeetleSim

**BeetleSim** is a virtual simulation platform designed for the autonomous warehouse vehicle built by the Automation and Robotics Club of BITS hyderabad, **Beetle**. Built on **ROS 2**, BeetleSim provides a realistic environment to develop, test, and validate navigation algorithms, SLAM, laser-based guidance, and warehouse logistics operations.

---

## Features

- Complete integration with ROS 2 middleware
- Simulation of static and dynamic warehouse environments
- Autonomous navigation using path planning and obstacle avoidance
- Real-time SLAM (Simultaneous Localization and Mapping)
- Task execution capabilities such as crate transport and docking
- RViz2 visualization for mapping, localization, and path tracking
- Extendable framework to support multi-robot systems and fleet coordination

---

## Requirements

- ROS 2 (Humble or Foxy recommended)
- Gazebo or Ignition Fortress (for 3D simulation)
- Navigation2 (Nav2) stack
- SLAM Toolbox or GMapping
- ros2_control framework
- Supported LIDAR and IMU sensor simulation plugins

---
```
├── LICENSE
├── README.md
├── build
│   ├── bdist.linux-x86_64
│   └── lib
│       └── rl_rover2
│           ├── __init__.py
│           ├── controller.py
│           ├── controller2.py
│           ├── laser_avoidance.py
│           ├── odom_val.py
│           └── publisher.py
├── config
│   └── mapper_params_online_async.yaml
├── description
│   ├── gazebo_control.xacro
│   ├── inertial_macros.xacro
│   ├── lidar.xacro
│   ├── robot_core.xacro
│   └── rover.urdf.xacro
├── launch
│   ├── description.launch.py
│   └── gzsim.launch.py
├── package.xml
├── resource
│   └── rl_rover2
├── rl_rover2
│   ├── __init__.py
│   ├── __pycache__
│   ├── controller.py
│   ├── controller2.py
│   ├── laser_avoidance.py
│   ├── odom_val.py
│   └── publisher.py
├── setup.cfg
├── setup.py
```
--- 

## Installation

```bash
# Create and initialize a ROS 2 workspace
mkdir -p ~/beetle_ws/src
cd ~/beetle_ws/src

# Clone the BeetleSim repository
git clone https://github.com/AkshayArjun/beetlesim.git

# Build the workspace
cd ~/beetle_ws
colcon build

# Source the workspace
source install/setup.bash


```
--- 



https://github.com/user-attachments/assets/9d2fd66c-62ac-46b8-a441-96e29ba9a314
![Beetle v1](https://github.com/user-attachments/assets/67026e21-c636-4c04-a8f9-87400a79cc99)
