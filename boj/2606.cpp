#include <stdio.h>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

int check[105];
int n,e;
queue<int> qu;
vector<int> com[105];

int solve(int start);

int main(){
    scanf("%d%d", &n,&e);
    for(int i=0; i<e; i++){
        int start, end;
        scanf("%d%d", &start, &end);
        com[start].push_back(end);
        com[end].push_back(start);
    }
    printf("%d\n", solve(1)-1);
    return 0;
}

int solve(int start){
    int ret = 0;
    check[start] = 1;
    qu.push(start);
    while(!qu.empty()){
        int top_c = qu.front();
        ret += 1;
        qu.pop();
        for(int i=0; i<com[top_c].size(); i++){
            if(check[com[top_c][i]])
                continue;
            check[com[top_c][i]] = 1;
            qu.push(com[top_c][i]);
        }
    }
    return ret;
}
