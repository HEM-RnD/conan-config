cmake_minimum_required(VERSION 3.5)
project({{ name }})

message("Main cmake")

add_library(${CMAKE_PROJECT_NAME})

#Include conanbuildinfo.cmake from cmake generator. 
#Conan has to be installed before cmake run or conan-cmake-integration configured in cmake install parameters.
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

target_sources(${PROJECT_NAME} PUBLIC 
    # insert source fikes here, eg.: ${CMAKE_CURRENT_LIST_DIR}/src/my_file.cpp
    ${CMAKE_CURRENT_LIST_DIR}/src/DumpFile_please_replace_it_with_proper_source_files.cpp
)

target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC inc)
target_compile_features(${CMAKE_PROJECT_NAME} PUBLIC cxx_std_17)
target_link_libraries(${CMAKE_PROJECT_NAME} PUBLIC
    # insert here the packages names, that the package depands on, eg.: CONAN_PKG::HEM_OSAL
)

install(DIRECTORY .
        DESTINATION .
        FILES_MATCHING PATTERN "*.hpp")

install(DIRECTORY .
        DESTINATION .
        FILES_MATCHING PATTERN "*.h")

install(TARGETS ${CMAKE_PROJECT_NAME}
        LIBRARY
        DESTINATION lib
)
                      
#tests
set(BUILD_TESTING True)

add_test_suites(TESTS 
                # insert test files names here
                DumpTestFile_please_replace_it_with_proper_test_files
                IncludesTest
               LINK_LIBRARIES ${CMAKE_PROJECT_NAME}
)
