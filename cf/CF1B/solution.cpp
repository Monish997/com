#include <bits/stdc++.h>
using namespace std;

#define read(dtype, var) \
    dtype var;           \
    cin >> var

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;

int main() {
    freopen("./input.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    read(int, t);
    while (t--) {
        read(string, s);
        if (s[0] == 'R' && isdigit(s[1]) && s.find('C') != string::npos) {
            string row = s.substr(1, s.find('C') - 1);
            int col = stoi(s.substr(s.find('C') + 1));
            string colstr = "";
            while (col) {
                int rem = col % 26;
                if (rem) {
                    colstr = (char)(rem + 'A' - 1) + colstr;
                } else {
                    colstr = 'Z' + colstr;
                    col -= 26;
                }
                col /= 26;
            }
            cout << colstr << row << endl;
        } else {
            int i = s.find_first_of("123456789");
            string colstr = s.substr(0, i);
            string row = s.substr(i);
            int col = 0;
            for (int j = 0; j < colstr.length(); j++) {
                col += (colstr[j] - 'A' + 1) * pow(26, colstr.length() - j - 1);
            }
            cout << "R" << row << "C" << col << endl;
        }
    }
}
