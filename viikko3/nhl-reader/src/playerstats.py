from player import Player
class PlayerStats:
    def __init__(self,reader):
        self.reader = reader

    def pistejarjestus(self,p:Player):
        return p.points

    def top_scorers_by_nationality(self,nationality:str):
        allPlayers = self.reader.get_players()
        nationalPlayers = []
        for pla in allPlayers:
            if pla.nationality==nationality:
                nationalPlayers.append(pla)
        nationalPlayers.sort(key=self.pistejarjestus,reverse=True)
        return nationalPlayers
