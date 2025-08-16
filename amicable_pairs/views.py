from django.shortcuts import render

# Create your views here.
def sum_proper_divisors(n):
    division_sum = 1
    limit = int(n ** 0.5) + 1
    for i in range(2, limit):
        if n % i == 0:
            division_sum += i
            if i != n // i:
                division_sum += n // i
    return division_sum

def find_amicable_pairs(limit):
    amicable_pairs = []
    divisor_sums = {}

    for a in range(2, limit + 1) :
        if a in divisor_sums :
            continue

        sum_b = sum_proper_divisors(a)

        if sum_b <= a or sum_b > limit :
            divisor_sums[a] = sum_b
            continue

        sum_c = sum_proper_divisors(sum_b)

        if sum_c == a :
            amicable_pairs.append((a, sum_b))
            divisor_sums[a] = sum_b
            divisor_sums[sum_b] = a

    return amicable_pairs

def amicable_numbers_view(request):
    amicable_pairs = []
    limit = None
    error_message = None

    if request.method == 'POST' :
        limit_str = request.POST.get('limit')
        if not limit_str :
            error_message = 'Please enter a number. 🔢'
        else :
            try :
                limit = int(limit_str)
                if limit < 2 :
                    error_message = 'Please enter a number greater than or equal to 2.'
                else :
                    amicable_pairs = find_amicable_pairs(limit)
                    if not amicable_pairs :
                        error_message = f'No amicable numbers found up to {limit}.'
            except ValueError :
                error_message = 'Please enter a valid integer.'

    return render(request, 'index.html', {
        'amicable_pairs' :amicable_pairs,
        'limit' :limit,
        'error_message' :error_message
    })