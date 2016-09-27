#include <stdio.h>

void swap(int *a, int *b) { // HL
    int t = *a;
    *a = *b;
    *b = t;
}

int main() {
    int a = 1;
    int b = 2;
    swap(&a, &b); // HL
    printf("%d %d\n", a, b); // 2 1 // HL
    return 0;
}
