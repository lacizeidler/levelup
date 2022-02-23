from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from levelupapi.models import Game, Event, GameType


class EventTests(APITestCase):
    def setUp(self):
        """
        Create a new Event, collect the auth Token, and create a sample Game
        """

        # Define the URL path for registering a Gamer
        url = '/register'

        # Define the Gamer properties
        gamer = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }

        # Initiate POST request and capture the response
        response = self.client.post(url, gamer, format='json')

        # Store the TOKEN from the response data
        self.token = Token.objects.get(pk=response.data['token'])

        # Use the TOKEN to authenticate the requests
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Assert that the response status code is 201 (CREATED)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # SEED THE DATABASE WITH A GAMETYPE
        # This is necessary because the API does not
        # expose a /gametypes URL path for creating GameTypes

        # Create a new instance of a Game
        game = Game()
        game.title = "Clue"
        game.maker = "Milton Bradley"
        game.skill_level = 5
        game.number_of_players = 6
        game.game_type = GameType.objects.create(label="Board Game")

        # Save the Game to the testing database
        game.save()

    def test_create_event(self):
        """
        Ensure we can create (POST) a new Event.
        """

        # Define the URL path for creating a new Game
        url = "/events"

        # Define the Game properties
        event = {
            "description": "Super Fun Awesome Event",
            "date": "2022-05-28",
            "time": "05:30:28",
            "organizer": 1,
            "game": 1
        }

        # Initiate POST request and capture the response
        response = self.client.post(url, event, format='json')

        # Assert that the response status code is 201 (CREATED)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the values are correct
        self.assertEqual(response.data["organizer"]
                         ['user'], self.token.user_id)
        self.assertEqual(response.data["date"], event['date'])
        self.assertEqual(response.data["time"], event['time'])
        self.assertEqual(
            response.data["description"], event['description'])
        self.assertEqual(response.data["game"]
                         ['id'], event['game_id'])

    # def test_get_game(self):
    #     """
    #     Ensure we can GET an existing game.
    #     """

    #     # Create a new instance of Game
    #     game = Game()
    #     game.gamer_id = 1
    #     game.title = "Monopoly"
    #     game.maker = "Milton Bradley"
    #     game.skill_level = 5
    #     game.number_of_players = 4
    #     game.game_type_id = 1

    #     # Save the Game to the testing database
    #     game.save()

    #     # Define the URL path for getting a single Game
    #     url = f'/games/{game.id}'

    #     # Initiate GET request and capture the response
    #     response = self.client.get(url)

    #     # Assert that the response status code is 200 (OK)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     # Assert that the values are correct
    #     self.assertEqual(response.data["gamer"]['id'], game.gamer_id)
    #     self.assertEqual(response.data["title"], game.title)
    #     self.assertEqual(response.data["maker"], game.maker)
    #     self.assertEqual(response.data["skill_level"], game.skill_level)
    #     self.assertEqual(
    #         response.data["number_of_players"], game.number_of_players)
    #     self.assertEqual(response.data["game_type"]['id'], game.game_type_id)

    # def test_delete_game(self):
    #     """
    #     Ensure we can delete an existing game.
    #     """

    #     # Create a new instance of Game
    #     game = Game()
    #     game.gamer_id = 1
    #     game.title = "Sorry"
    #     game.maker = "Milton Bradley"
    #     game.skill_level = 5
    #     game.number_of_players = 4
    #     game.game_type_id = 1

    #     # Save the Game to the testing database
    #     game.save()

    #     # Define the URL path for deleting an existing Game
    #     url = f'/games/{game.id}'

    #     # Initiate DELETE request and capture the response
    #     response = self.client.delete(url)

    #     # Assert that the response status code is 204 (NO CONTENT)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #     # Initiate GET request and capture the response
    #     response = self.client.get(url)

    #     # Assert that the response status code is 404 (NOT FOUND)
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
