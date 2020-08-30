#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
using namespace std;

int coord_x[]={-1, 0, 1, 0};
int coord_y[]={0, -1, 0, 1};
int map[1005][1005];
int check[1005][1005];
int n,m;
int solve_bfs();

int main(){
    scanf("%d%d", &n,&m);
    for(int i=1; i<=m; i++)
        for(int j=1; j<=n; j++)
            scanf("%d", &map[j][i]);

    printf("%d\n", solve_bfs());
    return 0;
}

int solve_bfs(){
    bool all_one = true;
    queue<pair<int, pair<int,int>>> qu;
    for(int i=1; i<=m; i++){
        for(int j=1; j<=n; j++){
            if(map[j][i] == 1){
                qu.push(make_pair(0, make_pair(j, i)));
                check[j][i] = 1;
                all_one = false;
            }
        }
    }
    if(all_one)
        return 0;

    int ret = -1;
    while(!qu.empty()){
        pair<int, pair<int,int>> top = qu.front();
        qu.pop();
        ret = max(ret, top.first);
        for(int i=0; i<4; i++){
            int next_x = top.second.first + coord_x[i];
            int next_y = top.second.second + coord_y[i];
            if(map[next_x][next_y] == -1 || map[next_x][next_y] == 1 ||
            next_x < 1 || next_x > n || next_y < 1 || next_y > m || check[next_x][next_y])
                continue;
            check[next_x][next_y] = 1;
            qu.push(make_pair(top.first+1, make_pair(next_x, next_y)));
        }
    }

    bool can_finish = true;
    for(int i=1; i<=m; i++)
        for(int j=1; j<=n; j++){
            if(map[j][i] == 0 && check[j][i] == 0)
                can_finish = false;
        }
    if(!can_finish)
        return -1;
    else
        return ret;
}
