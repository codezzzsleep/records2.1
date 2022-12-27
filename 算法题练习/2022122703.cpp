#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	int a = 0, b = 1;
	if (n >= 1)
		cout << a << ' ';
	if (n >= 2)
		cout << b << ' ';
	for (int i = 3; i <= n; i++) {
		cout << a + b << ' ';
		int t = a;
		a = b;
		b = t + a;
	}
	return 0;
}