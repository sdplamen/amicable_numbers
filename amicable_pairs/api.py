from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from amicable_pairs.serializers import AmicableNumbersSerializer
from amicable_pairs.views import find_amicable_pairs


class AmicableNumbersAPI(APIView):
    serializer_class = AmicableNumbersSerializer

    def post(self, request) :
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() :
            limit = serializer.validated_data['limit']
            if limit <= 0 :
                return Response({'error' :'The limit must be a positive integer.'}, status=status.HTTP_400_BAD_REQUEST)

            amicable_pairs = find_amicable_pairs(limit)

            response_data = {
                'limit' :limit,
                'amicable_pairs' :amicable_pairs,
                'count' :len(amicable_pairs)
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)