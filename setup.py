from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'ros2cv0_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # CRITICAL: This line tells ROS 2 to install your launch files
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cchung',
    maintainer_email='cchung@ltu.edu',
    description='how to display image frames on a Image topic in ROS2',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [ # package_name.node_file_name_without_py:main
            'image_view_exe = ros2cv0_pkg.image_view:main',
        ],
    },
)
