#include <stdio.h>

int main() {
    char c; 
    while(scanf("%c", &c) == 1){
        int ascii = (int) c;  
        if (ascii > 64 && ascii < 91){
            printf("%c", c);
        }
    }
}
