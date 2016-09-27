#include <stdio.h>

int main() {
    int a[3] = {2016, 9, 27};
    printf("%d %d %d\n", a[0], a[1], a[2]); // 2016 9 27
    a[2] = 29;
    printf("%d %d %d\n", a[0], a[1], a[2]); // 2016 10 29

    // Long Array // HL
    int la[100] = {2016};
    printf("%d %d\n", la[0], la[1]); // 2016 0
    return 0;
}
