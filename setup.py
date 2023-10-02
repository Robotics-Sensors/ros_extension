from setuptools import setup, find_packages

setup(
    name="ros_extension",
    version="0.1.0",  # Set the appropriate version
    description="ROS Extensions",
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
    project_urls={
        "Home": "https://github.com/RonaldsonBellande/ros_extension",
        "Homepage": "https://github.com/RonaldsonBellande/ros_extension",
        "documentation": "https://github.com/RonaldsonBellande/ros_extension",
        "repository": "https://github.com/RonaldsonBellande/ros_extension",
    },
)
