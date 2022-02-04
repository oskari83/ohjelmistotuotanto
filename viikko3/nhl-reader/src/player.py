class Player:
    def __init__(self, name,goals, assists, team, nat):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.points = goals+assists
        self.team = team
        self.nationality = nat
    
    def __str__(self):
        return f"{self.name:25}{self.team:6} {str(self.goals):>2} + {str(self.assists):>2} = {str(self.points):2}"
