class Uczen:
    def __init__(self, imie, nazwisko, nazwa_klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_klasy = nazwa_klasy

    def __repr__(self):
        return f"Uczen {self.imie} {self.nazwisko} z klasy: {self.nazwa_klasy}"


class Nauczyciel:
    def __init__(self, imie, nazwisko, nazwa_przedmiotu, klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_przedmiotu = nazwa_przedmiotu
        self.klasy = klasy

    def __repr__(self):
        return f"Nauczyciel {self.imie} {self.nazwisko} od {self.nazwa_przedmiotu} uczacy klasy: {self.klasy}"


class Wychowawca:
    def __init__(self, imie, nazwisko, nazwa_klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_klasy = nazwa_klasy

    def __repr__(self):
        return f"Nauczyciel {self.imie} {self.nazwisko} wychowawca klasy: {self.nazwa_klasy}"


uczniowie = [Uczen(imie="Michal", nazwisko="Kowal", nazwa_klasy="3C"),
             Uczen(imie="Marek", nazwisko='Wysoki', nazwa_klasy="3C"),
             Uczen(imie="Magda", nazwisko="Lewa", nazwa_klasy="3C")]
nauczyciele = [Nauczyciel(imie="Jacek", nazwisko="Laska", nazwa_przedmiotu="Chemia", klasy=["3C", "2A", "4B"]),
               Nauczyciel(imie="Jakub", nazwisko="Gutowski", nazwa_przedmiotu="WOS", klasy=["2C", "2A", "4B"]),
               Nauczyciel(imie="Szymon", nazwisko="Goniec", nazwa_przedmiotu="Historia", klasy=["3C", "1C"])]
wychowawcy = [Wychowawca(imie="Piotr", nazwisko="Klamka", nazwa_klasy="3C")]


def znajdz_uczniow_klasy(nazwa_klasy):
    uczniowie_klasy = []
    for uczen in uczniowie:
        if uczen.nazwa_klasy == nazwa_klasy:
            uczniowie_klasy.append(uczen)
    return uczniowie_klasy


def znajdz_wychowawce_klasy(nazwa_klasy):
    for wychowawca in wychowawcy:
        if wychowawca.nazwa_klasy == nazwa_klasy:
            return wychowawca


def wypisz_lekcje_ucznia(imie_ucznia, nazwisko_ucznia):
    lekcja_ucznia = {}
    for uczen in uczniowie:
        if uczen.imie == imie_ucznia and uczen.nazwisko == nazwisko_ucznia:
            for nauczyciel in nauczyciele:
                if uczen.nazwa_klasy in nauczyciel.klasy:
                    lekcja_ucznia[nauczyciel.nazwa_przedmiotu] = str(nauczyciel.imie + " " + nauczyciel.nazwisko)
    return lekcja_ucznia


def wypisz_klasy_nauczyciela(imie_nauczyciela, nazwisko_nauczyciela):
    for nauczyciel in nauczyciele:
        if nauczyciel.imie == imie_nauczyciela and nauczyciel.nazwisko == nazwisko_nauczyciela:
            return nauczyciel.klasy


def wypisz_uczniow_wychowawcy(imie_wychowawcy, nazwisko_wychowawcy):
    for wychowawca in wychowawcy:
        if wychowawca.imie == imie_wychowawcy and nazwisko_wychowawcy == nazwisko_wychowawcy:
            return znajdz_uczniow_klasy(wychowawca.nazwa_klasy)


koniec_utworz = False
koniec_zarzadzaj = False
koniec_programu = False
while not koniec_programu:
    print("---PROGRAM DO OBSLUGI BAZY SZKOLNEJ---")
    operacja = input("1. Utworz\n2. Zarzadzaj\n3. Koniec")
    if operacja == "1":  # Utworz
        while not koniec_utworz:
            utworz_obiekt = input("Kogo chcesz utworzyc ?:\nNauczyciel\nUczen\nWychowawca\nKoniec\n").capitalize()
            if utworz_obiekt == "Uczen":
                imie = input("Podaj imie ucznia:").capitalize()
                nazwisko = input("Podaj nazwisko ucznia:").capitalize()
                nazwa_klasy = input("Podaj klase ucznia:").upper()
                uczniowie.append(Uczen(imie=imie, nazwisko=nazwisko, nazwa_klasy=nazwa_klasy))

            elif utworz_obiekt == "Nauczyciel":
                klasy = []
                imie = input("Podaj imie nauczyciela:").capitalize()
                nazwisko = input("Podaj nazwisko nauczyciela:").capitalize()
                nazwa_przedmiotu = input("Podaj nazwe przedmiotu nauczyciela:").lower()
                while True:
                    klasa_prowadzona = input("Podaj nazwy klas, ktore nauczyciel prowadzi").upper()
                    if klasa_prowadzona == "":
                        break
                    else:
                        klasy.append(klasa_prowadzona)
                nauczyciele.append(Nauczyciel(imie, nazwisko, nazwa_przedmiotu, klasy))
            elif utworz_obiekt == "Wychowawca":
                imie = input("Podaj imie wychowawcy:").capitalize()
                nazwisko = input("Podaj nazwisko wychowawcy:").capitalize()
                nazwa_klasy = input("Podaj klase wychowawcy:").upper()
                wychowawcy.append(Wychowawca(imie=imie, nazwisko=nazwisko, nazwa_klasy=nazwa_klasy))
            elif utworz_obiekt == "Koniec":
                koniec_utworz = True
            else:
                print("Niepoprawne dane wejsciowe, sprobuj jeszcze raz")
    elif operacja == "2":  # Zarzadzaj
        while not koniec_zarzadzaj:
            typ_uzytkownika = input("Podaj typ uzytkownika:\nklasa\nuczen\nnauczyciel\nwychowawca\nkoniec\n").lower()
            if typ_uzytkownika == "klasa":
                nazwa_klasy = input("Podaj nazwe klasy np. 3C").upper()
                uczniowie_klasy = znajdz_uczniow_klasy(nazwa_klasy)
                wychowawca = znajdz_wychowawce_klasy(nazwa_klasy)
                print(uczniowie_klasy)
                print(wychowawca)
            elif typ_uzytkownika == "uczen":
                imie_ucznia = input("Podaj imie ucznia:").capitalize()
                nazwisko_ucznia = input("Podaj nazwisko ucznia:").capitalize()
                pokaz_lekcje = wypisz_lekcje_ucznia(imie_ucznia, nazwisko_ucznia)
                print(pokaz_lekcje)
            elif typ_uzytkownika == "nauczyciel":
                imie_nauczyciela = input("Podaj imie nauczyciela:").capitalize()
                nazwisko_nauczyciela = input("Podaj nazwisko nauczyciela:").capitalize()
                pokaz_klasy = wypisz_klasy_nauczyciela(imie_nauczyciela, nazwisko_nauczyciela)
                print(pokaz_klasy)
            elif typ_uzytkownika == "wychowawca":
                imie_wychowawcy = input("Podaj imie wychowawcy: ").capitalize()
                nazwisko_wychowawcy = input("Podaj nazwisko wychowawcy: ").capitalize()
                wypisz_uczniow = wypisz_uczniow_wychowawcy(imie_wychowawcy, nazwisko_wychowawcy)
                print(wypisz_uczniow)
            elif typ_uzytkownika == "koniec":
                koniec_zarzadzaj = True
            else:
                print("Niepoprawne dane wejsciowe")
    elif operacja == "3":  # Koniec
        koniec_programu = True
    else:
        print("Cos poszlo nie tak, wybierz:\n 1. Utworz\n 2. Zarzadzaj\n 3. Koniec")
