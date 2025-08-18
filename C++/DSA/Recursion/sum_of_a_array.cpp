#include<bits/stdc++.h>
using namespace std;

int sumOfArray(vector<int> a,int n)
{
    if(n==0)
        return 0;

    return a[n-1]+sumOfArray(a,n-1);

}

int main()
{
    vector<int> a = {1,2,3};

    cout<<sumOfArray(a,a.size());
}