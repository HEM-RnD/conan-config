cmake_minimum_required(VERSION 3.15.0)

set(CONAN_CMAKE_INTEGRATION_SOURCES_DIR ${CMAKE_BINARY_DIR})
set(CONAN_CMAKE_INTEGRATION_ENTRY_POINT_FILENAME conan-cmake-integration-entrypoint.cmake)
set(CONAN_CMAKE_INTEGRATION_SOURCES ${CMAKE_BINARY_DIR}/conan-cmake-integration-sources.tar.gz)

if(NOT DEFINED CACHE{CONAN_CMAKE_INTEGRATION_ENTRY_POINT})

    message(STATUS "Downloading conan-cmake-integration from https://bitbucket.org/hemrnd/conan-cmake-integration")
    file(DOWNLOAD "https://bitbucket.org/hemrnd/conan-cmake-integration/get/main.tar.gz"
                "${CONAN_CMAKE_INTEGRATION_SOURCES}"
                TLS_VERIFY ON)
    file(ARCHIVE_EXTRACT 
            INPUT "${CONAN_CMAKE_INTEGRATION_SOURCES}"
            DESTINATION ${CONAN_CMAKE_INTEGRATION_SOURCES_DIR})
    file(REMOVE "${CONAN_CMAKE_INTEGRATION_SOURCES}")

    file(GLOB_RECURSE CONAN_CMAKE_INTEGRATION_ENTRY_POINT
        ${CONAN_CMAKE_INTEGRATION_SOURCES_DIR}/**/${CONAN_CMAKE_INTEGRATION_ENTRY_POINT_FILENAME})
    if ("${CONAN_CMAKE_INTEGRATION_ENTRY_POINT}" STREQUAL "")
        message(FATAL_ERROR "Can't find ${CONAN_CMAKE_INTEGRATION_ENTRY_POINT_FILENAME}, something is wrong!")
    endif()

    set(CONAN_CMAKE_INTEGRATION_ENTRY_POINT ${CONAN_CMAKE_INTEGRATION_ENTRY_POINT} CACHE STRING "Conan integration entrypoint filename with path")
endif()

message(STATUS "Conan-cmake-integration found in ${CONAN_CMAKE_INTEGRATION_ENTRY_POINT}.")
include(${CONAN_CMAKE_INTEGRATION_ENTRY_POINT})