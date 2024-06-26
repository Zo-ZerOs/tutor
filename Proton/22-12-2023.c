#include <stdio.h>

int main() {
    // loop : for, while, do - while
    printf("- FOR -\n");
    
    /*
    for ( initial ; condition ; update ) {
        statements
    }
    initial -> condition -> statement -> update -> condition -> ...
    จะทำก็ต่อเมื่อ condition เป็นจริง จะหลุดก็ต่อเมื่อ condition เป็นเท็จ
    */
    int i, j;
    for ( i = 0 ; i < 10 ; i++ ) {
        printf("A ");
    }
    for ( i = 3 ; i < 10 ; i *= 2) {
        printf("B ");
    }
    for ( i = 0 ; i < 3 ; i++ ) {
        for ( j = 0 ; j < 4 ; j++ ) {
            printf("# ");
        }
        printf("\n");
    }
    
    // รับค่าจำนวนเต็ม 2 จำนวน (n และ m) โดยที่ n < m
    // หาผลบวกของตัวเลขจำนวนเต็มทุกตัวตั้งแต่ n ถึง m
    int i, n, m, sum = 0;
    scanf("%d %d", &n, &m);
    for ( i = n ; i <= m ; i++ ) {
        sum += i;
    }
    printf("%d", sum);
    // ex. n = 3, m = 10
    // i = 11
    // sum = 0 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    
    return 0;
}
