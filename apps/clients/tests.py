import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_client_status_code_200_ok(client):
    url = reverse('clients')
    response = client.get(url)
    assert response.status_code == 200
