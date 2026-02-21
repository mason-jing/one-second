#!/bin/bash

# Number to guess: How many times can we execute the `true` command in a second?

# Commands: 5,000
# Time: 3.022517 seconds
# Rate: 1,654 commands/second


NUMBER="$1"

# Record start time in nanoseconds (remove the decimal point to get integer nanoseconds)
start_ns=$(date +%s%N)

# shellcheck disable=SC2034
for i in $(seq "$NUMBER"); do
    /usr/bin/env true;
done

# Record end time in nanoseconds (remove the decimal point to get integer nanoseconds)
end_ns=$(date +%s%N)

# Calculate elapsed time in nanoseconds using Bash arithmetic
elapsed_ns=$((end_ns - start_ns))

# Convert to seconds (with 6 decimal places for display)
# 1 second = 1,000,000,000 nanoseconds
elapsed_sec=$((elapsed_ns / 1000000000))          # Integer seconds
elapsed_subsec_ns=$((elapsed_ns % 1000000000))    # Remaining nanoseconds
elapsed_microsec=$((elapsed_subsec_ns / 1000))    # Convert to microseconds (6 decimal places)

# Calculate rate (commands per second) - multiply by 1000000000 to avoid decimals
# Then divide to get the final rate
rate=$(( (NUMBER * 1000000000) / elapsed_ns ))

printf "Commands: %'d\n" "$NUMBER"
printf "Time: %d.%06d seconds\n" "$elapsed_sec" "$elapsed_microsec"
printf "Rate: %'d commands/second\n" "$rate"
