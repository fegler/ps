#include <stdio.h>
#include <algorithm>

using namespace std;

int board[55][55];
int n,m;
int result=987654321;

int num_change(int wb, int start_y, int start_x);
int main()
{
    //input
    scanf("%d%d\n", &n,&m);

    //each line of board input
    char temp[55];
    for(int a=0; a<n; a++)
    {
        scanf("%s", temp);
        for(int b=0; b<m; b++)
        {
            if(temp[b] == 'W')
                board[a][b] = 0;
            else
                board[a][b] = 1;
        }
    }

    //check the number of change at each point of board
    for(int a=0; a<=n-8; a++)
    {
        for(int b=0; b<=m-8; b++)
        {
            result = min(result, min(num_change(0,a,b), num_change(1,a,b)));
        }
    }
    printf("%d\n", result);
}

int num_change(int wb, int start_y, int start_x)
{
    int check_even, check_odd;
    int result = 0;

    for(int a=0; a<8; a++)
    {
        if(wb == 0) {
            if(a%2 == 0)
                check_even = 0, check_odd = 1;
            else
                check_even = 1, check_odd = 0;
        } else{
            if(a%2 == 0)
                check_even = 1, check_odd = 0;
            else
                check_even = 0, check_odd = 1;
        }
        for(int b=0; b<8; b++)
        {
            int pos_y = start_y + a;
            int pos_x = start_x + b;
            if(b%2 == 0 && board[pos_y][pos_x] != check_even) result += 1;
            if(b%2 == 1 && board[pos_y][pos_x] != check_odd) result += 1;
        }
    }
    return result;
}
