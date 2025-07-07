"Проверка статус-кодов"
from requests import Response

import json


class Checking():

    """Метод для проверки статус-кодов"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Success. Status code = " + str(response.status_code))
        else:
            print("FAIL. Status code = " + str(response.status_code))


    """Метод для проверки обязательных полей"""
    @staticmethod
    def check_json_token(response: Response, expected_values):
        token = json.loads(response.text)
        assert list(token) == expected_values
        print("Поля присутствуют")


    """Метод для проверки значений обязательных полей"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_values):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_values
        print(field_name + " success")
