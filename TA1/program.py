print('Program 1') 

word = input('\nInput a string: ')
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
vowel_count = 0
consonant_count = 0
space_count = word.count(" ")
 
for character in word:
    if character in vowels:
        vowel_count += 1
    elif character.isalpha():
        consonant_count += 1
        
print('Number of vowels: ', vowel_count)
print('Number of consonant: ', consonant_count)
print('Number of spaces: ', space_count)

print('\nProgram 2') 

word2 = input('\nInput a string with digits: ')
sumOfDigits = 0

for character in word2:
    if character.isdigit():
        sumOfDigits += int(character)

print('Sum of digits: ', sumOfDigits)

print('\nProgram 3') 

print('\nA.')
rows = 5  # Number of rows

for i in range(1, rows + 1):  # Loop for rows
    for j in range(rows - i):  # Loop for spaces
        print(" ", end="")  # Print spaces
    for k in range(1, i + 1):  # Loop for numbers
        print(k, end="")  # Print numbers
    print()
    
print('\nB.')
n = 1  # Start with the first integer which is 1

while n <= 5:  # Loop hanggang umabot 5
    count = 1  # Start from the first count sa row
    
    # Print n amount of integers in each row
    while count <= n:
        print(n, end="")  # Print n integers in a row
        count += 1  # Increment count
        
    print()  # Move to the next line for the next row
    n += 2  # Increase n by 2 (to get the next odd number)

n = 6 # labas na ng loop kaya print panibago
count = 1
while count <= n:
    print(n, end="")
    count += 1
print()
    
n = 7
count = 1
while count <= n:
    print(n, end="")
    count += 1