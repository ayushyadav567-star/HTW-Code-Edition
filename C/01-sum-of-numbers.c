#include <stdio.h>

int main(void) {
    int n;
    int sum = 0;

    printf("Enter a positive integer: ");
    if (scanf("%d", &n) != 1 || n < 1) {
        printf("Please enter a positive integer.\n");
        return 1;
    }
//there was no = sign because of which the loop was only running till n-1
    for (int i = 1; i <= n; i++) {
        sum += i;
    }

    printf("Sum from 1 to %d = %d\n", n, sum);
    return 0;
}
