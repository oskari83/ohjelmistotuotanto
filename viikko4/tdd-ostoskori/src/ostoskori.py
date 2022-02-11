from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._hinta = 0
        self._amountKorissa = 0
        self._kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self._amountKorissa

    def hinta(self):
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        prod = Ostos(lisattava)
        self._amountKorissa +=1
        if prod in self._kori:
            i = self._kori.index(prod)
            self._kori[i].muuta_lukumaaraa(1)
        else:
            self._kori.append(prod)
        self._hinta += lisattava.hinta()

    def poista_tuote(self, poistettava: Tuote):
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._kori
