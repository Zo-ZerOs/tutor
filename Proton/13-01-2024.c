#include <stdio.h>

int main() {
    printf("- Array -\n");
    int a[3]; // a มีช่อง 3 ช่อง ได้แก่ a[0], a[1], a[2]
    int b[5] = {1, 3, 4, 2, 6};
    printf("%d", b[0]); // 1
    printf("%d", b[1]); // 3
    printf("%d", b[2]); // 4
    printf("%d", b[3]); // 2
    printf("%d", b[4]); // 6
    
    // การรับค่าใส่ array เป็นจำนวน n ตัว
    int c[100], n;
    scanf("%d", &n);
    for (int i = 0 ; i < n ; i++) {
        scanf("%d", &c[i]);
    }
    // การแสดงค่าใน array เป็นจำนวน 10 ตัว
    for (int i = 0 ; i < 10 ; i++) {
        printf("%d", &c[i]);
    }
    
    return 0;
}
