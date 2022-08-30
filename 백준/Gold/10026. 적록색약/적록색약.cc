#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int n;
int cnt = 0;
string board[102];
queue<pair<int, int> > Q;
bool vis[102][102];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int bfs(int i, int j){
    if(vis[i][j]) return 0;
    Q.push({i,j});
    vis[i][j] = 1;

    while(!Q.empty()){
        auto cur = Q.front();
        Q.pop();

        for(int dir = 0; dir < 4; dir++){
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];
            int tmpx = cur.X;
            int tmpy = cur.Y;

            if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
            if(vis[nx][ny]) continue;
            if(board[nx][ny] != board[tmpx][tmpy]) continue;
            vis[nx][ny] = 1;
            Q.push({nx,ny});
        }
    }
    return 1;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for(int i = 0; i < n; i++) cin >> board[i];

    int cnt = 0;
    // 적녹색약x
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            int k = bfs(i,j);
            if(k == 1) cnt++;
        }
    }
    cout << cnt << '\n';

    // 적녹색약
    cnt = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            vis[i][j] = 0;
            if(board[i][j] == 'G') board[i][j] = 'R';
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            int k = bfs(i,j);
            if(k == 1) cnt++;
        }
    }    
    cout << cnt << '\n';

}
