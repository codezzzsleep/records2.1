#include <bits/stdc++.h>
using namespace std;
const int  N = 5e5 + 10;
char str[N];
int l[N], r[N];

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> str[i];
	}
	for (int i = 0, g = 0, h = 0; i < n; i++) {
		if (str[i] == 'G')
			l[i] = h, h = 0, g++;
		else
			l[i] = g, g = 0, h++;
	}
	for (int i = n - 1, h = 0, g = 0; i >= 0; i--) {
		if (str[i] == 'G')
			r[i] = h, h = 0, g++;
		else
			r[i] = g, g = 0, h++;
	}
	long long  res = 0;
	for (int i = 0; i < n; i++) {
		res += (long long)r[i] * l[i] + max(r[i] - 1, 0) + max(l[i] - 1, 0);
	}
	cout << res << endl;
	return 0;
}