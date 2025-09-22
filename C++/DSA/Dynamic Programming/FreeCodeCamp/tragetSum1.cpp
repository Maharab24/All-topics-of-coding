#include<bits/stdc++.h>
using namespace std;

bool canSum(int n, vector<int>&a,vector<int>&dp)
{


    for(int i=0 ; i<=dp.size(); i++)
    {
        if(dp[i]==n)
        return dp[n];
    }

    if(n==0) return true;
    if(n<0) return false;

    for(int i=0 ; i < a.size(); i++)
    {
        if(canSum(n-a[i],a,dp)==true)
        {
            dp[n]=true;
            return true;
        }

    }

    dp[n]=false;
    return false; 




}




int main(){

    int n ;
    cin>>n;

    int size;
    cin>>size;

    vector<int>a(size);
    vector<int>dp(size+3);

    for(int i=0 ; i< size ; i++)
    {
        cin>>a[i];
    }

    cout<<canSum(n,a,dp);

}
