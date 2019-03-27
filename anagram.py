def main():
    def anagram(word1, word2):
        n = len(word1)
        if n != len(word2):
            return False
        slownik1 = dict()
        slownik2 = dict()
        for i in range(n):
            if word1[i] in slownik1:
                slownik1[word1[i]] += 1
            else:
                slownik1[word1[i]] = 1
            if word2[i] in slownik2:
                slownik2[word2[i]] += 1
            else:
                slownik2[word2[i]] = 1
        return slownik1 == slownik2

    print(anagram('kajak', 'kkaaj'))


if __name__ == "__main__":
    main()