#include <iostream>
#include <algorithm>
#include <vector>
#include <memory.h>
#include <queue>

using namespace std;

int v[1001];
string name[1001];
queue<int> score[1001];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    string trash;
    int n; cin >> n; getline(cin, trash);
    for(int i=1; i<=n; i++){
        getline(cin, name[i]);
    }
    int a, cnt=1;
    while(cin >> a){
        score[cnt].push(a);
        for(int i=1; i<n; i++){
            int b; cin >> b;
            score[cnt].push(b);
        }
        cnt++;
    }
    cnt--;
    while(1){
        for(int i=1; i<=cnt; i++){
            while(v[score[i].front()]==-1){
                score[i].pop();
            }
            v[score[i].front()]++;
        }
        int mx=0, mn=9999999;
        for(int i=1; i<=n; i++){
            mx=max(mx, v[i]);
            if(v[i]!=-1){ mn=min(mn, v[i]); }
        }

        if(mx*2>cnt || mx==mn){
            for(int i=1; i<=n; i++){
                if(v[i]==mx){
                    cout << name[i] << "\n";
                }
            }
            return 0;
        }
        for(int i=1; i<=n; i++){
            if(v[i]==mn){ v[i]=-1; }
            else if(v[i]!=-1){ v[i]=0; }
        }
    }
    return 0;
}