#include <bits/stdc++.h>
using namespace std;
const int N = 20;
int n;
bool flag[N];

void dfs(int u) {
	if (u > n) {
		for (int i = 1; i <= n; i++) {
			if (flag[i]) {
				cout << i << ' ';
			}
		}
		cout << endl;
		return;
	}
	flag[u] = true;
	dfs(u + 1);
	flag[u] = false;

	flag[u] = false;
	dfs(u + 1);
	flag[u] = false;
}

int main() {
	cin >> n;
	dfs(1);
	return 0;
}