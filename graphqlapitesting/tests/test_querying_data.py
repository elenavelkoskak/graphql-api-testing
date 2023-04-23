import requests
import unittest

BASE_URL = "https://swapi-graphql.netlify.app/.netlify/functions/index"


class TestBasicQuery(unittest.TestCase):
    def test_all_films(self):
        body = '{"query":"{allFilms {totalCount}}"}'

        response = requests.post(url=BASE_URL, data=body, headers={"Content-Type":"application/json"})

        res = response.json()
        assert res["data"]["allFilms"]["totalCount"] == 6

    def test_all_people(self):
        body = '{"query":"{allPeople {totalCount}}"}'

        response = requests.post(url=BASE_URL, data=body, headers={"Content-Type": "application/json"})

        people = response.json()
        assert people["data"]["allPeople"]["totalCount"] == 82

    def test_all_planets(self):
        body = '{"query":"{allPlanets {totalCount}}"}'

        response = requests.post(url=BASE_URL, data=body, headers={"Content-Type": "application/json"})

        planets = response.json()
        assert planets["data"]["allPlanets"]["totalCount"] == 60

    def test_all_species(self):
        body = '{"query":"{allSpecies {totalCount}}"}'

        response = requests.post(url=BASE_URL, data=body, headers={"Content-Type": "application/json"})

        species = response.json()
        assert species["data"]["allSpecies"]["totalCount"] == 37

    def test_all_vehicles(self):
        body = '{"query":"{allVehicles {totalCount}}"}'

        response = requests.post(url=BASE_URL, data=body, headers={"Content-Type": "application/json"})

        vehhicles = response.json()
        assert vehhicles["data"]["allVehicles"]["totalCount"] == 39

    def test_all_starships(self):
        body = '{"query":"{allStarships {totalCount}}"}'

        response = requests.post(url=BASE_URL, data=body, headers={"Content-Type": "application/json"})

        starships = response.json()
        assert starships["data"]["allStarships"]["totalCount"] == 36
