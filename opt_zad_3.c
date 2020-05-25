#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>

typedef unsigned int uint;

#define min(a, b)   ((a) < (b) ? (a) : (b))

bool array_has(const uint *array, uint start, uint size, uint tgt, uint *idx)
{
    bool has = false;
    for (uint i = start; i < size; i++) {
        if (array[i] == tgt) {
            has = true;
            *idx = i;
            break;
        }
    }
    return has;
}

int main(void)
{
    uint max_len, n, k = 0, start = 0, end = 0, idx;
    uint *z;
    scanf("%d", &max_len);
    scanf("%d", &n);
    z = malloc(sizeof(*z) * n);
    for (uint i = 0; i < n; i++)
        scanf("%d", &z[i]);
    while (array_has(z, start, n, 1, &idx)) {
        end = idx + max_len;
        for (uint i = idx; i < end; i++) {
            z[min(i, n - 1)] = 0;
        }
        k += 1;
    }
    printf("%d\n", k);
    free(z);
    return 0;
}
