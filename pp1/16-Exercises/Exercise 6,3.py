def count(s, l):
    string = str(s)
    letter = str(l)
    counter = 0
    for character in string:
        if character == letter:
            counter = counter + 1
        print(counter)
input_letter = input('Enter a letter: ')
count('banana', input_letter)