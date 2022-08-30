#include <iostream>
#include <deque>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t, n, error;
    string p, nums;
    bool rev;
    deque<string> cutNums;

    cin >> t;
    while(t--){
        cin >> p;
        cin >> n;
        cin >> nums;
        rev = false; // R 여부 초기화
        error = 0; // error 여부 초기화

// string nums 입력값 괄호 삭제 
        nums.erase(nums.begin()); 
        nums.erase(nums.end()-1);

// string nums 입력값 , 기준으로 split
        istringstream ss(nums);
        string stringBuffer;
        cutNums.clear();

        while(getline(ss,stringBuffer, ',')){
            cutNums.push_back(stringBuffer);
        }

// 'R'인 경우 => rev 여부 바꿔줌/ 'D'인 경우 => 크기 확인 후 0인 경우 error, 아닌경우 rev = true 일 때 pop_back, false 일 때 pop_front
        for(auto i : p){
            if(i == 'R' && rev == false){
                rev = true;
            }else if(i == 'R' && rev == true){
                rev = false;
            }else if(i == 'D'){
                if(cutNums.size() == 0) error = -1;
                else{
                    if(rev == false) cutNums.pop_front();
                    else cutNums.pop_back();
                }
            }
        }

        // 출력
        if(error == -1) cout << "error" << '\n'; 
        else if(cutNums.size() != 0){
            cout << '[';
            if(rev == false){ 
                cout << cutNums.front();
                cutNums.pop_front();
                for(auto i = cutNums.begin(); i < cutNums.end(); i++){
                    cout << "," << *i;
                }
            }else{
                cout << cutNums.back();
                cutNums.pop_back();
                for(auto i = cutNums.rbegin(); i < cutNums.rend(); i++){
                    cout << "," << *i;
                }
            }
            cout << ']' << '\n';
        }else if(cutNums.size() == 0){ // 'D' 없이 'R' 중 입력값 없는 경우 출력
            cout << "[]" << '\n';
        }
    }

}