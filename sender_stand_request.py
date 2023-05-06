import configuration
import requests
import data


def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=data.user_body,
                         headers=data.headers)


response = post_new_user()
print(response.status_code)
print(response.json())