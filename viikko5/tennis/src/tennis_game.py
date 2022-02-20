class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.point_term = {0:"Love",1:"Fifteen",2:"Thirty",3:"Forty"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            #if equal on points
            if self.player1_score in self.point_term:
                return self.point_term[self.player1_score] + "-All"
            else:
                return "Deuce"
        elif self.player1_score >= 4 or self.player2_score >= 4:
            #if either player could have won or is in a position to win
            return self.score_difference(self.player1_score,self.player2_score)   
        else:
            #normal play
            return self.point_term[self.player1_score] + "-" + self.point_term[self.player2_score]
    
    def score_difference(self, score1, score2):
        difference_for_player1 = score1-score2
        if difference_for_player1 == 1:
            return "Advantage player1"
        elif difference_for_player1 == -1:
            return "Advantage player2"
        elif difference_for_player1 >= 2:
            return "Win for player1"
        else:
            return "Win for player2"