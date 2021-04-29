cmake_minimum_required(VERSION 3.5)
project({{ name }})

message("Main cmake")

include(cmake/packagemanager.cmake)

add_library(${CMAKE_PROJECT_NAME} INTERFACE)

target_include_directories(${CMAKE_PROJECT_NAME} INTERFACE inc)
target_compile_features(${CMAKE_PROJECT_NAME} INTERFACE cxx_std_17)
target_link_libraries(${CMAKE_PROJECT_NAME} INTERFACE 
                      # insert here the packages names, that the package depands on, eg.: CONAN_PKG::HEM_OSAL
                      )

install(DIRECTORY inc/ 
        DESTINATION inc/HEM/${CMAKE_PROJECT_NAME}
        FILES_MATCHING PATTERN "*.hpp")

install(DIRECTORY inc/ 
        DESTINATION inc/HEM/${CMAKE_PROJECT_NAME}
        FILES_MATCHING PATTERN "*.h")
                      
#tests
set(BUILD_TESTING True)

add_test_suites(TESTS 
                # insert test files names here
                DumpTestFile_please_replace_it_with_proper_test_files
                IncludesTest
               LINK_LIBRARIES ${CMAKE_PROJECT_NAME}
)