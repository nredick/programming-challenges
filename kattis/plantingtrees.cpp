#include <iostream>
#include <algorithm>
#include <queue>
using namespace std; 


int main (){
	/* init var for # of seeds, day of party, and seedling
	 * for keeping track of trees to push onto queue */
	int seeds, partytime = 1, tree = 0;  
	cin >> seeds; // get number of seedlings 
	
	priority_queue <int> grow; // declare an array to hold the growth times 
	for (int i = 0; i < seeds; i++){ // init arr values from input 
		cin >> tree; 
		grow.push(tree);	
	}
	// greedy algorithm 
	int day = 1; // init var to keep track of what day it is  
	while(!grow.empty()) { // while there's still seedlings in the queue
		// set the day of party to max of queue + how many day's it's been 
		// (because only one tree can be planted each day)
		// and the prev partytime  
		partytime = max(grow.top() + ++day, partytime); 
	        grow.pop(); // remove the compared seedling from the queue 
	}
	cout << partytime; // result 
}
