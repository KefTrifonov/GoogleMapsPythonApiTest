import requests

from utils.logger import Logger

"""Список http методов"""

class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        Logger.write_log_request(url, method="GET")
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.write_log_response(result)
        return result

    @staticmethod
    def post(url, body):
        Logger.write_log_request(url, method="POST")
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.write_log_response(result)
        return result

    @staticmethod
    def put(url, body):
        Logger.write_log_request(url, method="PUT")
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.write_log_response(result)
        return result

    @staticmethod
    def delete(url, body):
        Logger.write_log_request(url, method="DELETE")
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.write_log_response(result)
        return result