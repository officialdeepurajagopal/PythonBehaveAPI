from behave import given, when, then
from utils.api_client import APIClient
from utils.helpers import Helpers
import pdb
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@given('I setup the API client')
def setupClient(context):
    context.client = APIClient()
    context.helper = Helpers();
    
@when('I set the headres')
def setupHeaders(context):
    headers = context.helper.getHeaders()
    context.client.set_headers(headers)

@when('I send a GET request to "{endpoint}"')
def sendGetRequest(context, endpoint):
    context.response = context.client.get(endpoint)
    # logging.info(f"Response Received: {context.response.json()}")

@then('I validate the response status code is {statuscode}')
def validateStatusCode(context, statuscode):
    assert context.response.status_code == int(statuscode)

@then('I validate the response contains first name "{firstName}"')
def validateFirstName(context, firstName):
    assert firstName == context.response.json()["data"]["first_name"]


@then('I validate the number of users is {count}')
def validateNumberOfUsers(context, count):
    user_list = context.response.json()["data"]
    assert len(user_list) == int(count)

@then('I validate the list of users include "{name}"')
def validateNumberOfUsers(context, name):
    user_list = context.response.json()["data"]
    found = False
    for user in user_list:
        if isinstance(user, dict) and user.get("first_name") == name:
            found = True
            assert found

    
    
    