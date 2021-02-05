// imports 
#include <stdio.h> 
#include <math.h>

int main() {
    int num; int boxes; // where num = # of inputs to follow; boxes = # of ballot boxes
    while(scanf("%d %d", &num, &boxes) == 2 && num != -1) {
        int l = 1; int mid; int max = 0; 
        int pop[num]; // declare arr to keep track of inputs of populations
        for (int i = 0; i < num; i++) {
            // find largest population in a case and put all the pops into pop
            if (scanf("%d", &pop[i]) == 1 && pop[i] > max) { 
                max = pop[i]; 
            }
        }

        int people = max; // people = max # of people @ 1 box in most efficient case
        while(l <= max) {
            int box = 0; // number of boxes distributed
            mid = (l + max)/2; // half of largest population 
            
            /* for each of the populations, divide by half the 
             * largest population of the case. then add 1 if there's 
             * a remainder or 0 if there's not (to assign 1 box to cities with
             * a pop > mid). that is the # of boxes distributed to that city
             */

            for (int i = 0; i < num; i++) {
                box += pop[i]/mid + (pop[i]%mid != 0);
            }
            
            /* if boxes distributed (box) is less than all of the boxes that  
             * need to be assigned, then set max to one less than mid, set people to  
             * mid. else, let l = one more than mid 
             */

            if (box <= boxes) {
                max = mid - 1;
                people = mid;
            }else { 
                l = mid + 1;
            }
        }
        // print max # of people assigned to 1 box @ efficient assignment
        printf("%d\n", people);
    }
    return 0; // success
}
