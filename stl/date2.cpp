#include <string.h>

int gg_days(date d) {
    int res = 0;
    date td = (date) {1, 1, 1};
    while (memcmp(&td, &d, sizeof(date)) != 0) {
        res++;
        gg_next_day(&td); // HL
    }
    return res;
}