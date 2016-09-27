#include <stdio.h>

typedef struct {
    int year;
    int month;
    int day;
} Date; // HL

int main() {
    Date a = {2016, 9, 27}; // HL
    printf("%d %d %d\n", a.year, a.month, a.day); // 2016 9 27
    Date b = a; // HL
    b.day = 29;
    printf("%d %d %d\n", b.year, b.month, b.day); // 2016 9 29
    return 0;
}
