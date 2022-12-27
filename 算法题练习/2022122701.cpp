#include <bits/stdc++.h>
using namespace std;
const int N = 20;
int st[N];
int n;

void dfs(int u) {
	if (u > n) {
		for (int i = 1; i < n; i++) {
			if (st[i] == 1) {
				cout << i << ' ';
			}
		}
		cout << endl;
		return;
	}
	st[u] = 1;
	dfs(u + 1);
	st[u] = 0;

	st[u] = 2;
	dfs(u + 1);
	st[u] = 0;
}

int main() {
	cin >> n;
	dfs(1);
	return 0;
}