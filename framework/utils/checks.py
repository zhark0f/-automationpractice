from typing import Union
import requests
from framework.utils.asserts import assert_equal
from assertpy import assert_that


class CommonCheckers:

    # Status code checkers

    @staticmethod
    def check_status_code(response: requests.Response, expected_code: int):
        """
        Contains checks that are not related to a specific microservice or business entity.
        ! Accepts an object of the Response wrapper class, not an object of the requests library.

        :param response: requests.Response
        :param expected_code: status code
        """
        error_message = f"Actual status code '{response.status_code}' not equal expected status code '{expected_code}'"
        assert_equal(left_part=response.status_code, right_part=expected_code, message=error_message)

    @staticmethod
    def check_status_code_not_equal(response: requests.Response, expected_code: int):
        assertion_message = f"Incorrect status code: {response.status_code}'"
        assert response.status_code != expected_code, f'{assertion_message}: {response.status_code}'

    @staticmethod
    def check_multiple_status_codes(response: requests.Response, expected_status_codes: list):
        assert response.status_code in expected_status_codes, "Incorrect status code"

    def check_status_code_200(self, response):
        self.check_status_code(response=response, expected_code=200)

    def check_status_code_201(self, response):
        self.check_status_code(response=response, expected_code=201)

    def check_status_code_400(self, response):
        self.check_status_code(response=response, expected_code=400)

    def check_status_code_401(self, response):
        self.check_status_code(response=response, expected_code=401)

    def check_status_code_403(self, response):
        self.check_status_code(response=response, expected_code=403)

    def check_status_code_404(self, response):
        self.check_status_code(response=response, expected_code=404)

    def check_status_code_not_404(self, response):
        self.check_status_code_not_equal(response=response, expected_code=404)

    @staticmethod
    def check_field_exists(field, assertion_message='The specified field does not exist'):
        assert field is not None, assertion_message
        return field

    @staticmethod
    def check_field_not_exists(field, assertion_message='The specified field exists, but should not'):
        assert field is None, assertion_message

    @staticmethod
    def check_field_equals(field, expected_value, assertion_message='Invalid field value'):
        assert field == expected_value, assertion_message

    @staticmethod
    def check_field_not_equals(field, expected_value, assertion_message='Invalid field value'):
        assert field != expected_value, assertion_message

    def check_field_exists_and_equals(self, field, expected_value,
                                      assertion_exists_message='The specified field does not exist',
                                      assertion_equals_message='Invalid field value'):
        self.check_field_exists(field, assertion_exists_message)
        self.check_field_equals(field, expected_value, assertion_equals_message)

    @staticmethod
    def check_field_is_less_or_equals(field, expected_value, assertion_message='Invalid field value'):
        assert field <= expected_value, assertion_message

    @staticmethod
    def check_not_empty_iterable(iterable,
                                 assertion_message='An empty response was received (an empty iterable object)'):
        assert len(iterable) != 0, assertion_message

    @staticmethod
    def check_empty_iterable(iterable, assertion_message='Non-empty iterable object'):
        assert len(iterable) == 0, assertion_message

    @staticmethod
    def check_json_exists(response: requests.Response):
        response_json = response.json()
        assert response_json is not None, "An empty response was received"
        return response_json

    def code_ok_not_empty_json_exists(self, response: requests.Response):
        self.check_status_code_200(response)
        self.check_json_exists(response)
        self.check_not_empty_iterable(response.json())

    @staticmethod
    def check_field_equals_soft(
        field: Union[str, int], expected_value: Union[str, int],
            assertion_message: str = "Invalid field value"):
        assert_that(field).described_as(assertion_message).is_equal_to(expected_value)

    @staticmethod
    def check_field_not_equals_soft(
        field: Union[str, int], expected_value: Union[str, int],
            assertion_message: str = "Invalid field value"):
        assert_that(field).described_as(assertion_message).is_equal_to(expected_value)
