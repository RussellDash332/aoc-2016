#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    vector<vector<int>> v;
    int a, b, c, possible = 0, possible2 = 0;
    while (cin >> a >> b >> c) {
        v.push_back({a, b, c});
        if (a + b + c > 2 * max(max(a, b), c)) {
            possible++;
        }
    }

    for (int i = 0; i < (int) v.size(); i += 3) {
        for (int j = 0; j < 3; j++) {
            if (v[i][j] + v[i + 1][j] + v[i + 2][j] > 2 * max(max(v[i][j], v[i + 1][j]), v[i + 2][j])) {
                possible2++;
            }
        }
    }

    cout << "Part 1: " << possible << endl;
    cout << "Part 2: " << possible2 << endl;

    return 0;
}