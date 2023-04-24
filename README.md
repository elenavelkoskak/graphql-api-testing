# Description

The project is about testing the graphql API. 

The API has the following endpoints:
* POST /graphql: Accepts a GraphQL query or mutation and returns the corresponding
data.

API: http://graphql.org/swapi-graphql

# Feature 1: Basic API testing
Feature 1: Querying data
We want to ensure that the API correctly returns data when queried. You should write tests to verify
that:
* Basic queries return the expected data.
* Queries with arguments return the expected data.
* Queries with nested data return the expected data

# Feature 2: Mutating data

We want to ensure that the API correctly mutates data when requested. You should write tests to
verify that:
* Basic mutations work correctly.

# Feature 3: Error handling
We want to ensure that the API correctly handles errors. You should write tests to verify that:
* Queries with invalid fields return an error.



# Tools

In order to utilise this project you need to have the following installed locally:
* selenium
* requests
* unittest
* pytest

# Usage

* Command used for parallel execution: pytest -n [Number of cores]
* To run all test execute command: pytest