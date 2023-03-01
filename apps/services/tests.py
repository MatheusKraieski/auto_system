import pytest
from django.urls import reverse

from apps.services.models import Service


@pytest.mark.django_db
def test_car_status_code_200_ok(client):
    response = client.get(reverse('services'))
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.django_db
def test_car_db_is_correct(client):
    Service.objects.create(
        ref_code="Face",
        client_id="Chery",
        car_id="IRD6051",
        description="2011",
        observation="188898",
    )

    response = client.get(reverse('cars'))
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Face",
            "brand": "Chery",
            "plate": "IRD6051",
            "year": 2011,
            "km": "188898",
            "color": "Silver"
        }
    ]


@pytest.mark.django_db
def test_car_create_car(client):
    url = reverse('cars')
    new_car_dict =  {
            "name": "Face",
            "brand": "Chery",
            "plate": "IRD6051",
            "year": 2011.0,
            "km": "188898",
            "color": "Silver"
        }
    response = client.post(url, data=new_car_dict)
    new_client = Car.objects.get(plate='IRD6051')

    assert new_client.name == new_car_dict.get('name')
    assert new_client.brand == new_car_dict.get('brand')
    assert new_client.plate == new_car_dict.get('plate')
    assert new_client.year == new_car_dict.get('year')
    assert new_client.km == new_car_dict.get('km')
    assert new_client.color == new_car_dict.get('color')
    assert response.status_code == 201
