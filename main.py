from evidence import Evidence

def menu():
    options = [
        "Vytvořit pojištěného",
        "Zobrazit seznam pojištěných",
        "Najít pojištěného",
        "Odstranit pojištěného",
        "Upravit pojištěného",
        "Ukončit aplikaci"
    ]
    print("-------------")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print("-------------")


def main():
    evidence = Evidence()

    while True:
        menu()
        volba = input("Zadejte číslo možnosti: ")

        if volba == "1":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            vek = input("Zadejte věk: ")
            telefon = input("Zadejte telefonní číslo: ")
            evidence.vytvor_pojisteneho(jmeno, prijmeni, vek, telefon)
            print("Pojištěný byl vytvořen.")

        elif volba == "2":
            print("Seznam pojištěných:")
            evidence.zobraz_seznam_pojisteni()

        elif volba == "3":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            evidence.najdi_pojisteneho(jmeno, prijmeni)

        elif volba == "4":
            id = input("Zadejte ID pojištěného: ")
            evidence.odstran_pojisteneho(id)

        elif volba == "5":
            id = input("Zadejte ID pojištěného: ")
            jmeno = input("Zadejte nové jméno: ")
            prijmeni = input("Zadejte nové příjmení: ")
            vek = input("Zadejte nový věk: ")
            telefon = input("Zadejte nové telefonní číslo: ")
            evidence.edituj_pojisteneho(id, jmeno, prijmeni, vek, telefon)

        elif volba == "6":
            evidence.zavri_spojeni()
            break

        else:
            print("Neplatná volba. Zadejte číslo možnosti (1, 2, 3, 4, 5 nebo 6).")

if __name__ == "__main__":
    main()
