#include <bits/stdc++.h>
using namespace std;

#define all(x) x.begin(), x.end() // HL

void print_vector(vector<int> v) {
    for (int a : v) {
        cout << a << " ";
    }
    cout << endl;
}

int main() {
    vector<int> v{2, -3, 1, 5, -4};
    sort(all(v), greater<int>()); // HL
    print_vector(v); // 5 2 1 -3 -4
    sort(all(v), [](int a, int b) {  // HL
        return abs(a) < abs(b);
    });
    print_vector(v); // 1 2 -3 -4 5
    // ... See next slide // HL
    return 0;
}
