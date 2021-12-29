import json
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from django.urls import reverse


class LoginTestCase(APITestCase):
    def setUp(self):
        self.register_url = reverse("auth_register")
        self.login_url = reverse("token_obtain_pair")

        self.user_data = {
            "username": "user_teste",
            "password": "teste@user_teste",
            "password2": "teste@user_teste",
            "email": "teste_api@gmail.com",
            "first_name": "marcos paulo",
            "last_name": "barreto",
        }

        return super().setUp()

    def test_registration(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_different_passwords(self):
        response = self.client.post(
            self.register_url,
            {
                "username": "user_teste",
                "password": "teste@user_teste",
                "password2": "different_password",
                "email": "teste_api@gmail.com",
                "first_name": "marcos paulo",
                "last_name": "barreto",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_small_password(self):
        response = self.client.post(
            self.register_url,
            {
                "username": "user_teste",
                "password": "123",
                "password2": "123",
                "email": "teste_api@gmail.com",
                "first_name": "marcos paulo",
                "last_name": "barreto",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_no_data(self):
        response = self.client.post(self.register_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        response = self.client.post(self.register_url, self.user_data)

        response = self.client.post(
            self.login_url,
            {
                "username": self.user_data["username"],
                "password": self.user_data["password"],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_wrong_password(self):
        response = self.client.post(self.register_url, self.user_data)

        response = self.client.post(
            self.login_url,
            {
                "username": self.user_data["username"],
                "password": "wrong_password",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_wrong_username(self):
        response = self.client.post(self.register_url, self.user_data)

        response = self.client.post(
            self.login_url,
            {
                "username": "wrong_username",
                "password": self.user_data["password"],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class CandidatesTestCase(APITestCase):
    def setUp(self):
        self.candidate_url = "/api/candidates/manager/"

        self.candidate_data = {
            "name": "Marcos Paulo",
            "email": "marcosbra@gmail.com",
            "cpf": "52186536080",
            "age": 28,
            "salary_claim": "1250",
            "immediate_availability": True,
        }

        self.candidate_data_update = {
            "name": "Marcos",
            "email": "marcos@gmail.com",
            "age": 38,
            "salary_claim": "1250",
            "immediate_availability": False,
        }

        self.user = User.objects.create_user(username="teste", password="teste")
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_create_candidate(self):
        response = self.client.post(self.candidate_url, self.candidate_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_candidate_no_data(self):
        response = self.client.post(self.candidate_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_candidate_age_under_19(self):
        self.candidate_data["age"] = 18
        response = self.client.post(self.candidate_url, self.candidate_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_candidate_wrong_cpf(self):
        self.candidate_data["cpf"] = "04846175322"
        response = self.client.post(self.candidate_url, self.candidate_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_candidate_repeated_cpf_email(self):
        self.test_create_candidate()
        response = self.client.post(self.candidate_url, self.candidate_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_candidates(self):
        self.test_create_candidate()

        response = self.client.get(self.candidate_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_details_candidate(self):
        candidate_request = self.client.post(self.candidate_url, self.candidate_data)
        response = self.client.get(
            self.candidate_url + str(candidate_request.data["id"]) + "/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_details_candidate_wrong_id(self):
        candidate_request = self.client.post(self.candidate_url, self.candidate_data)
        response = self.client.get(
            self.candidate_url + str(candidate_request.data["id"] + 200) + "/"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_candidate(self):
        candidate_request = self.client.post(self.candidate_url, self.candidate_data)
        response = self.client.put(
            self.candidate_url + str(candidate_request.data["id"]) + "/",
            self.candidate_data_update,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_cpf_candidate(self):
        candidate_request = self.client.post(self.candidate_url, self.candidate_data)
        response = self.client.put(
            self.candidate_url + str(candidate_request.data["id"]) + "/",
            {"cpf": "04846175324"},
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_candidate(self):
        candidate_request = self.client.post(self.candidate_url, self.candidate_data)
        response = self.client.delete(
            self.candidate_url + str(candidate_request.data["id"]) + "/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_candidate_wrong_id(self):
        candidate_request = self.client.post(self.candidate_url, self.candidate_data)
        response = self.client.delete(
            self.candidate_url + str(candidate_request.data["id"] + 200) + "/"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
