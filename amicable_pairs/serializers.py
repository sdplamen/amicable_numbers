from rest_framework import serializers

# class AmicablePairSerializer(serializers.Serializer):
#     number1 = serializers.IntegerField()
#     number2 = serializers.IntegerField()

class AmicableNumbersSerializer(serializers.Serializer):
    limit = serializers.IntegerField()
    # amicable_pairs = AmicablePairSerializer(many=True)
    # message = serializers.CharField(required=False)
    # error = serializers.CharField(required=False)