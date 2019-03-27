def main():
    def if_palindrome(text):
        n = len(text)
        for i in range(len(text)//2):
            if text[i] != text[n-i-1]:
                return False
        return True
    print(if_palindrome('kajak'))

    def if_palindrome_python_version(text):
        return text == text[::-1]

    print(if_palindrome_python_version('kajak'))


if __name__ == "__main__":
    main()