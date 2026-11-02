import ctypes
from pathlib import Path

from django.shortcuts import render

# Option 2: C sieve, built with
#   cc -O2 -shared -fPIC amicable_pairs/amicable.c -o amicable_pairs/libamicable.so
# If the library is missing or can't be loaded, the Python sieve is used instead.
C_MAX_LIMIT = 100_000_000  # keeps divisor sums inside a C int
C_MAX_PAIRS = 10_000

try:
    _lib = ctypes.CDLL(str(Path(__file__).with_name('libamicable.so')))
    _lib.find_amicable_pairs.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    _lib.find_amicable_pairs.restype = ctypes.c_int
except OSError:
    _lib = None


def find_amicable_pairs_c(limit):
    buf = (ctypes.c_int * (2 * C_MAX_PAIRS))()
    n = _lib.find_amicable_pairs(limit, buf, C_MAX_PAIRS)
    if n < 0:
        raise MemoryError('limit too large')
    return [(buf[2 * k], buf[2 * k + 1]) for k in range(n)]


# Option 1: pure Python sieve
def find_amicable_pairs_py(limit):
    # divisor_sums[n] = sum of proper divisors of n
    divisor_sums = [1] * (limit + 1)
    divisor_sums[0] = divisor_sums[1] = 0
    for i in range(2, limit // 2 + 1):
        for j in range(2 * i, limit + 1, i):
            divisor_sums[j] += i

    return [
        (a, b)
        for a, b in enumerate(divisor_sums)
        if a < b <= limit and divisor_sums[b] == a
    ]


def find_amicable_pairs(limit):
    if _lib is not None and limit <= C_MAX_LIMIT:
        return find_amicable_pairs_c(limit)
    return find_amicable_pairs_py(limit)

def amicable_numbers_view(request):
    amicable_pairs = []
    limit = None
    error_message = None

    if request.method == 'POST':
        limit_str = request.POST.get('limit')
        if not limit_str:
            error_message = 'Please enter a number. 🔢'
        else:
            try:
                limit = int(limit_str)
                if limit < 2:
                    error_message = 'Please enter a number greater than or equal to 2.'
                else:
                    amicable_pairs = find_amicable_pairs(limit)
                    if not amicable_pairs:
                        error_message = f'No amicable numbers found up to {limit}.'
            except ValueError:
                error_message = 'Please enter a valid integer.'

    return render(request, 'index.html', {
        'amicable_pairs': amicable_pairs,
        'limit' :limit,
        'error_message': error_message
    })