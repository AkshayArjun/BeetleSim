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

## Whats next 

- Implemetnting RL based algortihmns Like DDPG, SAC for autonomous navigation.
- Implementing a dynamic APF algorithm

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





