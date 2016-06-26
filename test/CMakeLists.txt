# gumbo_query tests

################################################################################
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
################################################################################

include_directories(${Gumbo_INCLUDE_DIRS})
include_directories(${gumbo_query_SOURCE_DIRECTORY})

add_executable(test_id ID.cpp)

set(tests test_id)
target_link_libraries(${tests} gq gumbo)

set_property(TARGET ${tests} PROPERTY CXX_STANDARD 11)
set_property(TARGET ${tests} PROPERTY CXX_STANDARD_REQUIRED ON)
