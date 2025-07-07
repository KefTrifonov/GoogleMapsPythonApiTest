import datetime
import os

class Logger():
    file_name = f'logs/log' + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + '.log'


    @classmethod
    def write_log_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as log_file:
            log_file.write(data)

    @classmethod
    def write_log_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_write_log = f'\n------\n'
        data_to_write_log += f'Test: "{test_name}\n"'
        data_to_write_log += f'Time: {str(datetime.datetime.now())}\n'
        data_to_write_log += f'Requests method: {method}\n'
        data_to_write_log += f'Requests URL: {url}\n'
        data_to_write_log += '\n'

        cls.write_log_file(data_to_write_log)

    @classmethod
    def write_log_response(cls, result):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_write_log = f'Response code: {result.status_code}\n'
        data_to_write_log += f'Response text: {result.text}\n'
        data_to_write_log += f'Response headers: {headers_as_dict}\n'
        data_to_write_log += f'Response cookies: {cookies_as_dict}\n'
        data_to_write_log += f'\n------\n'

        with open(cls.file_name, 'a') as log_file:
            log_file.write(data_to_write_log)
