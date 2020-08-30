#include <stdio.h>
#include <queue>
#include <algorithm>
#include <string.h>
using namespace std;

int map[105][105];
int coord_x[] = {-1, 0, 1, 0};
int coord_y[] = {0, -1, 0, 1};
int n,m;

int solve_bfs();

int main(){
    scanf("%d %d", &n,&m);
    char temp[105];
    for(int i=1; i<=n; i++){
        scanf("%s", temp);
        for(int j=0; j<strlen(temp); j++){
            if(temp[j] == '1')
                map[j+1][i] = 1;
        }
    }
    printf("%d\n", solve_bfs());
    return 0;
}

int solve_bfs(){
    queue<pair<int, pair<int,int>>> qu;
    pair<int,int> start = make_pair(1, 1);
    qu.push(make_pair(1, start));
    map[1][1] = 0;

    while(!qu.empty()){
        pair<int, pair<int,int>> top = qu.front();
        qu.pop();
        if(top.second.first == m && top.second.second == n)
            return top.first;
        for(int i=0; i<4; i++){
            int next_x = top.second.first + coord_x[i];
            int next_y = top.second.second + coord_y[i];
            if(map[next_x][next_y]){
                map[next_x][next_y] = 0;
                qu.push(make_pair(top.first+1, make_pair(next_x, next_y)));
            }
        }
    }
}
