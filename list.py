def main():
    list1 = [1, True, 'Dog']
    print(list1)
    print(len(list1))

    list1.append(2.5+5.9j)
    print(list1)

    list1.extend([96, 97, 98])
    print(list1)

    print(list1 + [3, 4, 5])
    print(list1)

    print([1, 2, 3] * 3)
    print(list1 * 3)

    print(list1[4])
    print(list1[-1])

    list1[1] = False
    print(list1)

    print(list1[2:5])

    list1[0:2] = [1, 2, 3, 4, 5]
    print(list1)
    print(len(list1))

    list1.insert(2, 'New_element')
    print(list1)

    del list1[5]
    print(list1)

    numbers = [1, 7, 2, 9, 5, 19, 22, 3]
    #numbers.sort()
    numbers.reverse()
    print(numbers)

    text = "My new car"
    print(text[0])
    print(text[0:2])
    print(len(text))

    print('First row\nSecond row')
    print(r'First row\nSecond row')

    variable = 5
    text1 = f'Variable value is {variable}'
    print(text1)

    manyRows = """First row
    Second row
    Third Row"""
    print(manyRows)

    print('a' < 'b')

    text2 = 'my new car'
    print(text2.upper())

    text3 = 'My New Car'
    print(text3.lower())

    text4 = '   \n\t Dog    \n '
    print(text4.strip())

    text5 = 'A word, another word, and another word'
    print(text5.count('word'))
    text5 = text5.replace('word', 'cat')
    print(text5)

    listOfWords = ['my', 'new', 'car']
    print(listOfWords)
    print(len(listOfWords))
    print(" ".join(listOfWords))
    print(len(listOfWords))

    text6 = 'My new car'
    print(text6.split(" "))



if __name__ == "__main__":
    main()
