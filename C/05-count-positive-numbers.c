#include <stdio.h>

int main(void) {
    int n;
    int count = 0;

    printf("How many integers will you enter? ");
    if (scanf("%d", &n) != 1 || n < 1 || n > 100) {
        printf("Enter a count from 1 to 100.\n");
        return 1;
    }

    printf("Enter %d integers:\n", n);
    for (int i = 0; i < n; i++) {
        int value;
        if (scanf("%d", &value) != 1) {
            printf("Invalid input.\n");
            return 1;
        }

        if (value > 0) {
            count++;
        }
    }

    printf("Positive numbers: %d\n", count);
    return 0;
}
