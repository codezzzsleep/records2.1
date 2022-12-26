#include <bits/stdc++.h>
using namespace std;
const int N = 10;
int st[N];
bool used[N];
int n, m;

void dfs(int u) {
	if (u > m) {
		for (int i = 1; i <= m; ++i) {
			cout << st[i] << ' ';
		}
		cout << endl;
		return;
	}
	for (int i = 1; i <= n; ++i) {
		if (!used[i]) {
//			if (st[u - 1] > i)
//				return;
			st[u] = i;
			used[i] = true;
			dfs(u + 1);
			st[u] = 0;
			used[i] = false;
		}
	}

}

int main() {
	cin >> n >> m;
	dfs(1);
	return 0;
}