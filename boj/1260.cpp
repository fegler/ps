#include <stdio.h>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

int check[1005];
vector<int> node[1005];

void dfs(int n);
void bfs(int n);

int main(){
    int n,m,start;
    scanf("%d%d%d", &n,&m,&start);

    // generate bi-directional graph
    for(int i=1; i<=m; i++){
        int s, d;
        scanf("%d%d",&s,&d);
        node[s].push_back(d);
        node[d].push_back(s);
    }
    // for smaller first rule
    for(int i=0; i<=n; i++)
        sort(node[i].begin(), node[i].end());

    check[start] = 1;
    dfs(start);
    printf("\n");

    for(int i=0; i<=n; i++)
        check[i] = 0;
    bfs(start);
}

void dfs(int n){
    printf("%d ", n);
    for(int i=0; i<node[n].size(); i++){
        int next_n = node[n][i];
        if(check[next_n])
            continue;
        check[next_n] = 1;
        dfs(next_n);
    }
}

void bfs(int n){
    queue<int> qu;
    qu.push(n);
    check[n] = 1;
    while(!qu.empty()){
        int top_n = qu.front();
        qu.pop();
        printf("%d ", top_n);
        for(int i=0; i<node[top_n].size(); i++){
            if(check[node[top_n][i]])
                continue;
            qu.push(node[top_n][i]);
            check[node[top_n][i]] = 1;
        }
    }
    printf("\n");
}
