#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, k;
	int res = 0;
	cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		int x = i;
		while (x != 0) {
			if (x % 10 == k)
				res++;
			x /= 10;
		}
	}
	return 0;
}