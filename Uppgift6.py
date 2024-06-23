def beräkna_genomsnittsålder():
    könen = {'kvinna': [], 'man': []}

    try:
        antal_personer = int(input("Ange antal personer: "))
        if antal_personer < 0:
            raise ValueError("Antal personer måste vara högre än 0.")
    except ValueError as e:
        print(f"Felaktig inmatning: {e}.")
        return

    for i in range(antal_personer):
        while True:
            try:
                kön, ålder = input("Ange kön (kvinna/man) och ålder (separerade med mellanslag): ").strip().lower().split()
                ålder = int(ålder)
                if ålder < 0:
                    raise ValueError("Åldern måste vara högre än 0.")

                if kön in könen:
                    könen[kön].append(ålder)
                    break
                else:
                    print("Felaktigt kön, försök igen.")
            except ValueError as e:
                print(f"Felaktig inmatning: {e}. Försök igen.")

    for kön, lista in könen.items():
        if lista:
            print(f"Genomsnittsåldern för {kön}: {sum(lista) / len(lista):.2f}") # 3 * 20 = 60 / 3 = 20
        else:
            print(f"Ingen data för {kön}.")

if __name__ == "__main__":
    beräkna_genomsnittsålder()