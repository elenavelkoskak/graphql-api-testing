import requests
import unittest

BASE_URL = "https://swapi-graphql.netlify.app/.netlify/functions/index"


class TestQueriesWithNestedData(unittest.TestCase):

    def test_film_titles(self):
        body = """
                query {
                    person(id: "cGVvcGxlOjE=") {
                         name,
                         filmConnection{
                                films{
                                    title
                                }
                            }
                        }
                }
        """
        films = ["A New Hope", "The Empire Strikes Back", "Return of the Jedi", "Revenge of the Sith"]

        response = requests.post(url=BASE_URL, json={"query": body}, headers={"Content-Type": "application/json"})
        response = response.json()

        result_films = response["data"]["person"]["filmConnection"]["films"]
        result_film_names = []
        for film in result_films:
            name = film["title"]
            result_film_names.append(name)
        assert result_film_names == films

    def test_planets_titles(self):
        body = """
             query {
                film(id: "ZmlsbXM6Mg==") {
                     title,
                     planetConnection{
                            planets{
                                name
                            }
                        }
                    }
            }
        """
        planets = ["Hoth", "Dagobah", "Bespin", "Ord Mantell"]

        response = requests.post(url=BASE_URL, json={"query": body}, headers={"Content-Type": "application/json"})
        response = response.json()

        result_planets = response["data"]["film"]["planetConnection"]["planets"]
        result_planets_names = []
        for planet in result_planets:
            name = planet["name"]
            result_planets_names.append(name)
        assert result_planets_names == planets

    def test_all_planets_films(self):
        body = """
            query {
              allPlanets{
                      planets{name, filmConnection{films{title}}}
                }
            }
        """
        correct_data = {'Tatooine': 5, 'Alderaan': 2, 'Yavin IV': 1, 'Hoth': 1, 'Dagobah': 3, 'Bespin': 1, 'Endor': 1, 'Naboo': 4, 'Coruscant': 4, 'Kamino': 1, 'Geonosis': 1, 'Utapau': 1, 'Mustafar': 1, 'Kashyyyk': 1, 'Polis Massa': 1, 'Mygeeto': 1, 'Felucia': 1, 'Cato Neimoidia': 1, 'Saleucami': 1, 'Ord Mantell': 1}

        response = requests.post(url=BASE_URL, json={"query": body}, headers={"Content-Type": "application/json"})
        response = response.json()

        result_planets = response["data"]["allPlanets"]["planets"]

        data = {}
        for planet in result_planets:
            name = planet["name"]
            all_films = planet["filmConnection"]["films"]
            if all_films:
                data[name] = len(all_films)

        assert data == correct_data

        

