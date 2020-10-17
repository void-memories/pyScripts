#include <bits/stdc++.h>
using namespace std;
#define ll long long int

int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);

	ll t,n,s,u,d,l,r;
	ch

	cin>>t;
	while(t--){
		u=d=l=r=0;
		cin>>n;
		for(ll i=0;i<n;i++){
			cin>>temp;
			if(temp=='U')
			u++;
			else if (temp=='D')
			d++;
			else if (temp=='L')
			l++;
			else if (temp=='R')
			r++;
		}

		cout<<min(u,d)+min(l,r)<<endl;
	}
	return 0;

}