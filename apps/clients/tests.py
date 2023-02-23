import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_client_status_code_200_ok(client):
    url = reverse('clients')
    response = client.get(url)
    assert response.status_code == 200

# def test_client_db_is_correct(client):
#     url = reverse('clients')
#     response = client.get(url)
#     assert response.json == [
# 	{
# 		"id": 1,
# 		"name": "Matheus Kraieski",
# 		"email": "mathkraieski@gmail.com",
# 		"cpf": "1540620001",
# 		"cnpj": null,
# 		"first_phone": "51994542807",
# 		"second_phone": null
# 	}
# ]
