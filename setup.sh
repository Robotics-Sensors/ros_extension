#!/bin/bash

# Create directory if it doesn't exist
if [ ! -d ~/.config/ros_extension ]; then
    mkdir -p ~/.config/ros_extension
fi

# Move script to the appropriate directory
cp ./scripts/toggle_ros_versions.sh ~/.config/ros_extension

# Define the content to be added
content=$'
ros_toggle_version_function() {
    # Specify the path to your script here
    ~/.config/ros_extension/toggle_ros_versions.sh
    source ~/.bashrc
}
'

# Add content to ~/.bashrc if not present
if ! grep -q "ros_toggle_version_function()" ~/.bashrc; then
    printf "%s\n" "$content" >> ~/.bashrc
    source ~/.bashrc
fi

source ~/.bashrc
