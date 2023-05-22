import sqlite3

class Pojisteny:
    def __init__(self, id, jmeno, prijmeni, vek, telefon):
        self.id = id
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"ID: {self.id}\nJméno: {self.jmeno}\nPříjmení: {self.prijmeni}\nVěk: {self.vek}\nTelefonní číslo: {self.telefon}\n"

class Evidence:
    def __init__(self):
        self.connection = sqlite3.connect('pojisteni.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS pojisteni
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            jmeno TEXT,
                            prijmeni TEXT,
                            vek INTEGER,
                            telefon TEXT)''')
        self.connection.commit()

    def vytvor_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        self.cursor.execute("INSERT INTO pojisteni (jmeno, prijmeni, vek, telefon) VALUES (?, ?, ?, ?)",
                            (jmeno, prijmeni, vek, telefon))
        self.connection.commit()

    def zobraz_seznam_pojisteni(self):
        self.cursor.execute("SELECT * FROM pojisteni")
        rows = self.cursor.fetchall()

        if len(rows) == 0:
            print("Nejsou žádní pojištění.")
        else:
            for row in rows:
                pojisteny = Pojisteny(row[0], row[1], row[2], row[3], row[4])
                print(pojisteny)

    def najdi_pojisteneho(self, jmeno, prijmeni):
        self.cursor.execute("SELECT * FROM pojisteni WHERE jmeno=? AND prijmeni=?", (jmeno, prijmeni))
        row = self.cursor.fetchone()

        if row is not None:
            pojisteny = Pojisteny(row[0], row[1], row[2], row[3], row[4])
            print(pojisteny)
        else:
            print("Pojištěný nenalezen.")

    def odstran_pojisteneho(self, id):
        self.cursor.execute("DELETE FROM pojisteni WHERE id=?", (id,))
        self.connection.commit()
        print("Pojištěný byl odstraněn.")

    def edituj_pojisteneho(self, id, jmeno, prijmeni, vek, telefon):
        self.cursor.execute("UPDATE pojisteni SET jmeno=?, prijmeni=?, vek=?, telefon=? WHERE id=?",
                            (jmeno, prijmeni, vek, telefon, id))
        self.connection.commit()
        print("Pojištěný byl upraven.")

    def zavri_spojeni(self):
        self.connection.close()
