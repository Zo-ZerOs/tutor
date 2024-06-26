#include <stdio.h> // std = standard, i = input, o = output

int main() {
    // Basic I/O function (printf and scanf)
    printf("- BASIC -\n");
    int n = 3, m = 12, k = 25; // สร้าง variable ชื่อ n มีชนิดคือ integer (เอาไว้เก็บจำนวนเต็ม)
    printf("%d %d %d\n", n, m, k); // แสดงผล
    
    int number;
    printf("Please enter any number: ");
    scanf("%d", &number); // รับค่า
    printf("%d\n", number);
    
    // Variable and Data Type
    // มีอยู่หลายอย่าง เช่น int, float, char, (long, double, pointer, etc.)
    printf("- DATA TYPE -\n");
    int integer; // ex. 3, 5, 18
    float rational; // 3.0, 5.27, 18.00562851
    char character; // 'a', '5', '#'
    
    printf("Please Enter 1 integer: ");
    scanf("%d", &integer);
    printf("Please Enter 1 rational: ");
    scanf("%f", &rational);
    printf("Please Enter 1 character: ");
    scanf("%c", &character);
    
    printf("%d %f %c", integer, rational, character);
    
    return 0;
}
