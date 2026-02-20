#include <stdlib.h>
#include <stdio.h>
#include <time.h>

// Number to guess: How big of an array (in bytes) can we allocate and fill in a second?
// This is intentionally more complicated than it needs to be so that it matches the out-of-order version :)

// Bytes: 500,000,000
// Time: 2.029000 seconds
// Rate: 246,426,811 bytes/second


char* f(const long long NUMBER) {
    char* array = malloc(NUMBER);

    long long j = 1;
    for (long long i = 0; i < NUMBER; ++i) {
        j *= 2;
        j = j > NUMBER ? j - NUMBER : j;
        array[i] = j;
    }

    // so that -O2 doesn't optimize out the loop
    volatile char result = array[NUMBER / 7];

    return array;
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
    char* array = f(iterations);
    const clock_t end = clock();

    const double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    const double rate = (double)iterations / elapsed;

    printf("Bytes: %lld\n", iterations);
    printf("Time: %.6f seconds\n", elapsed);
    printf("Rate: %.0f bytes/second\n", rate);

    free(array);

    return 0;
}
