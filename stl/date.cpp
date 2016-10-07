typedef struct {
    int year;
    int month;
    int day;
} date;

date gg2st(date gg) {
    int days = gg_days(gg); // HL
    date st = (date) {1, 1, 1};
    for (int i = 0; i < days; i++) {
        st_next_day(&st); // HL
    }
    return st;
}
