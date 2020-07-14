#include <stdio.h>
#include <algorithm>

int solve();

int check_locy[4][2] = {{1,0}, {1,1}, {1,1}, {0,1}};
int check_locx[4][2] = {{0,1}, {0,-1}, {0,1}, {1,1}};
int h, w;
int grid[30][30];

int main()
{
    int t;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d %d\n", &h, &w);
        for(int i=0; i<h; i++)
        {
            char grid_temp[35];
            scanf("%s", grid_temp);
            for(int j=0; j<w; j++)
            {
                if(grid_temp[j] == '#')
                    grid[i][j] = 1;
                else
                    grid[i][j] = 0;
            }
        }
        int result = solve();
        printf("%d\n", result);
    }
    return 0;
}

int solve()
{
    int result = 0;
    int pox = -1;
    int poy = -1;

    for(int i=0; i<h; i++)
    {
        for (int j = 0; j < w; j++)
            if (grid[i][j] == 0) {
                poy = i, pox = j;
                break;
            }
        if(poy != -1)
            break;
    }
    if(pox == -1 || poy == -1)
        return 1;

    for(int k=0; k<4; k++) {
        int can_fill = 1;
        for (int l = 0; l < 2; l++) {
            int next_y = poy + check_locy[k][l];
            int next_x = pox + check_locx[k][l];
            if (next_y < 0 || next_y >= h
            || next_x < 0 || next_x >= w
            || grid[next_y][next_x] > 0) {
                can_fill = 0;
                break;
            }
        }
        if (can_fill) {
            grid[poy][pox] = 1;
            for (int l = 0; l < 2; l++)
                grid[poy + check_locy[k][l]][pox + check_locx[k][l]] = 1;
            result += solve();
            grid[poy][pox] = 0;
            for (int l = 0; l < 2; l++)
                grid[poy + check_locy[k][l]][pox + check_locx[k][l]] = 0;
        }
    }
    return result;
}
