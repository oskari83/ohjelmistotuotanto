import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_toimii(self):
        self.assertEqual(str(self.statistics.search("Sem")), "Semenko EDM 4 + 12 = 16")
    
    def test_search_palauttaa_none(self):
        self.assertEqual(str(self.statistics.search("Selanne")), "None")

    def test_team_toimii(self):
        self.assertEqual(str(self.statistics.team("DET")[0]), "Yzerman DET 42 + 56 = 98")

    def test_top_scorers_toimii(self):
        self.assertEqual(str(self.statistics.top_scorers(4)[2]), "Yzerman DET 42 + 56 = 98")