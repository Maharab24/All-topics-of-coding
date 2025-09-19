#include <bits/stdc++.h>
using namespace std;

int fib(int n, vector<int> &d)
/*
    if i use just vector<int> d , then the code run very slowly.
    If I use vector<int>&d, then the code run very fast. Because

d is passed by value, not by reference.
That means a copy of the vector is created every time fib() is called.
So your memoization array is not actually shared between recursive calls — it resets each time.
*/

{

    if (d[n] != -1)
        return d[n];
    if (n <= 2)
        return 1;

    d[n] = fib(n - 1, d) + fib(n - 2, d);

    return d[n];
}

int main()
{
    int n;
    cin >> n;

    vector<int> d(n + 1, -1); // insert -1 in all index.

    cout << fib(n, d);
}