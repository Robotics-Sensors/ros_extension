#!/bin/bash

# Add ROS configurations to ~/.bashrc if not present
configs_check() {
    if ! grep -q "source /opt/ros/noetic/setup.bash" ~/.bashrc; then
        echo 'source /opt/ros/noetic/setup.bash' >> ~/.bashrc
        echo 'export ROS_VERSION=1' >> ~/.bashrc
    fi

    if ! grep -q "source /opt/ros/foxy/setup.bash" ~/.bashrc; then
        echo 'source /opt/ros/foxy/setup.bash' >> ~/.bashrc
        echo 'export ROS_VERSION=2' >> ~/.bashrc
    fi
}


# Function to toggle between ROS 1 (Noetic) and ROS 2 (Foxy) in ~/.bashrc
toggle_ros_versions() {
    # Check if ROS 1 (Noetic) is uncommented
    if grep -q "# source /opt/ros/foxy/setup.bash" ~/.bashrc; then
        # Comment out ROS 1 (Noetic) and uncomment ROS 2 (Foxy)
        sed -i 's|^source /opt/ros/noetic/setup.bash|# source /opt/ros/noetic/setup.bash|' ~/.bashrc
        sed -i 's|^# source /opt/ros/foxy/setup.bash|source /opt/ros/foxy/setup.bash|' ~/.bashrc

    else
        # Uncomment ROS 2 (Foxy) and comment ROS 1 (Noetic)
        sed -i 's|^source /opt/ros/foxy/setup.bash|# source /opt/ros/foxy/setup.bash|' ~/.bashrc
        sed -i 's|^# source /opt/ros/noetic/setup.bash|source /opt/ros/noetic/setup.bash|' ~/.bashrc
    fi

    # Check if ROS 1 (Noetic) is uncommented
    if grep -q "# \export ROS_VERSION=2" ~/.bashrc; then
        # Comment out ROS 1 (Noetic) and uncomment ROS 2 (Foxy)
        sed -i 's|^export ROS_VERSION=1|# export ROS_VERSION=1|' ~/.bashrc
        sed -i 's|^# export ROS_VERSION=2|export ROS_VERSION=2|' ~/.bashrc

    else
        # Uncomment ROS 2 (Foxy) and comment ROS 1 (Noetic)
        sed -i 's|^export ROS_VERSION=2|# export ROS_VERSION=2|' ~/.bashrc
        sed -i 's|^# export ROS_VERSION=1|export ROS_VERSION=1|' ~/.bashrc
    fi

}

# Call the function to check and add ROS configurations
configs_check

# Call the function to toggle between ROS versions
toggle_ros_versions

# Source ~/.bashrc to apply changes
source ~/.bashrc

# Notify user of the current ROS version
echo "ROS$ROS_VERSION"
