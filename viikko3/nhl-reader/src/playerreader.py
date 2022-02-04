import requests
from player import Player

class PlayerReader:
    def __init__(self,address):
        self.address = address
    
    def get_players(self):
        response = requests.get(self.address).json()
        players = []
        for player_dict in response:
            pl = Player(player_dict['name'],player_dict['goals'],player_dict['assists'],player_dict['team'],player_dict['nationality'])
            players.append(pl)
        return players