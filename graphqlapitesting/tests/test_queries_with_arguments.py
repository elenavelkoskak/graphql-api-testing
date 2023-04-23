import requests
import unittest

BASE_URL = "https://swapi-graphql.netlify.app/.netlify/functions/index"


class TestQueriesWithArguments(unittest.TestCase):
    def test_film_id(self):
        body = """
            query {
              film(id: "ZmlsbXM6MQ==") {
                title
                }
            }
        """

        response = requests.post(url=BASE_URL, json={"query": body}, headers={"Content-Type":"application/json"})

        res = response.json()
        assert res["data"]["film"]["title"] == "A New Hope"

    def test_people_id(self):
        body = """
            query {
              person(id: "cGVvcGxlOjE=") {
                 name
                }
            }
        """

        response = requests.post(url=BASE_URL, json={"query": body}, headers={"Content-Type": "application/json"})

        person_name = response.json()
        assert person_name["data"]["person"]["name"] == "Luke Skywalker"

    def test_planet_id(self):
        body = """
            query {
              planet(id: "cGxhbmV0czo1") {
                 name
                }
            }
           """

        response = requests.post(url=BASE_URL, json={"query": body}, headers={"Content-Type": "application/json"})

        planet_name = response.json()
        assert planet_name["data"]["planet"]["name"] == "Dagobah"

    def test_species_id(self):
        body = """
            query {
              species(id: "c3BlY2llczo2") {
                 name
                }
            }
             """

        response = requests.post(url=BASE_URL, json={"query": body}, headers={"Content-Type": "application/json"})

        planet_name = response.json()
        assert planet_name["data"]["species"]["name"] == "Yoda's species"

    def test_vehicle_id(self):
        body = """
            query {
              vehicle(id: "dmVoaWNsZXM6MTQ=") {
                 name
                }
            }
                """

        response = requests.post(url=BASE_URL, json={"query": body}, headers={"Content-Type": "application/json"})

        planet_name = response.json()
        assert planet_name["data"]["vehicle"]["name"] == "Snowspeeder"