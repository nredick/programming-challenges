// imports
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>


int main() {
    // get n & p where n = # of commercial breaks & p = price/break 
    int n, p; 
    assert(scanf("%d %d", &n, &p) == 2);
    
    // make list of students listening per commercial break
    int breaks[n]; 
    for(int i = 0; i < n; i++){
        assert(scanf("%d", &breaks[i]) == 1);
        breaks[i] -= p; 
    }
    
    int local_max, global_max = 0; 

    for(int i = 0; i < n; i++){
        if (breaks[i] > breaks[i] + local_max){
            local_max = breaks[i];
        }else {
            local_max = breaks[i] + local_max; 
        }
        
        //local_max = max(breaks[i], breaks[i] + local_max);
        if (local_max > global_max){
            global_max = local_max; 
        }
    }
    printf("%d", global_max);
        return 0; //success 
}

