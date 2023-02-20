from django.urls import reverse


class TestURL():
    def test_client_url(self):
        response = reverse('values')
        self.assertEqual(response, '/api/v1/clients')
