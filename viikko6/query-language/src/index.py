from statistics import Statistics
from player_reader import PlayerReader
from queryBuilder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = (
        query
            .playsIn("NYR")
            .playsIn("PHI")
            .build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
