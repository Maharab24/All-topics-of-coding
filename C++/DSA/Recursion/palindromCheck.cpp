
#include <bits/stdc++.h>
using namespace std;

bool isPalindromeUtil(string& s, int left, int right) {

    // Base case
    if (left >= right)
        return true;


    if (s[left] != s[right])
        return false;


    return isPalindromeUtil(s, left + 1, right - 1);
}


bool isPalindrome(string s){
    int left = 0, right = s.length() - 1;
    return isPalindromeUtil(s, left, right);
}

int main() {
    string s = "abba";
    if (isPalindrome(s)) {
        cout << "Yes" << endl;
    }
    else {
        cout << "No" << endl;
    }

    return 0;
}