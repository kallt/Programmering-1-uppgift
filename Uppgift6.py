def beräkna_genomsnittsålder():
    könen = {'kvinna': [], 'man': []}                                 #Skapar en dictionary som ska lagra åldrarna i två listor baserat på kön

    try:
        antal_personer = int(input("Ange antal personer: "))          # kodblock som be användaren om antalet personer och plocka upp möjliga felmeddelanden 
        if antal_personer < 0:
            raise ValueError("Antal personer måste vara högre än 0.") # kontrollerar att antalet personer är ett positivt heltal 
    except ValueError as e:
        print(f"Felaktig inmatning: {e}.")                            # Ska hantera/fånga upp fel inmatning för antalet personer
        return

    for i in range(antal_personer):                                   # En for loop som ska iterera igenom antalet personer som angets och dela upp de i kön
        while True:
            try:
                kön, ålder = input("Ange kön (kvinna/man) och ålder (separerade med mellanslag): ").strip().lower().split()    # Här ber jag användaren om kön och ålder
                ålder = int(ålder)
                if ålder < 0:
                    raise ValueError("Åldern måste vara högre än 0.")                                # Här kontrollerar jag att åldern är positiv och inte har ett värde på 0 eller mindre

                if kön in könen:                                      # Här kollar koden ifall könen som anges av användaren är ett utav könen i 'könen' dictoionary ('man' eller 'kvinna') och lägger till ålder i rätt lista baserat på kön
                    könen[kön].append(ålder)
                    break
                else:                                          
                    print("Felaktigt kön, försök igen.")              # Skriver ut ett meddelande ifall könet som angetts inte är bekant med något av könen i ''könen''
            except ValueError as e:                                   # Koden ska hantera ogiltig inmatning för kön och ålder
                print(f"Felaktig inmatning: {e}. Försök igen.")

    for kön, lista in könen.items():                                  # Här beräknar koden den genomsnittliga åldern för varje kön 
        if lista:
            print(f"Genomsnittsåldern för {kön}: {sum(lista) / len(lista):.2f}") # 3 * 20 = 60 / 3 = 20
        else:
            print(f"Ingen data för {kön}.")                           # Om en eller båda listorna är tomma så printar det ett meddelande för användaren

if __name__ == "__main__":
    beräkna_genomsnittsålder()