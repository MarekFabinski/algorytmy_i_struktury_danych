def main():
    baza_danych_Polaków = {'48513298751' : ['Jan', 'Kowalski', 24],
                           '64975436978' : ['Ania', 'Nowak', 18],
                           '95236759789' : ['Adam', 'Mickiewicz', 220]}
    print(baza_danych_Polaków)

    print('64975436978' in baza_danych_Polaków)
    print('57596248626' not in baza_danych_Polaków)
    print(baza_danych_Polaków['64975436978'])
    print(baza_danych_Polaków.get('64975436978', 'nie istnieje'))
    print(baza_danych_Polaków.get('78612368239', 'nie istnieje'))

    baza_danych_Polaków['84523648955'] = ['Magda', 'Koper', 31]
    print(baza_danych_Polaków)

    del baza_danych_Polaków['84523648955']
    print(baza_danych_Polaków)

    for klucz in baza_danych_Polaków.keys():
        print(klucz)

    for wartosc in baza_danych_Polaków.values():
        print(wartosc)

    for klucz, wartosc in baza_danych_Polaków.items():
        print(klucz)
        print(wartosc)
        print('----')


if __name__ == "__main__":
    main()