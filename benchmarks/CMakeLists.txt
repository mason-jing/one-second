cmake_minimum_required(VERSION 4.2.2)
project(one_second_benchmarks C)

set(CMAKE_C_STANDARD 23)

# Here's what the different optimization levels mean:
#   -O0 (default): No optimization. Compiles code as written, fastest compile time, easiest to debug.
#   -O1: Basic optimizations. Moderate compile time, some performance improvement.
#   -O2: More aggressive optimizations. Longer compile time, better performance. This is commonly used for production.
#   -O3: Maximum optimizations including aggressive inlining and vectorization.
#   -Os: Optimize for size rather than speed.
#
# Debug symbols:
#   -g: Include debug information for use with debuggers (gdb, CLion debugger, etc.)
#       Makes executable larger but allows you to debug with source code and variable names.
set(CMAKE_C_FLAGS "-g")

add_executable(check_c_version check_c_version.c)
add_executable(sum sum.c)
