#include <stdio.h>
#include <algorithm>

int ret[25];

void path_finder(int n, int from, int middle, int to)
{
    if(n == 1)
    {
        printf("%d %d\n", from, to);
        return;
    }

    path_finder(n-1, from, to, middle);
    printf("%d %d\n", from, to);
    path_finder(n-1, middle, from, to);
}
int main()
{
    int n;
    scanf("%d", &n);
    ret[1] = 1;
    for(int i=2; i<=n; i++)
        ret[i] = ret[i-1]*2 + 1;
    printf("%d\n", ret[n]);

    path_finder(n, 1, 2, 3);
    return 0;
}
