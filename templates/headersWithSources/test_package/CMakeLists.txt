cmake_minimum_required(VERSION 3.5)
project(PackageTest CXX)

message("PackageTest cmake")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(myTest test.cpp)
target_link_libraries(myTest ${CONAN_LIBS})
target_compile_features(myTest PUBLIC cxx_std_17)
