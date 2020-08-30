#include <stdio.h>
#include <algorithm>
#include <queue>
using namespace std;

int map[105][105][105];
int check[105][105][105];
int n,m,h;
int coord_x[]={-1, 0, 1, 0, 0, 0};
int coord_y[]={0, -1, 0, 1, 0, 0};
int coord_z[]={0, 0, 0, 0, -1, 1};
struct qu_input{
    int pos_x;
    int pos_y;
    int pos_h;
    int step;
}qu_input;

int solve_bfs();

int main(){
    scanf("%d%d%d", &n,&m,&h);
    for(int i=1; i<=h; i++)
        for(int j=1; j<=m; j++)
            for(int k=1; k<=n; k++)
                scanf("%d", &map[k][j][i]);

    printf("%d\n", solve_bfs());
    return 0;
}

int solve_bfs(){
    int ret = -1;
    bool all_zero = true;
    queue<struct qu_input> qu;
    for(int i=1; i<=h; i++)
        for(int j=1; j<=m; j++)
            for(int k=1; k<=n; k++){
                if(map[k][j][i] == 1){
                    check[k][j][i] = 1;
                    struct qu_input input;
                    input.pos_h = i; input.pos_y = j; input.pos_x = k;
                    input.step = 0;
                    qu.push(input);
                    all_zero = false;
                }
            }
    if(all_zero)
        return 0;
    while(!qu.empty()){
        struct qu_input top = qu.front();
        qu.pop();
        ret = max(ret, top.step);
        for(int i=0; i<6; i++){
            int next_h = top.pos_h + coord_z[i];
            int next_y = top.pos_y + coord_y[i];
            int next_x = top.pos_x + coord_x[i];
            if(next_h > h || next_h < 1 || next_y > m || next_y < 1 || next_x > n || next_x < 1
            || check[next_x][next_y][next_h] || map[next_x][next_y][next_h] == -1)
                continue;
            struct qu_input next_st;
            next_st.pos_h = next_h; next_st.pos_y = next_y; next_st.pos_x = next_x;
            next_st.step = top.step + 1;
            check[next_x][next_y][next_h] = 1;
            qu.push(next_st);
        }
    }

    bool can_finish = true;
    for(int i=1; i<=h; i++)
        for(int j=1; j<=m; j++)
            for(int k=1; k<=n; k++)
                if(map[k][j][i] == 0 && check[k][j][i] == 0)
                    can_finish=false;
    if(!can_finish)
        return -1;
    else
        return ret;
}
