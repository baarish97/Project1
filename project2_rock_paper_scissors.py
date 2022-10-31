#Rock Paper Scissor game

import random
l=['rock', 'paper', 'scissors']
'''
    rock vs paper-> paper win
    paper vs scissors-> scissors win
    scissors vs rock-> rock win
'''
while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
    Game start...
    1 Yes
    2 No/Exit
    '''))
    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''
            1 Rock
            2 Scissors
            3 Paper
            '''))
            if userInput==1:
                uchoice ='rock'
            elif userInput==2:
                uchoice ='Scissors'
            elif userInput==3:
                uchoice ='paper'
            cchoice=random.choice(l)

            if cchoice==uchoice:
                print('Computer choice is', cchoice)
                print('Your choice is', uchoice)
                print('Game draw becoz choice are equal')
                ucount=ucount+1
                ccount= ccount+1
            elif ((uchoice=='paper' and cchoice=='rock') or(uchoice=='scissors' and cchoice=='paper')
                  or (uchoice=='rock' and cchoice=='scissors')):
                print('Computer choice is', cchoice)
                print('Your choice is', uchoice)
                print('You win the match')
                ucount = ucount + 1
            else:
                print('Computer choice is', cchoice)
                print('Your choice is', uchoice)
                print('Computer win')
                ccount= ccount+1
            if ucount==ccount:
                print("Final game draw")
                print('User score', ucount)
                print('Computer score', ccount)
            elif ucount> ccount:
                print('Final you win')
                print('User score', ucount)
                print('Computer score', ccount)
            else:
                print('Final Computer win')
                print('User score', ucount)
                print('Computer score', ccount)
    else:
         break
