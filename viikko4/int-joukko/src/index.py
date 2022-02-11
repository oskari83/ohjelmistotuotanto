import unittest
from int_joukko import IntJoukko


def main():

    def tee_joukko(*luvut):
        joukko = IntJoukko()
        for luku in luvut:
            joukko.lisaa(luku)

        return joukko

    eka = tee_joukko(1, 2, 5, 6)
    print(eka)
    toka = tee_joukko(2, 3, 4)
    print(toka)

    tulos = IntJoukko.erotus(eka, toka)
    vastauksen_luvut = tulos.to_int_list()
    print(vastauksen_luvut)


if __name__ == "__main__":
    main()
