print('Program 2')

word2 = input('\nInput a string with digits: ')
sumOfDigits = 0

for character in word2:
    if "0" <= character <= "9":
        sumOfDigits += int(character)

print('Sum of digits: ', sumOfDigits)