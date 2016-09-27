#include <stdio.h>

struct Date {
    int year;
    int month;
    int day;
};

int main() {
    struct Date a = {2016, 9, 27};
    printf("%d %d %d\n", a.year, a.month, a.day); // 2016 9 27
    struct Date b = a;
    b.day = 29;
    printf("%d %d %d\n", b.year, b.month, b.day); // 2016 9 29
    return 0;
}
