    int x = 0;
    cout << *find_if(all(v), [=](int a) { // HL
        return a < x;
    }) << endl; // -3

    cout << count_if(all(v), [=](int a) { // HL
        return a > x;
    }) << endl; // 3

    cout << accumulate(all(v), 0) << endl; // 1

    cout << accumulate(all(v), INT_MIN, [](int a, int b) { // HL
        return max(a, b);
    }) << endl; // 5

    cout << accumulate(all(v), 0, plus<int>()) << endl; // 1
    
    cout << accumulate(all(v), 0, [=](int a, int b) { // HL
        return a + (b > x);
    }) << endl; // 3