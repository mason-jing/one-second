#include <stdio.h>

int main() {
#ifdef __STDC_VERSION__
    printf("C Standard Version: %ld\n", __STDC_VERSION__);

    #if __STDC_VERSION__ >= 202311L
        printf("C23 is supported!\n");
    #elif __STDC_VERSION__ >= 201710L
        printf("C17 is supported (C23 not supported)\n");
    #elif __STDC_VERSION__ >= 201112L
        printf("C11 is supported (C23 not supported)\n");
    #elif __STDC_VERSION__ >= 199901L
        printf("C99 is supported (C23 not supported)\n");
    #else
        printf("Older C standard (C23 not supported)\n");
    #endif
#else
    printf("C89/C90 (C23 not supported)\n");
#endif

    return 0;
}
