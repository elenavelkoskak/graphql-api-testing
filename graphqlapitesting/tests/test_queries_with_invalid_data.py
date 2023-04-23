import requests
import unittest

BASE_URL = "https://swapi-graphql.netlify.app/.netlify/functions/index"


class TestQueriesWithInvalidData(unittest.TestCase):
    def test_film_invalid_object(self):
        body = """
            query {
              film2(id: "ZmlsbXM6MQ==") {
                title
                }
            }
        """

        response = requests.post(url=BASE_URL, json={"query": body}, headers={"Content-Type":"application/json"})

        res = response.json()
        assert res["errors"][0]["message"] == "Cannot query field \"film2\" on type \"Root\". Did you mean \"film\" or \"allFilms\"?"

    def test_film_invalid_id_value(self):
        body = """
            query {
              film(id: "test==") {
                title
                }
            }
         """

        response = requests.post(url=BASE_URL, json={"query": body}, headers={"Content-Type": "application/json"})

        res = response.json()
        assert res["errors"][0]["message"] == "No entry in local cache for https://swapi.dev/api/films/��-/"

    def test_film_invalid_id(self):
        body = """
            query {
              film(id1: "ZmlsbXMmcmc6MQ==") {
                title
                }
            }
         """

        response = requests.post(url=BASE_URL, json={"query": body}, headers={"Content-Type": "application/json"})

        res = response.json()
        assert res["errors"][0]["message"] == "Unknown argument \"id1\" on field \"film\" of type \"Root\". Did you mean \"id\"?"

    def test_film_invalid_title(self):
        body = """
            query {
              film(id: "ZmlsbXM6MQ==") {
                title1
                }
            }
         """

        response = requests.post(url=BASE_URL, json={"query": body}, headers={"Content-Type": "application/json"})

        res = response.json()
        assert res["errors"][0]["message"] == "Cannot query field \"title1\" on type \"Film\". Did you mean \"title\"?"

    def test_invalid_query(self):
        body = """
             query {
                  test
            }
         """

        response = requests.post(url=BASE_URL, json={"query": body}, headers={"Content-Type": "application/json"})

        res = response.json()
        assert res["errors"][0]["message"] == "Cannot query field \"test\" on type \"Root\"."