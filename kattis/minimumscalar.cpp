#include <iostream> 
#include <queue>
using namespace std;

int main() {
	// define a priority q that uses < for ordering
	priority_queue<long long, vector<long long>, greater_equal<long long> > v1;
	
	// define a priority q that uses > for ordering 
	priority_queue<long long, vector<long long>, less_equal<long long> > v2;

	int ncases;
	cin >> ncases; 
	for (int i = 1; i <= ncases; i++){
       		// define var for dim of vectors and init 
		int dim; 
		long long el; 
		cin >> dim;

		// fill first q for v1 
		for(int j = 0; j < dim; j++){
			cin >> el; 
			v1.push(el); 
		}

		// fill first q for v2 
		for(int j = 0; j < dim; j++){
			cin >> el; 
			v2.push(el); 
		}
		
		// init a var to store the dot product of the vectors 
		long long dot = 0; 
		// compute the dot product
		while(!v1.empty() && !v2.empty()){
			dot += v1.top() * v2.top();
			v1.pop();
			v2.pop();			
		}
		cout << "Case #" << i << ": " << dot << "\n";		
	}
}
