#include <bits/stdc++.h>
using namespace std;

bool canSum(int n, vector<int> &a, vector<int> &dp)
{
    if (n == 0) return true;
    if (n < 0) return false;

   
    if (dp[n] != -1) return dp[n];

    for (int i = 0; i < a.size(); i++)
    {
        if (canSum(n - a[i], a, dp))
        {
            dp[n] = true;
            return true;
        }
    }

    dp[n] = false;
    return false;
}

int main()
{
    int n;
    cin >> n;

    int size;
    cin >> size;

    vector<int> a(size);
    for (int i = 0; i < size; i++)
        cin >> a[i];

    vector<int> dp(n + 1, -1); // memo array indexed by n

    cout << (canSum(n, a, dp) ? "True" : "False");
}
