def main():
    def liniowa(x, a, b):
        return a*x+b

    a = 2
    x = 3
    wynik = liniowa(x, a, 5)
    print(wynik)
    print(liniowa(x, a, 3))

if __name__ == "__main__":
    main()