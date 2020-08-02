#include <stdio.h>
#include <algorithm>
using namespace std;
#define INF 987654321
int dp[1000005];

int main()
{
    int n;
    scanf("%d", &n);

    //init dp to INF for min() function.
    for(int i=2; i<=n; i++)
        dp[i] = INF;

    for(int i=1; i<=n; i++){
        if(i*3 <= n)
            dp[i*3] = min(dp[i*3], dp[i]+1);
        if(i*2 <= n)
            dp[i*2] = min(dp[i*2], dp[i]+1);
        dp[i+1] = min(dp[i+1], dp[i]+1);
    }

    printf("%d\n", dp[n]);
}
