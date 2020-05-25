#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>

int main(void)
{
    int max_len, n, k = 0, sect = 0, c = 0;
    scanf("%d", &max_len);
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &c);
        if (c == 1 && sect <= i) {
            k++;
            sect = i + max_len - 1;
        }
        if (sect > 0)
            sect--;
    }
    printf("%d\n", k);
    return 0;
}
