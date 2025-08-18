#include<bits/stdc++.h>
using namespace std;

void reverseString(string s, int n,string &ans)
{
    if(n==0)
    return ;

    ans+=s[n-1];

    reverseString(s,n-1,ans);

}


int main()
{
    string s = "Maharab Hossain Opi";

    string ans;

    reverseString(s,s.size(),ans);
    cout<<ans;

}