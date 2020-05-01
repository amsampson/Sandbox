import random
import sys

print('Hello, Thank you for choosing The Lab Chooser 3.0')
print('Password?')
Password = input()
while Password != 'Wowie Zowie':
    print ('Access Denied')
    print('Password?')
    Password = input()

print('Access granted')

print()


list=[]

### Attendence entry
print('Please enter those in attendance')
x = input()
list.append(x)
print('Please enter more. If finished hit ENTER')
while x != '': ### loop to type everybody in
    x = input()
    if x == '':
        break 
    else:
        list.append(x)
    print('Please enter more. If finished hit ENTER')


def shuffle_list():
    random.shuffle(list)

    print()
    print('The order for today is...')

    ### Order lister by line (will list vertically)
    for name in list:
        print(name)

        
shuffle_list()
print()

###reshuffler
y='reshuffle'
def reshuffle_list():
    print('To reshuffle type: reshuffle.  To exit: Please hit ENTER')
    y=input()
    if y.lower()=='reshuffle':
        shuffle_list()
    else:
        exit()
while y=='reshuffle':
    reshuffle_list()
