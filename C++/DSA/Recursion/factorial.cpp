#include <bits/stdc++.h>
using namespace std;

long long fact(int n) {
    if(n == 0 || n == 1) return 1;   // base case
    return n * fact(n - 1);          // recursion
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;

    cout << "Factorial of " << n << " = " << fact(n);
}
