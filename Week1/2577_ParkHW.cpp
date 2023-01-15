#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    int A, B, C;
    string result;

    cin >> A >> B >> C;
    result = to_string(A * B * C);
    
    for(int i = 0; i < 10; i++){
        int number = 0;
        
        for(int j = 0; j < result.size(); j++){
            int target = (int)result[j] - 48;
            if(target == i){
                number++;
            }
        }
        cout << number << '\n';
    }
    
    
    return 0;
}
