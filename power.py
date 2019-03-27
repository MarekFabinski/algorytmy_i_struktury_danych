def main():
    def power(podstawa, wykladnik):
        i = 1
        wynik = 1
        while i <= wykladnik:
            wynik *= podstawa
            i += 1
        return wynik
    print(power(3, 4))

    def power1(podstawa, wykladnik = 1):
        i = 1
        wynik = 1
        while i <= wykladnik:
            wynik *= podstawa
            i += 1
        return wynik
    print(power1(4))

    print(power(wykladnik = 5, podstawa = 4))


if __name__ == "__main__":
    main()