#include <bits/stdc++.h>
using namespace std;
const int N = 10;
int st[N];
bool used[N];
int n, m;

void dfs(int u) {
	if (u > n) {
		for (int i = 1; i <= n; i++) {
			cout << st[i] << ' ';
		}
		cout << endl;
		return;
	}
	for (int i = 1; i <= n; i++) {
		if (!used[u]) {
			st[i] = u;
			used[u] = true;
			dfs(u + 1);
			st[i] = 0;
			used[u] = false;
		}
	}
}

int main() {
	cin >> n >> m;
	dfs(1);
	return 0;
}