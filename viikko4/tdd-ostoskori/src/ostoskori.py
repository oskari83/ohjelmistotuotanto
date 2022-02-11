from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._hinta = 0
        self._amountKorissa = 0
        self._kori = []
        self._lisatytnimet = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self._amountKorissa

    def hinta(self):
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        prod = Ostos(lisattava)
        self._amountKorissa +=1
        if prod.tuotteen_nimi() in self._lisatytnimet:
            for i in range(len(self._kori)):
                if self._kori[i].tuotteen_nimi()==prod.tuotteen_nimi():
                    self._kori[i].muuta_lukumaaraa(1)
        else:
            self._kori.append(prod)
            self._lisatytnimet.append(prod.tuotteen_nimi())
        self._hinta += lisattava.hinta()

    def poista_tuote(self, poistettava: Tuote):    
        for i in range(len(self._kori)):
            if self._kori[i].tuotteen_nimi()==poistettava.nimi():
                if self._kori[i].lukumaara()==1:
                    self._kori.pop(i)
                    self._lisatytnimet.remove(poistettava.nimi())
                else:
                    self._kori[i].muuta_lukumaaraa(-1)
                self._amountKorissa -=1
                self._hinta -= poistettava.hinta()
        
    def tyhjenna(self):
        self._kori = []

    def ostokset(self):
        return self._kori
