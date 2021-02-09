#include <iostream> 
using namespace std; 

int main() {
	string s;
        string r = "";  	
	cin >> s; 
	for (int i = 0; i < s.length(); i++){
		if(int(s[i]) == 101) {
			r += "ee";
		}else { 
			r += s[i];
		}
	}
	cout << r; 
}
