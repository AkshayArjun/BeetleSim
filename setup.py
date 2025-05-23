from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'rl_rover2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share' , package_name , 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share' , package_name , 'description'), glob('description/*.xacro')),
        (os.path.join('share' , package_name , 'config'), glob('config/*.xacro'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='akshay',
    maintainer_email='aakshay1114@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = rl_rover2.publisher:main',
            'controller = rl_rover2.controller:main',
            'controller2 = rl_rover2.controller2:main',
            'laser_avoidance = rl_rover2.laser_avoidance:main',
            'odom_val = rl_rover2.odom_val:main',
        ],
    },
)
