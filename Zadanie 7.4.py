class film:
    def __init__(self, tytul, rok_wydania, gatunek, liczba_odtworzen=0):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen
    def play(self):
        self.liczba_odtworzen += 1
    def inf(self):
        print(f"{self.Tytul} {self.Rok_wydania}")

class serial:
    def __init__(self, tytul, rok_wydania, gatunek, numer_odcinka, numer_sezonu, liczba_odtworzen=0):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.numer_sezonu = numer_sezonu
        self.numer_odcinka = numer_odcinka
        self.liczba_odtworzen = liczba_odtworzen
    def views(self,):
        self.liczba_odtworzen += 1
    def info(self):
        print(f"{self.Tytul} S{self.numer_sezonu}E{self.Numer_odcinka}")

    
