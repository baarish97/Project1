#Number guessing game using random module

import random
cnum= random.randrange(1,101)
userinput= int(input('Enter the number:-'))
if userinput > cnum:
    print('Computer number is:',cnum)
    print('You guess number is too high')
elif userinput < cnum:
    print('Computer number is :', cnum)
    print ('Your guess number is too low')
else:
    print('Computer number is :', cnum)
    print('your guess number is equal')

        