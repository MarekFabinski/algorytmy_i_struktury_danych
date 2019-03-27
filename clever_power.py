def main():
    def power(podstawa, wykladnik):
        if wykladnik == 1:
            return podstawa
        if wykladnik == 0:
            return 1
        polowa = power(podstawa, wykladnik // 2)
        if wykladnik % 2 == 0:
            return polowa * polowa
        else:
            return polowa * polowa * podstawa

    print(power(2, 7))


if __name__ == "__main__":
    main()