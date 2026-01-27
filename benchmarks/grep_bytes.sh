#!/bin/bash 

# Number to guess: How many bytes can `grep` search, unsuccessfully, in a second?
# Note: the bytes are in memory

# Bytes: 5,000,000,000
# Time: 1.837374 seconds
# Rate: 2,721,274,561 bytes/second


NUMBER="$1"

# Record start time in nanoseconds (remove the decimal point to get integer nanoseconds)
start_ns=$(date +%s%N)

head -c "$NUMBER" < /dev/zero | grep blah

# Record end time in nanoseconds (remove the decimal point to get integer nanoseconds)
end_ns=$(date +%s%N)

# Calculate elapsed time in nanoseconds using Bash arithmetic
elapsed_ns=$((end_ns - start_ns))

# Convert to seconds (with 6 decimal places for display)
# 1 second = 1,000,000,000 nanoseconds
elapsed_sec=$((elapsed_ns / 1000000000))          # Integer seconds
elapsed_subsec_ns=$((elapsed_ns % 1000000000))    # Remaining nanoseconds
elapsed_microsec=$((elapsed_subsec_ns / 1000))    # Convert to microseconds (6 decimal places)

# Calculate rate (bytes per second) - multiply by 1000000000 to avoid decimals
# Then divide to get the final rate
rate=$(( (NUMBER * 1000000000) / elapsed_ns ))

printf "Bytes: %'d\n" "$NUMBER"
printf "Time: %d.%06d seconds\n" "$elapsed_sec" "$elapsed_microsec"
printf "Rate: %'d bytes/second\n" "$rate"
