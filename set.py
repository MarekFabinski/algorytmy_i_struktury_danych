def main():
    empty_set = set()
    set1 = {1, 3, 5}
    print(empty_set)
    print(set1)

    print(1 in empty_set)
    print(1 in set1)

    print(1 not in empty_set)
    print(1 not in set1)

    empty_set.add(2)
    set1.add(2)
    print(empty_set)
    print(set1)

    empty_set.discard(2)
    set1.discard(2)
    print(empty_set)
    print(set1)

    print({1, 5, 8} | {1, 5, 9})    #suma
    print({1, 5, 8} - {1, 5, 9})    #różnica
    print({1, 5, 8} & {1, 5, 9})    #przecięcie

    print({1, 5}.issubset({1, 5, 9}))


if __name__ == "__main__":
    main()