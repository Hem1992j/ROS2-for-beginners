cmake_minimum_required(VERSION 3.8)
project(my_custom_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Status.msg"
  "msg/LedStatesArray.msg"
  "srv/ComputeSquareArea.srv"
  "srv/SetLed.srv"
)



ament_package()
