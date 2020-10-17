#include<bits/stdc++.h>
using namespace std;
typedef long long ll; 
#define pb push_back
#define io ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL); 
#define all(s) s.begin(),s.end()
#define rep(i, a, b) for(ll i = a; i < b; i++)
#define _max(v) *max_element(v.begin(), v.end())
#define _min(v) *min_element(v.begin(), v.end())
#define ms(s, n) memset(s, n, sizeof(s))
ll raised(ll x,  ll y){ll res = 1;while (y > 0){ if (y & 1){res = res*x;} y = y>>1;x = x*x;}return res;}
ll raisedmod(ll x, ll y, ll p){int res = 1;x = x % p;while (y > 0){if (y & 1){res = (res*x) % p;}y = y>>1; x = (x*x) % p;}return res;}
ll gcd(ll a, ll b) { if (b == 0)return a; return gcd(b, a % b);} 
ll fact(ll n){ll res = 1; for (ll i = 2; i <= n; i++) res = res * i; return res; } 
ll nCr(ll n, ll r){ return fact(n) / (fact(r) * fact(n - r));} 


int main() 
{
    io;
    ll t; cin >> t;
    //t=1;
    while(t--)
    {
       ll n, k, l, f=0; cin >> n >> k>> l;
        vector<ll> v;
        rep(i, 1, n+1) { if(i%k!=0)v.pb(i%k); else v.pb(k);}
       rep(i, 0, v.size()-1) {if(v[i]==v[i+1]) f=1;}
       if(f==1 || k*l<n) cout<< -1;
       else {rep(i, 0, v.size()) cout<< v[i]<< " ";}
       cout<< endl;
    }
	return 0;
}