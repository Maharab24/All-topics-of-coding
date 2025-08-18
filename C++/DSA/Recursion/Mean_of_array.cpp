#include<bits/stdc++.h>
using namespace std;

int sumOfArray(vector<int> a , int n)
{
    if(n==0 )
    return 0 ;

    
}

float meanOfArray(vector<int> a)
{
    int n = a.size();


}

int main(){

    int n;
    cin>>n;

    vector<int> a(n);


    for(int i=0 ; i< n; i++)
    {
        cin>>a[i];
    }

    float mean= meanOfArray(a);

    cout<<mean;

}