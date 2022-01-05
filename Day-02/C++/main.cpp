#include <bits/stdc++.h>
#include <string>
#include <map>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    map<int, string> d;
    d.insert(pair<int, string>(2, "1"));
    d.insert(pair<int, string>(11, "2"));
    d.insert(pair<int, string>(12, "3"));
    d.insert(pair<int, string>(13, "4"));
    d.insert(pair<int, string>(20, "5"));
    d.insert(pair<int, string>(21, "6"));
    d.insert(pair<int, string>(22, "7"));
    d.insert(pair<int, string>(23, "8"));
    d.insert(pair<int, string>(24, "9"));
    d.insert(pair<int, string>(31, "A"));
    d.insert(pair<int, string>(32, "B"));
    d.insert(pair<int, string>(33, "C"));
    d.insert(pair<int, string>(42, "D"));

    string line, s = "", t = "";
    while (cin >> line) {
        int r1 = 1, c1 = 1, r2 = 2, c2 = 0;
        for (int i = 0; i < line.length(); i++) {
            if (line[i] == 'U') {
                r1 = max(0, r1 - 1);
                if (r2 != abs(c2 - 2)) {
                    r2 -= 1;
                }
            } else if (line[i] == 'D') {
                r1 = min(2, r1 + 1);
                if (r2 != 4 - abs(c2 - 2)) {
                    r2 += 1;
                }
            } else if (line[i] == 'L') {
                c1 = max(0, c1 - 1);
                if (c2 != abs(r2 - 2)) {
                    c2 -= 1;
                }
            } else {
                c1 = min(2, c1 + 1);
                if (c2 != 4 - abs(r2 - 2)) {
                    c2 += 1;
                }
            }
        }
        s += to_string(3 * r1 + c1 + 1);
        t += d[10 * r2 + c2];
    }

    cout << "Part 1: " << s << endl;
    cout << "Part 2: " << t << endl;

    return 0;
}