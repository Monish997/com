#include <bits/stdc++.h>
using namespace std;

class Solution {
   public:
    int minSetSize(vector<int>& arr) {
        set<int> s(arr.begin(), arr.end());
        int r = ceil((double)arr.size() / 2);
        if (s.size() == arr.size()) {
            return r;
        }
        vector<int> counts;
        for (auto x : s) {
            counts.push_back(count(arr.begin(), arr.end(), x));
        }
        sort(counts.begin(), counts.end(), greater<int>());
        int e = 0, n = 0;
        while (e < r) {
            e += counts[n++];
        }
        return n;
    }
};

int main() {
    Solution s;
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    cout << s.minSetSize(arr) << endl;
    return 0;
}