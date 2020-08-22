#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

int check[10];
vector<int> v;
int n,m;
void make_list(int num)
{
    if(num == m){
        for(int a=0; a<v.size(); a++)
            printf("%d ", v[a]);
        printf("\n");
        return;
    }

    for(int i=1; i<=n; i++){
        if(check[i]) continue;
        check[i] = 1;
        v.push_back(i);
        make_list(num + 1);
        check[i] = 0;
        v.pop_back();
    }
}

int main(){
    scanf("%d%d", &n,&m);
    make_list(0);
    return 0;
}
