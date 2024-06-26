#include <stdio.h>

int main() {
    // == != < > <= >= && ||
    // ! เปลี่ยนจาก True เป็น False หรือ เปลี่ยนจาก False เป็น True

    // Operator part 2
    // +=
    int number = 5;
    printf("%d\n", number);
    number = number + 5;
    printf("%d\n", number);
    number += 5;
    printf("%d\n", number);
    
    // -=
    int number = 5;
    printf("%d\n", number);
    number = number - 3;
    printf("%d\n", number);
    number -= 3;
    printf("%d\n", number);
    
    // *=
    int number = 5;
    printf("%d\n", number);
    number = number * 3;
    printf("%d\n", number);
    number *= 3;
    printf("%d\n", number);
    
    // /=
    int number = 8;
    printf("%d\n", number);
    number = number / 2;
    printf("%d\n", number);
    number /= 2;
    printf("%d\n", number);
    
    // %=
    int number = 10;
    printf("%d\n", number);
    number = number % 3;
    printf("%d\n", number);
    number %= 3;
    printf("%d\n", number);
    
    // ++
    // ถ้าอยู่ข้างหลัง เพิ่ม number อีก 1 หลังจากจบบรรทัดนั้นๆ
    // ถ้าอยู่ข้างหน้า เพิ่ม number อีก 1 ไปเลยยยย!
    int number = 10;
    printf("%d\n", number++);
    printf("%d\n", number);
    printf("%d\n", ++number);
    printf("%d\n", number);

    // --
    // ถ้าอยู่ข้างหลัง ลบ number อีก 1 หลังจากจบบรรทัดนั้นๆ
    // ถ้าอยู่ข้างหน้า ลบ number อีก 1 ไปเลยยยย!
    int number = 10;
    printf("%d\n", number--);
    printf("%d\n", number);
    printf("%d\n", --number);
    printf("%d\n", number);
    
    return 0;
}
