print('Program 1') 

word = input('\nInput a string: ')
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
vowel_count = 0
consonant_count = 0
space_count = word.count(" ")
 
for character in word:
    if character in vowels:
        vowel_count += 1
    elif "A" <= character <= "Z" or "a" <= character <= "z":
        consonant_count += 1
        
print('Number of vowels: ', vowel_count)
print('Number of consonant: ', consonant_count)
print('Number of spaces: ', space_count)