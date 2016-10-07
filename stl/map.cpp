#include <map>
#include <iostream>
using namespace std;

int main() {
    map<int, int> m;
    m[0] = 1;
    m[1] = 1;
    m[10] = 2;
    m[11] = 3;
    cout << m.size() << endl; // 4
    cout << m.count(1) << endl; // 1
    cout << m.count(2) << endl; // 0
    m.erase(1);
    cout << m.count(1) << endl; // 0

    for (auto p : m) {
        cout << p.first << ": " << p.second << endl; // 0: 1
                                                     // 10: 2
                                                     // 11: 3
    }
    return 0;
}
