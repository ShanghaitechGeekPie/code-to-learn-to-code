int gg_last_day(date *d) ;
void gg_next_month(date *d) ;

void gg_next_day(date *d) {
    if (d->day == gg_last_day(d)) {
        gg_next_month(d);
        d->day = 1;
    } else {
        d->day++;
    }
}

void st_next_day(date *d) ;
