#include <stdio.h>

int main() {
    // Operator
    // + - *
    printf("- Operator -\n");
    printf(" + - * \n");
    int a, b, ans;
    printf("a = ");
    scanf("%d", &a);
    printf("b = ");
    scanf("%d", &b);
    printf("ans = %d\n", a * b);
    
    // / (ผลลัพธ์ของ int / int จะได้ int แบบปัดลง)
    printf(" / \n");
    float a, b;
    printf("a = ");
    scanf("%f", &a);
    printf("b = ");
    scanf("%f", &b);
    printf("ans = %f\n", a / b);
    
    // % (เครื่องหมายหารเอาเศษ)
    printf(" % \n");
    int a, b;
    printf("a = ");
    scanf("%d", &a);
    printf("b = ");
    scanf("%d", &b);
    printf("ans = %d\n", a % b);
    
    // Logical Operator (==, !=, <, >, <=, >=, &&, ||)
    // 0: FALSE, เลขอื่นๆ = TRUE
    printf("- Logical Operator -\n");
    int a, b;
    printf("a = ");
    scanf("%d", &a);
    printf("b = ");
    scanf("%d", &b);
    printf("a is equal to b is %d\n", a == b); // == เท่ากัน?
    printf("a is not equal to b is %d\n", a != b); // != ไม่เท่ากัน?
    printf("a is less than b is %d\n", a < b); // < น้อยกว่า?
    printf("a is more than b is %d\n", a > b); // > มากกว่า?
    printf("a is less than or equal to b is %d\n", a <= b); // <= น้อยกว่า หรือ เท่ากัน?
    printf("a is more than or equal to b is %d\n", a >= b); // >= มากกว่า หรือ เท่ากัน?
    printf("a and b is %d\n", a && b); // && และ ต้องเป็นจริงทั้งคู่ถึงจะจริง
    printf("a and b is %d\n", a || b); // ||  หรือ ต้องเป็นเท็จทั้งคู่ถึงจะเท็จ
    // 5 < 4 เท็จ
    // 6 == 6 จริง
    // (3 != 7) && (5 < 4) = 1 && 0 = 0
    // {(7 >= 8) && 4} || 0 = 0
    
    // Condition (if-else)
    /*
    if (condition_1) {        ถ้าเกิด condition_1 เป็นจริง
        statement_1           ให้ทำ statement_1
    }
    else if (condition_2) {   แต่ถ้าเกิด condition_2 เป็นจริง
        statement_2           ให้ทำ statement_2
    }
    else {                    นอกนั้น
        statement_3           ให้ทำ statement_3
    }
    */
    int a = 3;
    // ถ้า a = 2 ให้ปริ้น 222 แต่ถ้า a = 5 ให้ปริ้น 555 นอกเหนือจากนั้นให้ปริ้น 000
    if (a == 2) {
        printf("222\n");
    }
    else if (a == 5) {
        printf("555\n");
    }
    else {
        printf("000\n");
    }

    // โจทย์ให้ฝึกใช้ if, else if, else
    // ถ้า a น้อยกว่า 10 ให้ปริ้น < , แต่ถ้า a เท่ากับ 10 ให้ปริ้น = , นอกเหนือจากนั้น ให้ปริ้น >

    return 0;
}
