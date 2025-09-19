/*
Qus: Say that you are a traveler on a 2D grid. You begin in the to-left corner
and your goal is to travel to the bottom-right corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m*n ?

write a function gridTraveler(m,n) that calculates this.

*/


#include<bits/stdc++.h>
using namespace std;


int gridTraveler(int m, int n, vector<vector<int>>&d)
{
    if(d[m][n]!=-1)
    return d[m][n];

    if(m==0 ||  n==0)
    return 0 ;

     if(m==1 &&  n==1)
    return 1 ;

    d[m][n]=gridTraveler(m-1,n,d)+gridTraveler(m,n-1,d);

    return d[m][n];

}



int main (){

    int m, n;

    cin>>m>>n;


    vector<vector<int>> d(m+5, vector<int>(n+5, -1));


    cout<<gridTraveler(m,n,d);



}