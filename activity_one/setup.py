from setuptools import setup

package_name = 'activity_one'

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
<<<<<<< HEAD
            "number_publisher = activity_one.number_publishe:main",
=======
            "number_publisher = activity_one.number_publisher:main",
>>>>>>> b2b2110 (added second activity)
            "number_counter = activity_one.number_counter:main"
        ],
    },
)
