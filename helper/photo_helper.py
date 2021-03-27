from helper.request_helper import RequestHelper
from helper import constants


class PhotoHelper:
    @staticmethod
    def get_a_photo(photo_id):
        endpoint = constants.GET_PHOTO_ENDPOINT.format(photo_id=photo_id)
        response = RequestHelper.send_get_request(endpoint)
        return response

    @staticmethod
    def like_a_photo(photo_id):
        endpoint = constants.LIKE_PHOTO_ENDPOINT.format(photo_id=photo_id)
        response = RequestHelper.send_post_request(endpoint)
        return response

    @staticmethod
    def unlike_a_photo(photo_id):
        endpoint = constants.UNLIKE_PHOTO_ENDPOINT.format(photo_id=photo_id)
        response = RequestHelper.send_delete_request(endpoint)
        return response


