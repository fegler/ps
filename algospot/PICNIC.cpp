#include <stdio.h>
#include <algorithm>

using namespace std;

int n,m;
int is_friend[10][10];
int taken[10];

int matching(int picked[10]);
int main(){
    int test_case;
    scanf("%d\n", &test_case);
    for(int i=0; i<test_case; i++){

        // friend information reset
        for(int a=0; a<10; a++)
            for(int b=0; b<10; b++)
                is_friend[a][b] = 0;

        // input
        scanf("%d %d\n", &n,&m);
        for(int j=0; j<m; j++){
            int f1,f2;
            scanf("%d %d", &f1, &f2);
            is_friend[f1][f2] = 1;
            is_friend[f2][f1] = 1;
        }

        // main algorithm
        for(int i=0; i<n; i++)
            taken[i] = 0;
        int answer = matching(taken);
        printf("%d\n", answer);
    }
}

int matching(int picked[10]){
    int min_student = -1;
    for(int i=0; i<n; i++)
        if(picked[i] == 0 && min_student < i){
            min_student = i;
            break;
        }
    if(min_student == -1)
        return 1;

    int answer = 0;
    for(int i=min_student+1; i<n; i++) {
        if (i == min_student) continue;
        if (!is_friend[min_student][i]) continue;
        if(picked[i]) continue;
        picked[i] = picked[min_student] = 1;
        answer += matching(picked);
        picked[i] = picked[min_student] = 0;
    }
    return answer;
}
