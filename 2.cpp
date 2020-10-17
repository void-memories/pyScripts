#include <bits/stdc++.h>
using namespace std;
long long rbc, wbc;
int main()
{
    long long t;
    scanf("%lld", &t);

    while (t--)
    {

        long long n, x, day = 0, cur;
        scanf("%lld%lld", &n, &x);

        vector<long long> a(n);
        for (long long i = 0; i < n; i++)
            scanf("%lld", &a[i]);

        sort(a.begin(), a.end());
        if (x >= a[n - 1])
        {
            day = n;
        }
        else
        {

            for (long long i = 0; i < n; i++)
            {

                if (a[i] == x)
                {
                    x = 2 * a[i];

                    day++;

                    a[i] = 0;
                }
                else if (a[i] > x)
                {
                    cur = ceil(a[i] / 2.0);

                    while (cur > x)
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
                {

                    day++;
                }
            }
        }

        printf("%lld\n", day);
    }
    return 0;
}