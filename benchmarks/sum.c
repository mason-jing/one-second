#include <stdlib.h>
#include <stdio.h>
#include <time.h>

// Number to guess: How many iterations of this loop can we go through in a second?

// Iterations: 10,000,000,000
// Time: 3.403000 seconds
// Rate: 2,938,583,603 iterations/second


void f(const long long NUMBER) {
    long long i;
    for (long long s = i = 0; i < NUMBER; ++i) {
        s += 1;
    }
}

int main(int argc, char** argv) {
    char* endptr;
    errno = 0;
    const long long iterations = strtoll(argv[1], &endptr, 10);

    // Check for conversion errors
    if (errno != 0 || *endptr != '\0' || endptr == argv[1]) {
        fprintf(stderr, "Error: Invalid number '%s'\n", argv[1]);
        return 1;
    }

    const clock_t start = clock();
    f(iterations);
    const clock_t end = clock();

    const double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    const double rate = (double)iterations / elapsed;

    printf("Iterations: %lld\n", iterations);
    printf("Time: %.6f seconds\n", elapsed);
    printf("Rate: %.0f iterations/second\n", rate);

    return 0;
}
