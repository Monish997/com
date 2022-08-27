#include <bits/stdc++.h>
using namespace std;

void ReplaceStringInPlace(string &subject, const string &search,
                          const string &replace)
{
    size_t pos = 0;
    while ((pos = subject.find(search, pos)) != string::npos)
    {
        subject.replace(pos, search.length(), replace);
        pos += replace.length();
    }
}

string solve()
{
    map<string, string> maps = {
        {"01", "2"},
        {"12", "3"},
        {"23", "4"},
        {"34", "5"},
        {"45", "6"},
        {"56", "7"},
        {"67", "8"},
        {"78", "9"},
        {"89", "0"},
        {"90", "1"},
    };
    int n;
    string s;
    cin >> n;
    cin >> s;
    string prev_str = "";
    while (prev_str != s)
    {
        prev_str = s;
        for (auto &it : maps)
        {
            string key = it.first;
            string value = it.second;
            ReplaceStringInPlace(s, key, value);
        }
    }
    return s;
}

int main()
{
    ifstream cin("input_substitutions.txt");
    ios_base::sync_with_stdio(false);
    std::cin.tie(0);
    std::cin.rdbuf(cin.rdbuf());

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        string r = solve();
        cout << "Case #" << i + 1 << ": " << r << "\n";
    }
    return 0;
}