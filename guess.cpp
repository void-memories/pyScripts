#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb push_back
#define fastIO                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);

int main()
{
    char c;
    char prev='Z';
    ll n;
    cin >> n;
    ll lo1 = 1;
    ll hi1 = n;
    ll lo2 = 1;
    ll hi2 = n;
    ll cnt = 1;
    ll f = 0;
    while (cnt <= 300)
    {

        ll mid = (lo1 + hi1) / 2;
        cout << mid << endl;
        cin >> c;

        if (prev==c || c=='E')
            {
                if (c == 'E')
            {
                f = 1;
                break;
            }
            else if (c == 'L')
            {
                hi1 = mid - 1;
            }
            else if (c == 'G')
            {
                lo1 = mid + 1;
            }}

        cnt++;
        prev=c;
    }
    if (f == 1)
    {
        exit(0);
    }
    print(0/0);
    return 0;
}

