#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

int n,m;
int start_p, end_p;
int check[105];
vector<int> chon[105];
int dfs(int person_id, int step);

int main(){
    scanf("%d", &n);
    scanf("%d%d", &start_p, &end_p);
    scanf("%d", &m);
    for(int i=1; i<=m; i++){
        int p1, p2;
        scanf("%d%d", &p1, &p2);
        chon[p1].push_back(p2);
        chon[p2].push_back(p1);
    }
    check[start_p] = 1;
    printf("%d\n", dfs(start_p, 0));
    return 0;
}

int dfs(int person_id, int step){
    if(person_id == end_p)
        return step;
    for(int i=0; i<chon[person_id].size(); i++){
        int next_p = chon[person_id][i];
        if(!check[next_p]){
            check[next_p] = 1;
            int ret = dfs(next_p, step+1);
            if(ret != -1)
                return ret;
            check[next_p] = 0;
        }
    }
    return -1;
}
