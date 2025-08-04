
//Consecutive rearrangement

// #include<bits/stdc++.h>
// using namespace std;


// bool consecutive(vector<int>a)
// {
//     sort(a.begin(),a.end());

//     for(int i=0 ; i<a.size()-1; i++)
//     {
//         if(a[i+1]!=a[i]+1)
//             return false;
//     }

//     return true;
// }

// int main()
// {
//     vector<int> a ={1, 2 ,5, 7, 4, 3, 6};

//     cout<<consecutive(a)<<endl;
// }



//Elements Smaller Than Adjacent Neighbours

// #include<bits/stdc++.h>
// using namespace std;

// vector<int> smaller ( vector<int> a)
// {

//     vector<int> res;



//         for (int i=1 ; i < a.size()-1 ; i++)
//         {
//             if(a[i]<a[i-1] && a[i]<a[i+1])
//             {
//                 res.push_back(a[i]);
//             }
//         }

//         return res;

// }


// int main()
// {
//     vector<int> a={1,2,5,0,3,1,7};


//     vector<int> b;

//     b = smaller(a);

//     for(auto u : b)
//     cout<<u<<" ";
// }


//Capitalize First Letter of Each Vector String

// #include<bits/stdc++.h>
// using namespace std;

// void test(vector<string> &a)
// {
//     for(int i=0 ;  i< a.size(); i++)
//     {
//         string s = a[i];

//         s[0]=toupper(s[0]);

//         a[i]=s;


//     }

// }

// int main(){

//   vector<string> a = {"red", "green", "black", "white", "Pink"};


//   test(a);

//   for(auto u : a)
//   cout<<u<<endl;



// }


//Verify letters of second string in first string

#include<bits/stdc++.h>
using namespace std;


int main (){

    
}
