#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    int N, Mean, Mid, Max, Range;
    double Sum = 0.0;
    int tempMax = 0;
    int smallMax = 0;
    int idxCount = 0;
    
    int min = 4000;
    int max = -4000;
    
    int cnt[8002] = {0};
    cin >> N;
    for(int i=0; i<N; i++){
        int x;
        cin >> x;
        
        cnt[x+4000] += 1;
        Sum+=x;
        
        if(min > x){
            min = x;
        }
        if(max < x){
            max = x;
        }
    }
    
    // 중앙값 및 최빈값
    
    for(int i=0; i<=8001; i++){
        if(idxCount < ceil(N * 0.5)){
            idxCount += cnt[i];
            if(idxCount >= ceil(N * 0.5)){
                Mid = i - 4000;
                
            }
        }
        
        
        if(tempMax < cnt[i]){
            smallMax = 0;
            tempMax = cnt[i];
            Max = i-4000;
        }
        
        else if(tempMax == cnt[i] && smallMax == 0){
            smallMax = 1;
            tempMax = cnt[i];
            Max = i-4000;
        }
    }
    
    
    // Results
    Mean = round(Sum/N);
    if(Mean == -0){
        Mean = 0;
    }
    Range = max - min;

    cout << Mean << '\n';
    cout << Mid << '\n';
    cout << Max << '\n';
    cout << Range;
    

    return 0;
}
