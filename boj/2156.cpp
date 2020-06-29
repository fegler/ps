#include <stdio.h>
#include <algorithm>
#include <iostream>

using namespace std;

int ans[10005];
int n;
int podo[10005];

int main()
{
    scanf("%d", &n);
    for(int i=1; i<=n; i++)
        scanf("%d", &podo[i]);

    ans[1] = podo[1];
    ans[2] = podo[2] + podo[1];
    ans[3] = max(ans[2], max(podo[1]+podo[3], podo[2]+podo[3]));

    for(int i=3; i<=n; i++)
        ans[i] = max(ans[i-1], max(ans[i-3]+podo[i-1]+podo[i], ans[i-2] + podo[i]));
    printf("%d\n", ans[n]);
    return 0;
}