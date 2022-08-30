#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
#define X first
#define Y second
#define Z third

int box[103][103][103];
int dist[103][103][103];
int n,m,h;
int dx[6] = {0,0,1,-1,0,0};
int dy[6] = {1,-1,0,0,0,0};
int dz[6] = {0,0,0,0,1,-1};

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> m >> n >> h;
    queue<tuple<int,int,int>> Q;

    for(int i = 0; i < h; i++){
        for(int j = 0; j < n; j++){
            for(int k = 0; k < m; k++){
                int tmp;
                cin >> tmp;
                box[j][k][i] = tmp;
                if(tmp == 1) Q.push({j,k,i});
                if(tmp == 0) dist[j][k][i] = -1;
            }
        }
    }

    while(!Q.empty()){
        auto cur = Q.front();
        Q.pop();

        int curx,cury,curz;
        tie(curx,cury,curz) = cur;

        for(int dir = 0; dir < 6; dir++){
            int nx = curx + dx[dir];
            int ny = cury + dy[dir];
            int nz = curz + dz[dir];

            if(nx < 0 || nx >= n || ny < 0 || ny >= m || nz < 0 || nz >= h) continue;
            if(dist[nx][ny][nz] >= 0) continue;

            dist[nx][ny][nz] = dist[curx][cury][curz]+1;
            Q.push({nx,ny,nz});
        }
    }

    int ans = 0;
    for(int i = 0; i < h; i++){
        for(int j = 0; j < n; j++){
            for(int k = 0; k < m; k++){
                if(dist[j][k][i] == -1){
                    cout << -1;
                    return 0;
                }
                ans = max(ans,dist[j][k][i]);
            }
        }
    }
    cout << ans;
}

