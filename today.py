"""Today"""
def main():
    '''input'''
    strings = input()
    for i in strings:
        if i.isupper():
            num = 65- ord(i)+90
            print(chr(num), end='')
        elif i.islower():
            num = 97- ord(i)+122
            print(chr(num), end='')
        else:
            print(i, end='')
main()
