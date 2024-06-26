#include <stdio.h>

int main() {
    printf("- Ascii -\n");
    char c = 'A';
    // จำแค่ 3 ตัวก็พอ
    // ascii: '0'=48, 'A'=65, 'a'=97
    printf("%d", c);
    
    printf("- String -\n");
    char a[100] = "Hello"; //array of character = string
    for (int i = 0 ; i < 5 ; i++) {
        printf("%c", a[i]);
    }
    printf("\n");
    
    printf("%s", a); //สำหรับ string เท่านั้น
    
    char b[100] = "HelloWorld";
    for (int i = 0 ; i < 10 ; i++) {
        printf("%c", b[i] + 1);
    }

    char c = 'a'; //'a' = 97
    if (c < 98) printf("Yes"); //จะปริ้น Yes เพราะ 'a' < 98
    else printf("No");

    return 0;
}
