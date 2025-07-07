from behave import given, when, then
from utils.api_client import APIClient
from utils.helpers import Helpers
import pdb

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

@then('I validate the response status code is {statuscode}')
def validateStatusCode(context, statuscode):
    assert context.response.status_code == int(statuscode)

@then('I validate the response contains first name "{firstName}"')
def validateFirstName(context, firstName):
    assert firstName == context.response.json()["data"]["first_name"]


