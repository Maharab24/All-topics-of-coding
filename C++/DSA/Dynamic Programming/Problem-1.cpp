//https://cses.fi/problemset/task/1633

#include<bits/stdc++.h>
using namespace std;

#define mod 1000000007

int n ,vis[1000005],dp[1000005];

int solve(int sum)
{

    if(sum==0)
        return 1;

    if(vis[sum]==1)
        return dp[sum];

    int res=0 ;

    for(int j=1; j<=6; j++)
    {
        if(sum>=j)
       res+= solve(sum-j);

       res%=mod;
    }

    vis[sum]=1;
    dp[sum]=res;



    return res;
}

int main()
{
    cin>>n;

    cout<<solve(n);
    return 0 ;
}