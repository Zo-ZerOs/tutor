#include <stdio.h>
#include <string.h>

int main() {

    int n = 1;
    char c = 'b'; // character
    
    char e[100] = "Proton"; // string
    char e[100] = {'P', 'r', 'o', 't', 'o', 'n'}; // character
    
    char A[100];
    scanf("%s", A);
    int len;
    len = strlen(A);
    
    int N_count = 0, S_count = 0, W_count = 0, E_count = 0;
    for (int i = 0 ; i < len ; i++) {
        if (A[i] == 'N') N_count++;
        else if (A[i] == 'S') S_count++;
        else if (A[i] == 'W') W_count++;
        else E_count++;
    }
    
    if (N_count != 0) printf("N:%d ", N_count);
    if (S_count != 0) printf("S:%d ", S_count);
    if (W_count != 0) printf("W:%d ", W_count);
    if (E_count != 0) printf("E:%d ", E_count);

    if (N_count - S_count > 0) printf("N:%d ", N_count - S_count);
    else if (N_count - S_count < 0) printf("S:%d ", -(N_count - S_count));
    if (W_count - E_count > 0) printf("W:%d ", W_count - E_count);
    else if (W_count - E_count < 0) printf("E:%d ", -(W_count - E_count));
    if ((N_count == S_count) && (W_count == E_count)) printf("0");
    
    return 0;
}
