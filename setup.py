from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ros_extension",
    version="0.1.0",
    description="ROS Extensions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="RonaldsonBellande",
    author_email="ronaldsonbellande@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        # List your dependencies here
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
    ],
    keywords=["package", "setuptools"],
    python_requires=">=3.0",
    extras_require={
        "dev": ["pytest", "pytest-cov[all]", "mypy", "black"],
    },
    entry_points={
        'console_scripts': [
            'toggle_ros_versions = ros_toggle_extension.toggle_ros_versions_extension:toggle_ros_versions',
            'run_colcon_in_src = ros_colcon_extension.colcon_src_extension:run_colcon_in_src',
        ],
    },
    project_urls={
        "Home": "https://github.com/RonaldsonBellande/ros_extension",
        "Homepage": "https://github.com/RonaldsonBellande/ros_extension",
        "documentation": "https://github.com/RonaldsonBellande/ros_extension",
        "repository": "https://github.com/RonaldsonBellande/ros_extension",
    },
)
