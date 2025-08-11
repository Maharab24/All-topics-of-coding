#include <bits/stdc++.h>
using namespace std;

/*........................Define..............................*/

#define optimize()                \
    ios_base::sync_with_stdio(0); \
    cin.tie(0);                   \
    cout.tie(0);
#define fraction(a)               \
    cout.unsetf(ios::floatfield); \
    cout.precision(a);            \
    cout.setf(ios::fixed, ios::floadfield);


typedef long long ll;


/*..........Debugger..........................*/
// use opi()...
template <typename F, typename S>
ostream &operator<<(ostream &os, const pair<F, S> &p)
{
    return os << "(" << p.first << ", " << p.second << ")";
}

template <typename T>
ostream &operator<<(ostream &os, const vector<T> &v)
{
    os << "{";
    for (auto it = v.begin(); it != v.end(); ++it)
    {
        if (it != v.begin())
            os << ", ";
        os << *it;
    }
    return os << "}";
}

template <typename T>
ostream &operator<<(ostream &os, const set<T> &v)
{
    os << "[";
    for (auto it = v.begin(); it != v.end(); ++it)
    {
        if (it != v.begin())
            os << ", ";
        os << *it;
    }
    return os << "]";
}

template <typename T>
ostream &operator<<(ostream &os, const multiset<T> &v)
{
    os << "[";
    for (auto it = v.begin(); it != v.end(); ++it)
    {
        if (it != v.begin())
            os << ", ";
        os << *it;
    }
    return os << "]";
}

template <typename F, typename S>
ostream &operator<<(ostream &os, const map<F, S> &v)
{
    os << "[";
    for (auto it = v.begin(); it != v.end(); ++it)
    {
        if (it != v.begin())
            os << ", ";
        os << it->first << " = " << it->second;
    }
    return os << "]";
}

#define opi(args...)            \
    do                          \
    {                           \
        cerr << #args << " : "; \
        faltu(args);            \
    } while (0)

void faltu()
{
    cerr << endl;
}

template <typename T>
void faltu(T a[], int n) // array opi(a,10) have to give size also
{
    for (int i = 0; i < n; ++i)
        cerr << a[i] << ' ';
    cerr << endl;
}

template <typename T, typename... hello>
void faltu(T arg, const hello &...rest)
{
    cerr << arg << ' ';
    faltu(rest...);
}
/*......................Debugger end.......................... */

/*..........Function section start........................*/
int sum_all_digit(int x)
{
    int add = 0;

    while (x != 0)
    {
        int r = x % 10;
        add += r;
        x = x / 10;
    }

    return add;
}

bool isPrime(int n)
{
    if (n <= 1)
        return false;

    int limit = sqrt(n + 1);
    for (int i = 2; i <= limit; i++)
    {
        if (n % i == 0)
            return false;
    }

    return true;
}
/*..........Function section end........................*/
/*.......... solve.......................*/

/*------------Note---------------*/
/*

*/

void solve()
{

    string s;
    cin>>s;

    for(int i=0 ; i<s.size();i++)
    {
        s[i] = tolower(s[i]);
    }

    string ans;

    for(int i=0 ; i<s.size(); i++)
    {
        if(s[i]=='a' || s[i]=='e' ||s[i]=='i' ||s[i]=='o' ||s[i]=='u' || s[i]=='y' )
        {
            continue;
        }
        else
        {
            ans+='.';
            ans+=s[i];
        }

    }

    cout<<ans<<endl;

}

/*...........solve end...................*/

int main()

{
    optimize();


        solve();

}