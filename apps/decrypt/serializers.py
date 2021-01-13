from rest_framework import serializers


class DecryptMessageSerializer(serializers.Serializer):
    passphrase = serializers.CharField(required=True)
    message = serializers.CharField(required=True)
