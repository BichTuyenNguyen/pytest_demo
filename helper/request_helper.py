import requests
from config.env_setup import EnvSetup


class RequestHelper:

    @staticmethod
    def send_get_request(end_point):
        url = EnvSetup.API + end_point
        return requests.get(url, headers={'Authorization': 'Bearer ' + EnvSetup.TOKEN}, verify=False)

    @staticmethod
    def send_post_request(end_point, data=None):
        url = EnvSetup.API + end_point
        return requests.post(url, headers={'Authorization': 'Bearer ' + EnvSetup.TOKEN}, data=data, verify=False)

    @staticmethod
    def send_delete_request(end_point):
        url = EnvSetup.API + end_point
        return requests.delete(url, headers={'Authorization': 'Bearer ' + EnvSetup.TOKEN}, verify=False)
