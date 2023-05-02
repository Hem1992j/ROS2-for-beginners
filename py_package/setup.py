from setuptools import setup

package_name = 'py_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hem',
    maintainer_email='rauljihemrajsinh89@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "first_node = py_package.first_node_oop:main",
            "first_publisher = py_package.my_first_publisher:main",
            "first_subscriber = py_package.my_first_subscriber:main",
            "add_two_ints_server = py_package.add_two_ints_server:main",
            "add_two_ints_client = py_package.add_two_ints_client:main"
        ],
    },
)
