from apps.clients.models import Client

from django.db import transaction


class ClientSerializer:
    def add_client(self, request):
        try:
            Client.objects.create(
                name=request.data.get('name'),
                email=request.data.get('email'),
                cpf=request.data.get("cpf"),
                cnpj=request.data.get('cnpj'),
                first_phone=request.data.get('first_phone'),
                second_phone=request.data.get('second_phone'),
            )

            return {'detail': 'Cliente created successfully.'}, 201
        except Exception as e:
            print(e)
            return {'detail': 'Cliente não pode ser criado.'}, 400

    def get_all_clients(self, clients):
        client_list_dict = []

        for client in clients:
            client_dict = self.build_client_dict(client)
            client_list_dict.append(client_dict)

        return client_list_dict, 200

    def build_client_dict(self, client):
        client_dict = {
            "name": client.name,
            "email": client.email,
            "cpf": client.cpf,
            "cnpj": client.cnpj,
            "first_phone": client.first_phone,
            "second_phone": client.second_phone
        }
        return client_dict
    
    def update_client(self, client, request):
        try:
            with transaction.atomic():
                client.name = request.data.get("name", client.name)
                client.email = request.data.get("email", client.email)
                client.cpf = request.data.get("cpf", client.cpf)  # noqa: E501
                client.cnpj = float(request.data.get("cnpj", client.cnpj))  # noqa: E501
                client.first_phone = float(request.data.get("first_phone", client.first_phone))  # noqa: E501
                client.color = request.data.get("second_phone", client.second_phone)  # noqa: E501

                client.save()
                return {"detail": "client was updated successfully."}, 201
        except Exception as e:
            print(e)
            return {"error": "client could not be changed."}, 400

    def delete_client(self, client, request):
        try:
            if transaction.atomic():
                client.delete()
            return {"detail": "Client was deleted successfully"}, 201
        except Exception as err:
            print(err)
            return {"error": "Client could not be deleted"}, 400