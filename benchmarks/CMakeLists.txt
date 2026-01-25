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


# 📋 Rebuild Instructions

# Option 1: Normal Rebuild
#   cd D:\My_Code\one-second\benchmarks\build
#   cmake --build .

# PowerShell One-Liner for Option 1:
#   cd D:\My_Code\one-second\benchmarks\build; cmake --build .


# Option 2: Clean Rebuild
#   cd D:\My_Code\one-second\benchmarks\build
#   cmake --build . --clean-first

# PowerShell One-Liner for Option 2:
#   cd D:\My_Code\one-second\benchmarks\build; cmake --build . --clean-first


# Option 3: Complete Clean Rebuild
#   cd D:\My_Code\one-second\benchmarks
#   Remove-Item -Recurse -Force build -ErrorAction SilentlyContinue
#   mkdir build
#   cd build
#   cmake -G "MinGW Makefiles" -DCMAKE_C_COMPILER=C:/msys64/ucrt64/bin/gcc.exe ..
#   cmake --build .

# PowerShell One-Liner for Option 3:
#   cd D:\My_Code\one-second\benchmarks; Remove-Item -Recurse build -ErrorAction SilentlyContinue; mkdir build; cd build; cmake -G "MinGW Makefiles" -DCMAKE_C_COMPILER=C:/msys64/ucrt64/bin/gcc.exe ..; cmake --build .

