from gnupg import GPG
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.decrypt.serializers import DecryptMessageSerializer


# Create your views here.
class DecryptMessageAPIView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = DecryptMessageSerializer

    def post(self, request):
        """Decrypts the given encrypted message using the given passphrase."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        passphrase = serializer.validated_data["passphrase"]
        message = serializer.validated_data["message"]

        decrypted = GPG().decrypt(message, passphrase=passphrase)
        return Response({"DecryptedMessage": decrypted.data})
