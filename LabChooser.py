print('Hello, Thank you for choosing The Lab Chooser')
print('Password?')
Password = input()
while Password != 'Wowie Zowie':
    print ('Access Denied')
    print('Password?')
    Password = input()
    
print()

import random
list = []

def labchooser(n):
    if n == 1 :
        return 'Dan'
    elif n == 2:
        return 'Lynn'
    elif n == 3:
        return 'Lyndsey'
    elif n == 4:
        return 'Katie'
    elif n == 5:
        return 'Laura'
    elif n == 6:
        return 'Emily S'
    elif n == 7:
        return 'Avery'
    elif n == 8:
        return 'Tim'
    elif n == 9:
        return 'Josh'
    elif n == 10:
        return 'Chiharu'
    elif n == 11:
        return 'Emily C'
    elif n == 12:
        return 'Maddie'
    elif n == 13:
        return 'Puneet'
    elif n == 14:
        return 'LaQuita'
    elif n == 15:
        return 'Ashley'
while len(list) < 15:
    r = labchooser(random.randint(1,15))
    if r not in list: list.append(r)


print(list)
print()
print('End Of Program, Thank You. Press ENTER to exit.')
input()
