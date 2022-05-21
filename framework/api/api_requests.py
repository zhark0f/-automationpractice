import requests
from framework.logger.logger import Logger


logger = Logger()


def get(url: str, headers: dict = None):
    try:
        response = requests.get(url=url, headers=headers)
        logger.api(response=response)
        return response
    except ConnectionError as err:
        logger.error(msg=err)


def post(url: str, data: dict = None, json: dict = None, files=None, headers: dict = None):
    try:
        response = requests.post(url=url, data=data, json=json, files=files, headers=headers)
        logger.api(response=response)
        return response
    except ConnectionError as err:
        logger.error(msg=err)


def put(url: str, data: dict = None, json: dict = None, headers: dict = None, files: dict = None):
    try:
        response = requests.put(url=url, data=data, json=json, headers=headers, files=files)
        logger.api(response=response)
        return response
    except ConnectionError as err:
        logger.error(msg=err)


def delete(url: str, params: dict = None, headers: dict = None):
    try:
        response = requests.delete(url=url, params=params, headers=headers)
        logger.api(response=response)
        return response
    except ConnectionError as err:
        logger.error(msg=err)


def patch(url: str, data: dict = None, json: dict = None, files=None, headers: dict = None):
    try:
        response = requests.patch(url=url, data=data, json=json, files=files, headers=headers)
        logger.api(response=response)
        return response
    except ConnectionError as err:
        logger.error(msg=err)
