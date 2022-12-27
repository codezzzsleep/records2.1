#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
int a[N], b[N], c[N];

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	for (int i = 0; i < n; i++)
		scanf("%d", &b[i]);
	for (int i = 0; i < n; i++)
		scanf("%d", &c[i]);
	sort(a, a + n);
	sort(b, b + n);
	sort(c, c + n);
	long long res = 0;
	for (int i = 0; i < n; i++) {
		int x = lower_bound(a, a + n, b[i]) - a;
		int y = upper_bound(c, c + n, b[i]) - c;
		res += x * y;
	}
	cout << res << endl;
	return 0;
}