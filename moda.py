def moda(lista):
    zliczenia = dict()
    for i in range(len(lista)):
        if lista[i] in zliczenia:
            zliczenia[lista[i]] += 1
        else:
            zliczenia[lista[i]] = 1
    maks = -1
    liczba_maks = -1
    for (co, ile) in zliczenia.items():
        if ile > maks:
            liczba_maks = co
            maks = ile
    return liczba_maks