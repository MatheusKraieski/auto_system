import pytest
from django.urls import reverse

from apps.clients.models import Client


@pytest.mark.django_db
def test_client_status_code_200_ok(client):
    url = reverse('clients')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_db_is_correct(client):
    Client.objects.create(
        name="Matheus Kraieski",
        email="mathkraieski@gmail.com",
        cpf="1540620001",
        cnpj="00000000000000",
        first_phone="51994542807",
        second_phone="51993580435"
    )
    response = client.get(reverse('clients'))
    assert response.json() == [
        {
            "id": 1,
            "name": "Matheus Kraieski",
            "email": "mathkraieski@gmail.com",
            "cpf": "1540620001",
            "cnpj": "00000000000000",
            "first_phone": "51994542807",
            "second_phone": "51993580435"
        }
    ]
