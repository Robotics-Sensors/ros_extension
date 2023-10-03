#!/usr/bin/env python3

import os
import subprocess

def find_src_directory():
    current_directory = os.getcwd()

    while current_directory != '/':
        src_directory = os.path.join(current_directory, 'src')
        if os.path.exists(src_directory) and os.path.isdir(src_directory):
            return current_directory

        current_directory = os.path.dirname(current_directory)

    raise FileNotFoundError("src directory not found in parent directories.")

def run_colcon_in_src(src_directory):
    try:
        subprocess.run(['colcon', 'build'], check=True, cwd=src_directory)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        exit(1)
