from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import math


def sum_proper_divisors(n) :
    division_sum = 1
    limit = int(n ** 0.5) + 1
    for i in range(2, limit) :
        if n % i == 0 :
            division_sum += i
            if i != n // i :
                division_sum += n // i
    return division_sum


def find_amicable_pairs(limit) :
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


class AmicableNumbersAPI(APIView) :
    def get(self, request) :
        limit_str = request.query_params.get('limit')

        if not limit_str :
            return Response({
                'error' :'Please provide a limit parameter'
            }, status=status.HTTP_400_BAD_REQUEST)

        try :
            limit = int(limit_str)
            if limit < 2 :
                return Response({
                    'error' :'Limit must be greater than or equal to 2'
                }, status=status.HTTP_400_BAD_REQUEST)

            amicable_pairs = find_amicable_pairs(limit)

            if not amicable_pairs :
                return Response({
                    'message' :f'No amicable numbers found up to {limit}',
                    'limit' :limit,
                    'amicable_pairs' :[]
                }, status=status.HTTP_200_OK)

            return Response({
                'limit' :limit,
                'amicable_pairs' :amicable_pairs
            }, status=status.HTTP_200_OK)

        except ValueError :
            return Response({
                'error' :'Please provide a valid integer'
            }, status=status.HTTP_400_BAD_REQUEST)