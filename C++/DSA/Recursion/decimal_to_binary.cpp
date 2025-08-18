#include<bits/stdc++.h>
using namespace std;

/**

10 % 2 = 0, continue with 10 / 2 = 5
5 % 2 = 1, continue with 5 / 2 = 2
2 % 2 = 0, continue with 2 / 2 = 1
1 % 2 = 1, stop as 1 / 2 = 0


 */

 void makeTheResult(int d, string &ans)
 {
   if(d>1)
      makeTheResult(d/2,ans);

   ans+=(d%2) + '0';


 }

 string decimalToBinary(int d)
 {
      string ans="";
      makeTheResult(d,ans);

      return ans;


 }



 int main()
 {
    int dec;
    cin>>dec;

    cout<<decimalToBinary(dec);


 }