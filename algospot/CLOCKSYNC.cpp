#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define INF 987654321
using namespace std;

int c, tmp, status[16];
int answer = INF;
char swt_value[10][17] = {
        "oooxxxxxxxxxxxxx",
        "xxxoxxxoxoxoxxxx",
        "xxxxoxxxxxoxxxoo",
        "oxxxooooxxxxxxxx",
        "xxxxxxoooxoxoxxx",
        "oxoxxxxxxxxxxxoo",
        "xxxoxxxxxxxxxxoo",
        "xxxxooxoxxxxxxoo",
        "xoooooxxxxxxxxxx",
        "xxxoooxxxoxxxoxx",

};

void time_change(int idx, int num, bool is_plus){
    for(int i=0; i<16; i++){
        if(swt_value[idx][i] == 'o') {
            if (is_plus) {
                status[i] += (num * 3);
                if (status[i] > 12) status[i] -= 12;
            } else {
                status[i] -= (num * 3);
                if (status[i] < 3) status[i] += 12;
            }
        }
    }
}

bool time_correct(){
    for(int i=0; i<16; i++)
        if(status[i] != 12) return false;
    return true;
}

void time_select(int idx, int num){
    if(time_correct()){
        answer = min(answer, num);
        return;
    }
    if(idx == 10) return;
    for(int i=0; i<4; i++){
        time_change(idx, i, true);
        time_select(idx+1, num+i);
        time_change(idx, i, false);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> c;
    for(int tc=0; tc<c; tc++){
        answer = INF;
        for(int i=0; i<16; i++){
            cin >> tmp;
            status[i] = tmp;
        }
        time_select(0,0);
        if(answer == INF) cout << "-1\n";
        else cout << answer<<"\n";
    }
    return 0;
}

