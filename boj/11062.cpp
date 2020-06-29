#include <stdio.h>
#include <algorithm>
#include <iostream>

using namespace std;

int dp[1005][1005];
int card[1005];
int sum[1005];
int n, T;

int main()
{
    scanf("%d", &T);
    for(int k=0; k<T; k++)
    {
        scanf("%d", &n);
        for(int i=0; i<=n; i++)
            for(int j=0; j<=n; j++)
                dp[i][j] = 0;
        for(int i=1; i<=n; i++)
        {
            scanf("%d", &card[i]);
            sum[i] = sum[i-1] + card[i];
            dp[i][i] = card[i];
        }

        for(int len = 2; len<=n; len++)
        {
            for(int i=1; i<=n-len+1; i++)
            {
                int left_choice = card[i] + sum[i+len-1]-sum[i]-dp[i+1][i+len-1];
                int right_choice = card[i+len-1] + sum[i+len-2]-sum[i-1]-dp[i][i+len-2];
                dp[i][i+len-1] = max(left_choice, right_choice);
            }
        }
        printf("%d\n", dp[1][n]);
    }
    return 0;
}