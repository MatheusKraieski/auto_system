import pytest
from django.urls import reverse

from apps.clients.models import Client


@pytest.mark.django_db
def test_client_status_code_200_ok(client):
    url = reverse('clients')
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == []


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
    assert response.status_code == 200
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


@pytest.mark.django_db
def test_client_create_client(client):
    url = reverse('clients')
    new_client_dict = {
            "name": "Matheus Kraieski",
            "email": "mathkraieski@gmail.com",
            "cpf": "1540620001",
            "cnpj": "00000000000000",
            "first_phone": "51994542807",
            "second_phone": "51993580435"
        }
    response = client.post(url, data=new_client_dict)
    new_client = Client.objects.get(cpf='1540620001')

    assert new_client.name == new_client_dict.get('name')
    assert new_client.email == new_client_dict.get('email')
    assert new_client.cpf == new_client_dict.get('cpf')
    assert new_client.cnpj == new_client_dict.get('cnpj')
    assert new_client.first_phone == new_client_dict.get('first_phone')
    assert new_client.second_phone == new_client_dict.get('second_phone')
    assert response.status_code == 201
