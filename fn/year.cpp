def year_info(y):
    print y
    for i in range(4):
        res0 = fill_table(y, i * 3 + 1) // HL
        res1 = fill_table(y, i * 3 + 2) // HL
        res2 = fill_table(y, i * 3 + 3) // HL
        for j in range(MONTH_HEIGHT):
            print res0[j], res1[j], res2[j]
