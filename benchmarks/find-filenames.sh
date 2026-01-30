#!/bin/bash

# Number to guess: How many files can `find` list in a second?
# Note: the files will be in the filesystem cache.

# Files: 100,000
# Time: 2.718258 seconds
# Rate: 36,788 files/second


NUMBER="$1"

# Record start time in nanoseconds (remove the decimal point to get integer nanoseconds)
start_ns=$(date +%s%N)

find "/usr" 2> /dev/null | head -n "$NUMBER" > /dev/null

# Record end time in nanoseconds (remove the decimal point to get integer nanoseconds)
end_ns=$(date +%s%N)

# Calculate elapsed time in nanoseconds using Bash arithmetic
elapsed_ns=$((end_ns - start_ns))

# Convert to seconds (with 6 decimal places for display)
# 1 second = 1,000,000,000 nanoseconds
elapsed_sec=$((elapsed_ns / 1000000000))          # Integer seconds
elapsed_subsec_ns=$((elapsed_ns % 1000000000))    # Remaining nanoseconds
elapsed_microsec=$((elapsed_subsec_ns / 1000))    # Convert to microseconds (6 decimal places)

# Calculate rate (files per second) - multiply by 1000000000 to avoid decimals
# Then divide to get the final rate
rate=$(( (NUMBER * 1000000000) / elapsed_ns ))

printf "Files: %'d\n" "$NUMBER"
printf "Time: %d.%06d seconds\n" "$elapsed_sec" "$elapsed_microsec"
printf "Rate: %'d files/second\n" "$rate"
