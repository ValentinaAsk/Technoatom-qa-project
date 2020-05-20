import time
from tests.base_api import BaseCase
import pytest


class DataInvalid:
    data1 = {"username": 'invalid_email', "password": "invalid_email", "email": "invalid_email"}
    data2 = {"username": 'zero_email', "password": "zero_email", "email": ""}
    data3 = {"username": 'invalid_pas', "password": "", "email": "invalid_passowd@mail.ru"}
    data4 = {"username": 'invalid_email', "password": "invalid_email", "email": "invalid_email"}
    data5 = {"username": 'very_big_length_username', "password": "big_length_username_pas",
              "email": "big_length_username@mail.ru"}
    data6 = {"username": '', "password": "zero_length_username_pass", "email": "zero_length_username@mail.ru"}
    data7 = {"username": 's', "password": "small_length_username_pas", "email": "small_length_username@mail.ru"}


class DataExist:
    data1 = {"username": 'valentina', "password": "valentina", "email": "valentina@mail.ru"}
    data2 = {"username": 'valentina', "password": "new_pas", "email": "valentina@mail.ru"}
    data3 = {"username": 'valentina', "password": "valentina", "email": "new_mail@mail.ru"}
    data4 = {"username": 'valentina', "password": "new_pas", "email": "new_mail@mail.ru"}


class TestAPICreation(BaseCase):

    @pytest.mark.API
    def test_create_account_status_code(self, api_client, user_without_access_field):
        data = user_without_access_field
        response = api_client.create(data["username"], data["password"], data["email"])
        assert response.status_code == 201, "Response status code isn't 201"

    @pytest.mark.API #+++
    def test_create_account_save_in_db(self, api_client, user_without_access_field):
        data = user_without_access_field
        api_client.create(data["username"], data["password"], data["email"])

        response_data = api_client.get_user_from_db(data["username"])
        time.sleep(1)
        assert response_data["username"] == data["username"]
        assert response_data["password"] == data["password"]
        assert response_data["email"] == data["email"]
        assert response_data["access"] == 1

    @pytest.mark.API
    @pytest.mark.parametrize("data", [DataExist.data1, DataExist.data2, DataExist.data3, DataExist.data4])
    def test_existent_user(self, api_client, data):
        response = api_client.create(**data)
        assert response.status_code == 304

    @pytest.mark.API
    @pytest.mark.parametrize("data", [DataInvalid.data1, DataInvalid.data2, DataInvalid.data3, DataInvalid.data4, DataInvalid.data5, DataInvalid.data6, DataInvalid.data7])
    def test_invalid_data(self, api_client, data):

        response = api_client.create(**data)
        api_client.delete_user_from_db(data["username"])
        assert response.status_code == 400
    #
    # @pytest.mark.API
    # def test_invalid_name_zero_length(self, api_client):
    #
    #     response = api_client.create(**data)
    #     assert response.status_code == 400
    #
    # @pytest.mark.API
    # def test_invalid_name_big_length(self, api_client):
    #
    #     response = api_client.create(**data)
    #     assert response.status_code == 400
    #
    # @pytest.mark.API
    # def test_invalid_password(self, api_client):
    #
    #     response = api_client.create(**data)
    #     assert response.status_code == 400
    #
    # @pytest.mark.API
    # def test_invalid_email(self, api_client):
    #
    #     response = api_client.create(**data)
    #     assert response.status_code == 400
    #
    # @pytest.mark.API
    # def test_invalid_zero_email(self, api_client):
    #
    #     response = api_client.create(**data)
    #     assert response.status_code == 400


