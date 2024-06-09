import random

print('WELCOME TO THE GAME OF HEADS OR TAILS')
player_names =input('Please insert your names:')
player_names = player_names.replace(' and ',' ') 
player_names = player_names.replace(' AND ',' ') 
player_names = player_names.replace(' ANd ',' ')
player_names = player_names.replace(' aND ',' ')
player_names = player_names.replace(' AnD ',' ')
player_names = player_names.replace(' And ',' ')
player_names = player_names.replace(' aNd ',' ')
player_names = player_names.replace(' anD ',' ')
names = player_names.split()
print(f'{names[0]} is playing as tails and {names[1]} is playing as heads.')
throws = input('How many times do you want to flip the magical coin of heads or tails :')
throws = int(throws)
heads = 0
tails = 0

for throw in range(1,throws+1):
    if random.random() < 0.5 :
        print(f'Throw {throw}: head')
        heads = heads + 1
    else:
        print(f'Throw {throw}: tail')
        tails = tails + 1

if heads < tails:
    print(f'{names[0]} has won {tails} to {heads}!')
elif heads == tails:
    print("It's a draw !")
else:
    print(f'{names[1]} has won {heads} to {tails}!')
