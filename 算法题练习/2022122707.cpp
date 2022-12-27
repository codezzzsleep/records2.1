#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

int main() {
	LL x, y;
	LL res;
	cin >> x >> y;
	if (y > 0) {
		if (abs(x) <= y)
			res = 3 * y + (y * y - y) / 2 * 8 + x;
		else {
			if (x > 0)
				res = 3 * x + (x * x - x) / 2 * 8 + 2 * x - y;

			else
				res = 3 * -x + (x * x + x) / 2 * 8 + 2 * x + y;
		}
	} else {
		if (y - 1 <= x && x <= -y)
			res = 7 * -y + (y * y + y) / 2 * 8 - x;
		else {
			if (x > 0)
				res = 7 * x + (x * x - x) / 2 * 8 - 2 * x - y;
			else
				res = -7 * x - 7 + (x * x + 3 * x + 2) / 2 * 8 - 2 * x + y - 1;
		}
	}
	cout << res;
	return 0;
}