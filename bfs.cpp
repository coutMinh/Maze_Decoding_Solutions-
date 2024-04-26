#include<iostream>
#include<queue>
#include<vector>
#include<stdio.h>
using namespace std;

//Cho luoi o vuong voi cac duong di duoc va khong di duoc
//Ap dung bfs dfs
//nxn -> (2n+1)x(2n+1)
int n, m, s, t, u, v;
char a[1001][1001];
bool visited[1001][1001];
int d[1001][1001];//Mang luu so luong buoc di tu o bat dau den o i, j
int dx[] = { -1,0,0,1 };
int dy[] = { 0,-1,1,0 };
pair<int, int> parent[1001][1001];
void bfs(int i, int j) {
	queue<pair<int, int>> q;
	q.push({ i, j });
	a[i][j] = 'x';
	d[i][j] = 0;
	cout << i << " " << j << endl;
	while (!q.empty()) {
		pair<int, int> top = q.front();
		q.pop();
		//Duyet cac dinh ke
		for (int k = 0; k < 4; k++) {
			int i1 = top.first + dx[k];
			int j1 = top.second + dy[k];
			if (i1 >= 1 && i1 <= n && j1 >= 1 && j1 <= m && a[i1][j1] != 'x') {
				cout << i1 << " " << j1 << endl;
				d[i1][j1] = d[top.first][top.second] + 1;
				parent[i1][j1] = { top.first, top.second };
				if (a[i1][j1] == 'B')  return;
				q.push({ i1, j1 });
				a[i1][j1] = 'x';
			}
		}
	}
}
void Truyvet() {
	int i = u;
	int j = v;
	pair<int, int> temp;
	vector<pair<int, int>> ans;
	while (i != s || j != t) {
		ans.push_back({ i, j });
		temp = parent[i][j];
		i = temp.first;
		j = temp.second;
	}
	ans.push_back({ s, t });
	for (auto v: ans) {
		printf("(%d, %d)\n", v.first, v.second);
	}
}
void input() {
	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cin >> a[i][j];
			if (a[i][j] == 'A') {
				s = i;
				t = j;
			}
			else if (a[i][j] == 'B') {
				u = i;
				v = j;
			}
		}
	}
	//Co the xay dung dfs bang cach tim toa do diem B sau do check xem dfs da loan den B hay chua

	memset(visited, false, sizeof(visited));
	bfs(s, t);
	if (!d[u][v]) {
		cout << "Khong co duong di tu A den B\n";
	}
	else cout << d[u][v] << endl;
	Truyvet();
}
int main() {
	input();
}
//6 6
//xxxooo
//ooxooo
//oxxxxo
//ooooox
//xxoxox
//xoxxox
//6 6
//Aooxoo
//oxoooo
//oxoooo
//ooooxx
//xooooo
//oooxxB
//6 6
//Aooxoo
//oxoooo
//oxoooo
//ooooxx
//Boooxo
//oooxxx

