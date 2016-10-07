    reverse(v.begin(), v.end());
    print_vector(v); // 5 3 2 1 1
    
    random_shuffle(v.begin(), v.end());
    print_vector(v); // 1 3 1 2 5
    
    sort(v.begin(), v.end());
    print_vector(v); // 1 1 2 3 5
    
    cout << lower_bound(v.begin(), v.end(), 1) - v.begin() << endl; // 0
    cout << lower_bound(v.begin(), v.end(), 3) - v.begin() << endl; // 3
    
    do {
        print_vector(v); // See Next Slide // HL
    } while (next_permutation(v.begin(), v.end()));

    v.erase(unique(v.begin(), v.end()), v.end());
    print_vector(v); // 1 2 3 5
