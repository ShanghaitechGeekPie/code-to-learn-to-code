def month_info(y, m):
    print y
    res = fill_table(y, m) // HL
    for i in range(MONTH_HEIGHT):
        print res[i]
