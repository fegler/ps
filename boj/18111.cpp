#include <stdio.h>
#include <algorithm>

using namespace std;

int map[505][505];
int n,m, b;
int min_value = 987654321;
int max_value;
int main(){
    scanf("%d%d%d", &n,&m, &b);
    for(int i=0; i<n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &map[i][j]);
            min_value = min(min_value, map[i][j]);
            max_value = max(max_value, map[i][j]);
        }
    }
    int result_sec = 987654321;
    int result_value;
    for(int v=min_value; v<=max_value; v++){
        int sec = 0;
        int need_block = 0;
        int out_block = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(map[i][j] > v){
                    sec += (2*(map[i][j] - v));
                    out_block += (map[i][j] - v);
                }
                else if(map[i][j] < v){
                    sec += (v - map[i][j]);
                    need_block += (v - map[i][j]);
                }
            }
        }
        if(b + out_block >= need_block){
            if(result_sec >= sec){
                result_sec = sec;
                result_value = v;
            }
        }
    }

    printf("%d %d\n", result_sec, result_value);
    return 0;
}
