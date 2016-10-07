#include <vector> // HL
#include <iostream>
using namespace std;

int main() {
    vector<int> v(10, 1); // HL
    for (int i = 2; i < v.size(); i++) {
        v[i] = v[i - 1] + v[i - 2];
    }
    v.push_back(0);
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " "; // 1 1 2 3 5 8 13 21 34 55 0
    }
    return 0;
}
