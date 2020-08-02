#include <stdio.h>
#include <algorithm>
#include <math.h>
using namespace std;

int num_order(int n, int x, int y)
{
    // ending point -> only 2x2 grid
    if(n==1){
        if(x==1){
            if(y==1) return 1;
            else return 3;
        }
        else{
            if(y==1) return 2;
            else return 4;
        }
    }

    int ret = 0;
    int grid_wh = pow(2, n);
    int half_grid = grid_wh/2;
    if(x > grid_wh/2){
        if(y > half_grid) {
            ret += grid_wh * half_grid + half_grid * half_grid;
            x -= half_grid;
            y -= half_grid;
        }
        else {
            ret += half_grid * half_grid;
            x -= half_grid;
        }
    }
    else{
        if(y > half_grid) {
            ret += grid_wh * half_grid;
            y -= half_grid;
        }
    }
    ret += num_order(n-1, x, y);
    return ret;
}

int main()
{
    int n,x,y;
    scanf("%d%d%d", &n,&x,&y);
    printf("%d\n", num_order(n,y+1,x+1)-1);
    return 0;
}
