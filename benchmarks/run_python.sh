#!/bin/bash

# ---------------------------------------------------------------------------------------------------------
# ATTENTION: "python" is an alias in my ~/.bashrc, and aliases don't work in non-interactive bash scripts.

# Aliases are only loaded in interactive shells by default.

# When you run a bash script with #!/bin/bash, it starts a non-interactive shell that:
#   1. Does NOT load ~/.bashrc
#   2. Does NOT expand aliases (even if they were loaded)

# Interactive vs Non-Interactive Shells:
# |     Shell Type          | Loads ~/.bashrc? | Expands Aliases? |       Example
# | Interactive             |     ✅ Yes       |     ✅ Yes       |  Your terminal prompt
# | Non-interactive script  |     ❌ No        |     ❌ No        |  ./script.sh
# | Non-interactive with -i |     ✅ Yes       |     ✅ Yes       |  bash -i script.sh
# ---------------------------------------------------------------------------------------------------------


# Enable alias expansion in this non-interactive script
shopt -s expand_aliases
# Define the python alias (same as in ~/.bashrc)
alias python=/usr/bin/python3


# Number to guess: How many times can we start the Python interpreter in a second?

# Iterations: 200
# Time: 1.592725 seconds
# Rate: 125 iterations/second


NUMBER="$1"

# Record start time in nanoseconds (remove the decimal point to get integer nanoseconds)
start_ns=$(date +%s%N)

# shellcheck disable=SC2034
for i in $(seq "$NUMBER"); do
    python -c '';
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

# Calculate rate (iterations per second) - multiply by 1000000000 to avoid decimals
# Then divide to get the final rate
rate=$(( (NUMBER * 1000000000) / elapsed_ns ))

printf "Iterations: %'d\n" "$NUMBER"
printf "Time: %d.%06d seconds\n" "$elapsed_sec" "$elapsed_microsec"
printf "Rate: %'d iterations/second\n" "$rate"
