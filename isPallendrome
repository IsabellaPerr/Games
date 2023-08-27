#include <stdio.h>
#include <stdbool.h> 
#include <math.h>

int getDigit(int num, int n)
{
    int r;
    r = num / pow(10, n);
    r = r % 10;
    return r;
}

int isPalindrome(int x){
    if (x < 0){
        return false;
    }

    if (x == 0) {
        return true;
    }

    int tempx = x;
    int intLenght = 0;
    bool breakVar = true;

    while(breakVar) {

        tempx /= 10;

        if (tempx < 1) {
            breakVar = false;
        }
        intLenght += 1;
    }
    
    tempx = 0;
    int dig;
    for(int i = intLenght; i > 0; i--){
        dig = getDigit(x, i);

        tempx += (dig) * pow(10, i);
    }
    return !(tempx == x);

}

// ----------------------------
int main() {
  int x = isPalindrome(123);
    printf("%d\n", x);

  return 0;
}
