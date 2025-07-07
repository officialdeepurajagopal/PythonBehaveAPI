@api @smoke
Feature: API Testing Example

@get_user
  Scenario: Get user data and verify first name
    Given I setup the API client
    When I set the headres
    When I send a GET request to "/api/users/1"
    Then I validate the response status code is 200
    Then I validate the response contains first name "George"

@get_users
  Scenario: Get user data and verify number of users
    Given I setup the API client
    When I set the headres
    When I send a GET request to "/api/users"
    Then I validate the response status code is 200
    Then I validate the number of users is 6
    Then I validate the list of users include "Eve"


@get_users
  Scenario: Validate list of users contain specific users
    Given I setup the API client
    When I set the headres
    When I send a GET request to "/api/users"
    Then I validate the response status code is 200
    Then I validate the list of users include "Eve"
