from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, Or
from pino import Pino

class QueryBuilder:
    def __init__(self, pino=[]):
        self.query_objects = pino

    def playsIn(self, team):
        self.query_objects.append(PlaysIn(team))
        return QueryBuilder(self.query_objects)

    def hasAtLeast(self,val,atr):
        return QueryBuilder(self.query_objects.append(HasAtLeast(val,atr)))

    def hasFewerThan(self,val,atr):
        return QueryBuilder(self.query_objects.append(HasFewerThan(val,atr)))

    def build(self):
        print(self.query_objects)
        return And(self.query_objects)