#include <stdio.h>

int main() {
    int n = 0;
    scanf("%d", &n);

    // 1. 위쪽 절반 (늘어나는 부분)
    for (int i = 1; i <= n; i++) {
        // 왼쪽 별 출력 (i개)
        for (int j = 0; j < i; j++) {
            printf("*");
        }
        // 가운데 공백 출력 (2*n - 2*i개)
        for (int k = 0; k < 2 * n - 2 * i; k++) {
            printf(" ");
        }
        // 오른쪽 별 출력 (i개)
        for (int j = 0; j < i; j++) {
            printf("*");
        }
        printf("\n");
    }

    // 2. 아래쪽 절반 (줄어드는 부분)
    for (int i = n - 1; i > 0; i--) {
        // 왼쪽 별 출력 (i개)
        for (int j = 0; j < i; j++) {
            printf("*");
        }
        // 가운데 공백 출력 (2*n - 2*i개)
        for (int k = 0; k < 2 * n - 2 * i; k++) {
            printf(" ");
        }
        // 오른쪽 별 출력 (i개)
        for (int j = 0; j < i; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}