from django.shortcuts import render

# Create your views here.
def find_amicable_pairs(limit):
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