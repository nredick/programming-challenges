#include <iostream>
#include<algorithm> 
using namespace std; 

int main() {
	int n, r, e, c; 
	std::cin >> n;
        for (int i = 0; i < n; i++) {
		std::cin >> r >> e >> c;
		if (r < e-c){
			std::cout << "advertise\n"; 
		}else if (r == e-c) {
			std::cout << "does not matter\n";
		}else { 
			std::cout << "do not advertise\n";
		}		
	}	
}
