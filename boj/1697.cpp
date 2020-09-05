#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

queue<pair<int,int>> qu;
int check[100005];
int n,m;
int solve_bfs();
int main()
{
    scanf("%d%d", &n,&m);
    printf("%d\n", solve_bfs());
    return 0;
}

int solve_bfs(){
    check[n] = 1;
    qu.push(make_pair(n, 0));
    while(!qu.empty()){
        pair<int,int> top = qu.front();
        qu.pop();
        if(top.first == m)
            return top.second;
        if(top.first - 1 >= 0 && !check[top.first-1]){
            check[top.first-1] = 1;
            qu.push(make_pair(top.first - 1, top.second + 1));
        }
        if(top.first + 1 <= 100000 && !check[top.first+1]){
            check[top.first+1] = 1;
            qu.push(make_pair(top.first+1, top.second+1));
        }
        if(top.first*2 <= 100000 && !check[top.first*2]){
            check[top.first*2] = 1;
            qu.push(make_pair(top.first*2, top.second+1));
        }
    }
}
