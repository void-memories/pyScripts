#include<bits/stdc++.h>
using namespace std;

#define FASTIO1 ios_base::sync_with_stdio(false)
#define FASTIO2 cin.tie(NULL),cout.tie(NULL)
#define ll long long
#define pb push_back
#define mp make_pair

void solve()
{
	ll n,x;
	cin>>n>>x;
	ll a[n];
	for(ll i=0;i<n;i++)
		cin>>a[i];
	sort(a,a+n);
	if(x>=a[n-1])
	{
		cout<<n<<endl;
		return;
	}
	ll day=0;
	for(ll i=0;i<n;i++)
	{
		if(a[i]==x)
		{
			x=2*a[i];
			day++;
			a[i]=0;
		}
		else if(a[i]>x)
		{
			ll aa=ceil(a[i]/2.0);
			while(aa>x)
			{
				x*=2;
				day++;
			}
			day+=2;
			x=a[i]*2;
			a[i]=0;
		}
		else if(abs(x-a[i])<ceil(x/2.0))
		{
			x=a[i]*2;
			day++;
			a[i]=0;
		}
		else
			day++;
	}
	cout<<day<<endl;
}

int main() 
{
    FASTIO1;
    FASTIO2;

    ll t;
    cin>>t;
    while(t--)
        solve();
    
    return 0;
}