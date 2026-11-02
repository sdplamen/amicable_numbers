#include <stdlib.h>

/* Divisor-sum sieve, same logic as find_amicable_pairs_py in views.py.
   Fills out[] with a,b,a,b,... and returns the number of pairs (-1 if out of memory). */
int find_amicable_pairs(int limit, int *out, int max_pairs) {
    int *divisor_sums = calloc(limit + 1, sizeof(int));
    if (!divisor_sums) return -1;

    for (int i = 1; i <= limit / 2; i++)
        for (int j = 2 * i; j <= limit; j += i)
            divisor_sums[j] += i;

    int n = 0;
    for (int a = 2; a <= limit && n < max_pairs; a++) {
        int b = divisor_sums[a];
        if (b > a && b <= limit && divisor_sums[b] == a) {
            out[2 * n] = a;
            out[2 * n + 1] = b;
            n++;
        }
    }
    free(divisor_sums);
    return n;
}
