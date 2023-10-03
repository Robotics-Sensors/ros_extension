#!/usr/bin/env python3

import os
import fileinput

def toggle_ros_versions():
    bashrc_path = os.path.expanduser("~/.bashrc")

    # Check if ROS 1 (Noetic) is uncommented
    if any("# source /opt/ros/foxy/setup.bash" in line for line in open(bashrc_path)):
        # Comment out ROS 1 (Noetic) and uncomment ROS 2 (Foxy)
        replace_line(bashrc_path, 'source /opt/ros/noetic/setup.bash', '# source /opt/ros/noetic/setup.bash')
        replace_line(bashrc_path, '# source /opt/ros/foxy/setup.bash', 'source /opt/ros/foxy/setup.bash')

    else:
        # Uncomment ROS 2 (Foxy) and comment ROS 1 (Noetic)
        replace_line(bashrc_path, 'source /opt/ros/foxy/setup.bash', '# source /opt/ros/foxy/setup.bash')
        replace_line(bashrc_path, '# source /opt/ros/noetic/setup.bash', 'source /opt/ros/noetic/setup.bash')

    # Check if ROS_VERSION is set to 2
    if any("# export ROS_VERSION=2" in line for line in open(bashrc_path)):
        # Comment out ROS_VERSION=1 and uncomment ROS_VERSION=2
        replace_line(bashrc_path, 'export ROS_VERSION=1', '# export ROS_VERSION=1')
        replace_line(bashrc_path, '# export ROS_VERSION=2', 'export ROS_VERSION=2')

    else:
        # Uncomment ROS_VERSION=2 and comment ROS_VERSION=1
        replace_line(bashrc_path, 'export ROS_VERSION=2', '# export ROS_VERSION=2')
        replace_line(bashrc_path, '# export ROS_VERSION=1', 'export ROS_VERSION=1')

def replace_line(file_path, old_line, new_line):
    with fileinput.FileInput(file_path, inplace=True) as file:
        for line in file:
            print(line.replace(old_line, new_line), end='')
