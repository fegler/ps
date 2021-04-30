#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> h;
int sum_value;

void print_result(int id1, int id2){
    for(int i=0; i<9; i++){
        if(i != id1 && i != id2)
            printf("%d\n", h[i]);
    }
}

int main()
{
    for(int i=0; i<9; i++){
        int temp;
        scanf("%d", &temp);
        h.push_back(temp);
        sum_value += temp;
    }

    sort(h.begin(), h.end());

    for(int i=0; i<9; i++){
        for(int j=i+1; j<9; j++){
            if((sum_value - (h[i] + h[j])) == 100){
                print_result(i, j);
                return 0;
            }
        }
    }

    return 0;
}
