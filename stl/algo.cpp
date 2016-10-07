#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

void print_vector(vector<int> v) {
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;
}

int main() {
    unsigned n = 5;
    vector<int> v(n, 1);
    for (int i = 2; i < n; i++) {
        v[i] = v[i - 1] + v[i - 2];
    }
    print_vector(v); // 1 1 2 3 5
    // ... See Next Slide // HL
    return 0;
}
