from utils.api import GoogleMapsApi

from utils import checking

"""Создание, изменение и удаление локации"""

class TestCreateNewPlace():

    def test_create_new_place(self):

        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        checking.Checking.check_status_code(result_post, 200)
        checking.Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        checking.Checking.check_json_value(result_post, 'status', 'OK')

        print("Метод GET POST")
        result_get = GoogleMapsApi.get_location(place_id)
        checking.Checking.check_status_code(result_get, 200)
        checking.Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        checking.Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("Метод PUT")
        result_put = GoogleMapsApi.put_location(place_id)
        checking.Checking.check_status_code(result_put, 200)
        checking.Checking.check_json_token(result_put, ['msg'])
        checking.Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET PUT")
        result_get = GoogleMapsApi.get_location(place_id)
        checking.Checking.check_status_code(result_get, 200)
        checking.Checking.check_json_token(result_get,
                                           ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                            'website', 'language'])
        checking.Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_location(place_id)
        checking.Checking.check_status_code(result_delete, 200)
        checking.Checking.check_json_token(result_delete, ['status'])
        checking.Checking.check_json_value(result_delete, 'status', 'OK')

        print("Метод GET DELETE")
        result_get = GoogleMapsApi.get_location(place_id)
        checking.Checking.check_status_code(result_get, 404)
        checking.Checking.check_json_token(result_get, ['msg'])
        checking.Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")

        print("Test finished successfully")
