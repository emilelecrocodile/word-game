import random

random_number = random.randint(0,25) 

word = ''
while len(word) < 6:
    word = input('Please for my life type the magical word of golden destiny:')
    if len(word) < 6:
        print('Word is not long enough. It needs to have 6 characters minimum!')

print(f'the length of the word is {len(word)} characters long.')
print(f'The unicode for the first character {word[0]} is {ord(word[0])}.') 
print(f'The first two characters are "{word[0:2]}", the middle characters are "{word[2:-2]}" and the last two characters are"{word[-2:]}".')
print(f'Here is every 2 character of the word: "{word[::2]}" .')
print(f'Here is the word in reverse order: "{word[::-1]}" .')

print('-'.join([str(ord(character)) for character in word]))
# unicode_characters = []
# for character in word:  
#     unicode_characters.append(str(ord(character)))

# print('-'.join(unicode_characters))  