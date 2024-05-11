from datetime import datetime

#Definiálunk egy Szoba osztályt, amely tartalmazza a szoba számát és árát.
class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

#Az EgyagyasSzoba osztály az Szoba osztályból származik és beállítja az árat 10000-re.
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)

#A KetagyasSzoba osztály az Szoba osztályból származik és beállítja az árat 15000-re.
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)

#A Szalloda osztály létrehozása, amely tartalmazza a szálloda nevét és a szobákat.
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    #Új szoba hozzáadása a szállodához.
    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

#A Foglalas osztály definiálása, amely tartalmazza a foglalás szobáját és dátumát.
class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

#A FoglalasKezelo osztály létrehozása, amely kezeli a foglalásokat a szállodában.
class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    #Foglalás létrehozása egy adott szobára és dátumra.
    def foglalas(self, szobaszam, datum):
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                # Ellenőrzés, hogy a megadott szoba és dátumhoz van-e már foglalás
                if not self.ellenoriz_foglalast(szoba, datum):
                    return None
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return szoba.ar
        return None

    #Foglalás törlése az adott sorszám alapján.
    def lemondas(self, foglalas_sorszam):
        foglalas_index = foglalas_sorszam - 1
        if 0 <= foglalas_index < len(self.foglalasok):
            foglalas = self.foglalasok[foglalas_index]
            self.foglalasok.remove(foglalas)
            print("A foglalás sikeresen törölve.")
        else:
            print("Érvénytelen foglalás sorszám.")

    #A foglalások listázása.
    def listaz_foglalasok(self):
        for i, foglalas in enumerate(self.foglalasok):
            print(f"Foglalás {i+1}: Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum.strftime('%Y-%m-%d')}")

    #Ellenőrzi, hogy egy adott szobára és dátumra már van-e foglalás.
    def ellenoriz_foglalast(self, szoba, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum.date() == datum.date():
                return False
        return True

#Szálloda létrehozása és szobák hozzáadása.
def adatok_feltoltese():
    szalloda = Szalloda("Példa Szálloda")
    szalloda.uj_szoba(EgyagyasSzoba("101"))
    szalloda.uj_szoba(KetagyasSzoba("201"))
    szalloda.uj_szoba(KetagyasSzoba("202"))
    return szalloda

#Fő függvény, amely inicializálja a szállodát és a foglaláskezelőt, majd kezeli a felhasználói interakciót.
def main():
    szalloda = adatok_feltoltese()
    foglalas_kezelo = FoglalasKezelo(szalloda)

    #Példa foglalások hozzáadása
    foglalas_kezelo.foglalas("101", datetime(2024, 5, 15))
    foglalas_kezelo.foglalas("201", datetime(2024, 5, 17))
    foglalas_kezelo.foglalas("202", datetime(2024, 5, 19))
    foglalas_kezelo.foglalas("101", datetime(2024, 5, 20))
    foglalas_kezelo.foglalas("202", datetime(2024, 5, 21))

    #Felhasználói interakció kezelése
    while True:
        print("\nVálassz egy műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Művelet sorszáma: ")

        if valasztas == "1":
            szobaszam = input("Add meg a foglalni kívánt szoba számát: ")
            datum_str = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d")
                if datum >= datetime.now():
                    ar = foglalas_kezelo.foglalas(szobaszam, datum)
                    if ar:
                        print(f"A foglalás sikeres. Ár: {ar} Ft.")
                    else:
                        print("Nincs elérhető időpont a megadott szobához és dátumhoz.")
                else:
                    print("A foglalás csak jövőbeli dátumra lehetséges.")
            except ValueError:
                print("Érvénytelen dátum formátum.")
        elif valasztas == "2":
            foglalas_sorszam = int(input("Add meg a lemondani kívánt foglalás sorszámát: "))
            foglalas_kezelo.lemondas(foglalas_sorszam)
        elif valasztas == "3":
            print("Foglalások:")
            foglalas_kezelo.listaz_foglalasok()
        elif valasztas == "4":
            break
        else:
            print("Érvénytelen művelet.")

#Fő függvény meghívása
if __name__ == "__main__":
    main()

