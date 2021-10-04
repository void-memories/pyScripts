#include <bits/stdc++.h>
using namespace std;

#define FASTIO1 ios_base::sync_with_stdio(false)
#define FASTIO2 cin.tie(NULL), cout.tie(NULL)
#define ll long long
#define pb push_back
#define mp make_pair

int gcd(int a, int b)
{
	if (b == 0)
		return a;

	else
		return gcd(b, a % b);
}

/*Function to left rotate arr[] of siz n by d*/
vector<int> leftRotate(vector<int> arr, int d, int idx, int n)
{
	/* To handle if d >= n */
	d = d % n;
	int g_c_d = gcd(d, n);
	for (int i = 0; i < g_c_d; i++)
	{
		/* move i-th values of blocks */
		int temp = arr[i];
		int j = i;

		while (1)
		{
			int k = j + d;
			if (k >= n)
				k = k - n;

			if (k == i)
				break;

			arr[j] = arr[k];
			j = k;
		}
		arr[j] = temp;
	}
	return arr;
}

vector<int> RightRotate(vector<int> a, int n, int k)
{

	// If rotation is greater
	// than size of array
	k = k % n;
	vector<int> res;
	for (int i = 0; i < n; i++)
	{
		if (i < k)
		{

			// Printing rightmost
			// kth elements
			res.push_back(a[n + i - k]);
			//cout << a[n + i - k] << " ";
		}
		else
		{

			// Prints array after
			// 'k' elements
			res.push_back(a[i - k]);
			//cout << (a[i - k]) << " ";
		}
	}
	return res;
}

void solveForTestCases()
{
	int n;
	cin >> n;
	vector<int> v(n);
	for (auto &i : v)
		cin >> i;
	int cnt = 0;
	multiset<pair<int, int>> s;
	vector<pair<int, int>> ab;
	for (int i = 0; i < n; i++)
		if (v[i] != 0)
			s.insert({v[i], i});
	while (s.size() >= 2)
	{
		auto it = s.end();
		auto p = *--it;
		int ans = p.second + 1;
		s.erase(--s.end());
		it = s.end();
		auto q = *--it;
		int res = q.second + 1;
		s.erase(--s.end());
		cnt++;

		//cout << min(res, ans) << " " << max(res, ans) << "\n";
		ab.push_back({min(res, ans), max(ans, res)});
		if (p.first - 1 != 0)
		{
			s.insert({p.first - 1, p.second});
		}
		if (q.first - 1 != 0)
		{
			s.insert({q.first - 1, q.second});
		}
	}

	cout << cnt << "\n";
	for (auto i : ab)
		cout << i.first << " " << i.second << "\n";
}

void solve()
{
	ll n, x;
	cin >> n >> x;
	ll a[n];
	for (ll i = 0; i < n; i++)
		cin >> a[i];
	sort(a, a + n);
	if (x >= a[n - 1])
	{
		cout << n << endl;
		return;
	}
	ll day = 0;
	for (ll i = 0; i < n; i++)
	{
		if (a[i] == x)
		{
			x = 2 * a[i];
			day++;
			a[i] = 0;
		}
		else if (a[i] > x)
		{
			ll aa = ceil(a[i] / 2.0);
			while (aa > x)
			{
				x *= 2;
				day++;
			}
			day += 2;
			x = a[i] * 2;
			a[i] = 0;
		}
		else if (abs(x - a[i]) < ceil(x / 2.0))
		{
			x = a[i] * 2;
			day++;
			a[i] = 0;
		}
		else
			day++;
	}
	cout << day << endl;
}

int main()
{
	FASTIO1;
	FASTIO2;

	ll t;
	cin >> t;
	while (t--)
		solve();

	return 0;
}