#include <stdio.h>

int main() {
    // Data Type
    printf("- Data Type -\n");
    int integer = 10; //จำนวนเต็ม (%d)
    float rational = 3.3; //ทศนิยม (%f)
    char character = 'A'; //ตัวอักษร (%c)
    
    scanf("%c", &character);
    printf("%c\n", character);
    scanf("%d", &integer);
    printf("%d\n", integer);
    scanf("%f", &rational);
    printf("%.3f\n", rational); // %.nf จะพิมพ์ทศนิยมออกมา n ตำแหน่ง
    
    // Variable
    /*
    1. ห้ามขึ้นต้นด้วยตัวเลข เช่น 3rd, 76XDGGEZ
    2. ห้ามเป็นชื่อสำคัญ เช่น printf, int, return
    3. ห้ามมีตัวอังษรพิเศษ(ยกเว้น _) เช่น #thank, th@n
    4. ห้ามมี _ อย่างเดียว เช่น _
    */
    
    //Operator
    printf("- Operator -\n");
    printf("1. =\n");
    // 1. =
    int a, b;
    float c;
    a = 3;
    b = a; // เอาค่าที่อยู่ใน a ไปใส่ใน b (โดยที่ a ก็ยัง
    
    printf("%d %d\n", a, b);
    b = 4; // แก้ค่าใน b แต่ a ก็จะไม่เปลี่ยน
    printf("%d %d\n", a, b);
    
    return 0;
}
