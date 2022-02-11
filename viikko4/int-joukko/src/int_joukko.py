KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti
        self.pointer = 0

    def kuuluu(self, n):
        for i in range(0, len(self.ljono)):
            if n == self.ljono[i]:
                return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.pointer] = n
            self.pointer += 1

            if self.pointer % len(self.ljono) == 0:
                self.kasvata()
            return True
        return False

    def kasvata(self):
        taulukko_old = self.ljono
        self.kopioi_taulukko(self.ljono, taulukko_old)
        self.ljono = [0] * (self.pointer + self.kasvatuskoko)
        self.kopioi_taulukko(taulukko_old, self.ljono)

    def poista(self, n):
        for i in range(0, len(self.ljono)):
            if n == self.ljono[i]:
                self.ljono[i] = 0
                self.siirraAlkioitaVasemmalle(i)
                return True
        return False

    def siirraAlkioitaVasemmalle(self,kohta):
        for j in range(kohta, len(self.ljono)-1):
            apu = self.ljono[j]
            self.ljono[j] = self.ljono[j + 1]
            self.ljono[j + 1] = apu
        self.pointer -=1

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.pointer

    def to_int_list(self):
        taulu = [0] * self.pointer
        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]
        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        tulostus = "{"
        for i in range(len(self.ljono)):
            if self.ljono[i]!=0:
                tulostus += str(self.ljono[i])
                if i!= self.pointer-1:
                    tulostus += ", "
        return tulostus + "}"
    #muutos1
