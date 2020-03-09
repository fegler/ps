#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

int ans[10005];
int n,k;

int main() {

    scanf("%d%d", &n,&k);

    ans[0] = 1;
    int coin;
    for(int i=0; i<n; i++)
    {
        scanf("%d", &coin);
        for(int j=coin; j<=k; j++)
            ans[j] += ans[j-coin];
    }
    printf("%d\n", ans[k]);
    return 0;
}