import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikealla_numeroilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,'12345', '33333-44455', 5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_kahden_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikealla_numeroilla(self):
        # tehdään toteutus saldo-metodille
        def varasto_saldo2(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote2(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "vesi", 2)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo2
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote2

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,'12345', '33333-44455', 7)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_kahden_saman_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikealla_numeroilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,'12345', '33333-44455', 10)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_kahden_ostoksen_toinenloppu_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikealla_numeroilla(self):
        # tehdään toteutus saldo-metodille
        def varasto_saldo2(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote2(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "vesi", 0)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo2
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote2

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,'12345', '33333-44455',5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    def test_poista_kori_toimii(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,'12345', '33333-44455',0)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_tyhjää_tuotetta_ei_voi_lisata(self):
        def varasto_saldo2(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote2(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "vesi", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo2
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote2

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,'12345', '33333-44455',0)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista