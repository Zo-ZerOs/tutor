// Online C compiler to run C program online
#include <stdio.h>

void plus () {
    int num1, num2;
    scanf("%d %d", &num1, &num2);
    printf("%d\n", num1 + num2);
}

int power (int num1, int num2) {
    int ans = 1;
    for (int i = 0 ; i < num2 ; i++) {
        ans *= num1;
    }
    return ans;


int oraoraora () {
    return 8;
}

int main() {
    printf("- Function -\n");
    
    for (int i = 0 ; i < 100 ; i++) {
        plus();
    }
    
    int n, m;
    for (int i = 0 ; i < 100 ; i++) {
        scanf("%d %d", &n, &m);
        printf("%d\n", power(n, m));
    }
    
    int a;
    scanf("%d", &a);
    
    a = oraoraora();
    printf("%d", a);
    
    int x, y;
    scanf("%d %d", &x, &y);
    int answer = minus(x, y);
    printf("%d", answer);
    
    
    return 0;
}
