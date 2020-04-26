print('Hello, Thank you for choosing The Lab Chooser 2.0')
print('Password?')
Password = input()
while Password != 'Wowie Zowie':
    print ('Access Denied')
    print('Password?')
    Password = input()

print('Access granted')

print()

import random
list=[]

### Attendence entry
print('Please enter those in attendance')
x = input()
list.append(x)
print('Please enter more. If finished type: Done')
while x != 'Done': ### loop to type everybody in
    x = input()
    if x == 'Done':
        break ### This keeps "Done" from being listed
    else:
        list.append(x)
    print('Please enter more. If finished type: Done')

random.shuffle(list)


print()
print('The order for today is...')

### Order lister by line (will list vertically)
r=0
while r <= len(list):
    if r == len(list):
        break
    print(list[r])
    r = r+1
    
print()
print('To exit: Please hit ENTER')
input()
