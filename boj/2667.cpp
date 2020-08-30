#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <string.h>
using namespace std;

int map[30][30];
vector<int> results;
int n;
int pos_x[] = {0, -1, 0, 1};
int pos_y[] = {-1, 0, 1, 0};

int dfs(int x, int y);

int main(){
    scanf("%d", &n);
    for(int i=1; i<=n; i++){
        string temp;
        cin>>temp;
        for(int j=0; j<temp.length(); j++){
            if(temp[j] == '1')
                map[j+1][i] = 1;
        }
    }
    
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(map[j][i]) {
                map[j][i] = 0;
                results.push_back(dfs(j, i));
            }
        }
    }
    printf("%d\n", results.size());
    sort(results.begin(), results.end());
    for(int i=0; i<results.size(); i++)
        printf("%d\n", results[i]);

    return 0;
}

int dfs(int x, int y){
    int ret = 1;
    for(int coord=0; coord<4; coord++){
        int next_x = x + pos_x[coord];
        int next_y = y + pos_y[coord];
        if(map[next_x][next_y]) {
            map[next_x][next_y] = 0;
            ret += dfs(next_x, next_y);
        }
    }
    return ret;
}
