from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class DecryptMessageAPIViewTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = "/decryptMessage"

    def setUp(self):
        pass

    def test_decrypt_message_success(self):
        data = {
            "passphrase": "topsecret",
            "message": (
                "-----BEGIN PGP MESSAGE-----\n"
                "Version: GnuPG v2\n"
                "\n"
                "jA0ECQMCVady3RUyJw3X0kcBF+zdkfZOMhISoYBRwR3uk3vNv+TEg+rJnp4/yYIS\n"  # noqa: E501
                "pEoI2S82cDiCNBIVAYWB8WKPtH2R2YSussKhpSJ4mFgqyOA01uwroA==\n"
                "=KvJQ\n"
                "-----END PGP MESSAGE-----\n"
            ),
        }

        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("DecryptedMessage" in response.data)
        self.assertEqual(response.data["DecryptedMessage"], "Nice work!\n")

    def test_decrypt_message_invalid_payload(self):
        # missing "passphrase"
        data = {
            "message": (
                "-----BEGIN PGP MESSAGE-----\n"
                "Version: GnuPG v2\n"
                "\n"
                "jA0ECQMCVady3RUyJw3X0kcBF+zdkfZOMhISoYBRwR3uk3vNv+TEg+rJnp4/yYIS\n"  # noqa: E501
                "pEoI2S82cDiCNBIVAYWB8WKPtH2R2YSussKhpSJ4mFgqyOA01uwroA==\n"
                "=KvJQ\n"
                "-----END PGP MESSAGE-----\n"
            ),
        }

        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("passphrase" in response.data)
        self.assertEqual(
            response.data["passphrase"][0], "This field is required."
        )

        # missing "message"
        data = {
            "passphrase": "topsecret",
        }

        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("message" in response.data)
        self.assertEqual(
            response.data["message"][0], "This field is required."
        )
