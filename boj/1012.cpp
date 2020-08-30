#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int map[55][55];
int n,m,k;
int coord_x[] = {-1, 0, 1, 0};
int coord_y[] = {0, -1, 0, 1};

void dfs(int x, int y);

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        scanf("%d%d%d", &n,&m,&k);
        for(int i=1; i<=m; i++)
            for(int j=1; j<=n; j++)
                map[j][i] = 0;
        for(int i=0; i<k; i++){
            int pos_x, pos_y;
            scanf("%d%d", &pos_x, &pos_y);
            map[pos_x+1][pos_y+1] = 1;
        }
        int result = 0;
        for(int i=1; i<=m; i++)
            for(int j=1; j<=n; j++)
                if(map[j][i]){
                    result += 1;
                    map[j][i] = 0;
                    dfs(j, i);
                }
        printf("%d\n", result);
    }
    return 0;
}

void dfs(int x, int y){
    for(int coord=0; coord<4; coord++){
        int next_x = x + coord_x[coord];
        int next_y = y + coord_y[coord];
        if(map[next_x][next_y]){
            map[next_x][next_y] = 0;
            dfs(next_x, next_y);
        }
    }
}


