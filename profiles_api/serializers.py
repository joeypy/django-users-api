from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    '''Serializes a name field for testing out APIView'''
    name = serializers.CharField(max_length=10)
    # email = serializers.EmailField(max_length=255)
