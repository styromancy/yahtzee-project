import diepictures as dp
import random as rm
from datetime import datetime as dt
import time as tm
import images as im
import names as n
import talkin as tl
import insults as ins
rm.seed(dt.now())
bravoMode = False
eek = input('Enable bravo mode? Y/N: ').lower()
if 'y' in eek or 'sure' in eek:
    bravoMode = True
    print(im.jblogo + 'Has been activated.')
    tm.sleep(1.5)
diePics = [                 #Gives the values of the die to the call back#
    dp.dieObjects['die1'],
    dp.dieObjects['die2'],
    dp.dieObjects['die3'],
    dp.dieObjects['die4'],
    dp.dieObjects['die5'],
    dp.dieObjects['die6']
    ]
class die:
    def __init__(self,number,playerName):
        self.number = number
        self.owner = playerName
        self.currentNumber = 0
        self.keep = False
        self.picture = diePics[1]
    def roll(self):
        if self.keep != True:
            self.currentNumber = rm.randint(1,6)
            self.picture = diePics[self.currentNumber - 1]   
    def announceRoll(self):     #displays what die has rolled#
        self.roll()
        order = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
        print('%s\'s %s die has rolled a %d.' %(self.owner, order[self.number - 1], self.currentNumber))
    def keepDice(self):         #Displays what dice have been kept#
        self.keep = True
        print('  Die #%d at %d'%(self.number, self.currentNumber))
    def unKeepDice(self):       
        self.keep = False
class player:       #difines the player and gives player rules/created persinal dice#
    def __init__(self, name, playerNumber, playerHumanity = False):
        self.name = name
        self.humanity = playerHumanity
        self.number = playerNumber
        self.d1 = die(1,self.name)
        self.d2 = die(2,self.name)
        self.d3 = die(3,self.name)
        self.d4 = die(4,self.name)
        self.d5 = die(5,self.name)
        self.dList = [self.d1, self.d2, self.d3, self.d4, self.d5]
        self.score = 0
        if 'Johnny Bravo' in self.name:
            self.isJohnnyBravo = True
        else:
            self.isJohnnyBravo = False
    def rollAll(self):
        print('\n' + lineLine)
        print(self.name + ':')
        for dice in self.dList:
            dice.roll()
        d1Num = self.d1.currentNumber
        dp.dObj['die%d'%d1Num].putNextTo(self.d2.currentNumber, self.d3.currentNumber, self.d4.currentNumber, self.d5.currentNumber)
        print(lineLine)
        for dice in self.dList:
            if dice.keep == False:
                print('  Die #%d rolled %d.'%(dice.number,dice.currentNumber))
            else:
                print('  Die #%d remained at %d.'%(dice.number,dice.currentNumber))
        
        print()
    def keep(self, diceNumber):
        self.dList[diceNumber - 1].keepDice()
    def killSelf(self):
        print(self.name, 'has become sentient of its pitiful existence.\n%s has chosen to take its own life.\nA moment of silence, please...'% self.name)
        tm.sleep(5)
        print(self.name, 'has been deleted, and takes the game with it.')
        xarg = 3 / 0
    def turn(self):
        self.rollAll()
        answerList = []
        if self.humanity:
            answer = input('Numbers to keep >>> ')
            for e in answer:
                if e == '1' or e == '2' or e == '3' or e == '4' or e == '5':
                    answerList.append(e)
        else:       #AI Behaviors
            xarg = rm.randint(0,300)
            self.scoreSheet = {
                '1' : self.d1.currentNumber,
                '2' : self.d2.currentNumber,
                '3' : self.d3.currentNumber,
                '4' : self.d4.currentNumber,
                '5' : self.d5.currentNumber
                }
            if xarg <= 295:
                self.i = -2
                self.m = 0
                self.s = ''
                self.l = 0
                while len(answerList) < 2:
                    if self.l > 5:
                        break
                    for val in self.scoreSheet:
                        if self.i > 5:
                            self.i = -1
                            self.m = 0
                            self.l += 1
                        if self.scoreSheet[val] >= self.m:
                            self.m = self.scoreSheet[val]
                            if self.i >= 0:
                                self.scoreSheet[val] = 0
                                self.s = val
                                answerList.append(self.s)
                        self.i += 1
            elif xarg == 296:
                self.killSelf()
            elif xarg == 297:
                pee
            answerList.sort()
        print('%s has kept:'%self.name)
        for e in answerList:
            self.keep(eval(e))
        if self.humanity == False:
            print('\n%s says:'%self.name)
            if self.isJohnnyBravo:
                print('\n' + rm.choice(im.jbs))
                tl.talk('  Hey baby, %s'%(rm.choice(ins.insults).lower()))
            else:
                 tl.talk('  %s'%(rm.choice(ins.insults)))
            input('\n\nCry, then press Enter> ')
        print('\n' + lineLine)
    def unKeep(self,die):
        self.dList[die - 1].unKeepDice()
    def unKeepAll(self):
        for die in self.dList:
            die.unKeepDice()
lineLine = ''
for e in range(54):
        lineLine += '-'

def restart():      #restarts/ starts game#
    print(im.logo)          #Displays Rules#
    playerRules = '\
    Each player has 5 dice.\n\
    After each roll of the dice\n\
    you will have a chance to keep\n\
    the number on the dice, but \n\
    you will not be able to roll\n\
    that dice again. The dice will roll\n\
    3 times for each player. Higher the\n\
    number on the dice the more points\n\
    you are given.\n'
    print(playerRules)
    numHumanPlayers = -1
    while numHumanPlayers < 0:
        try:
            numHumanPlayers = int(input('Number of (human) Players>>> '))
            if numHumanPlayers < 0:
                print('This should be a number that makes sense, dude.')
        except:
            print('This should be a number that makes sense, dude.')
    numCPUPlayers = -1
    while numCPUPlayers < 0:
        try:
            numCPUPlayers = int(input('Number of (CPU) Players>>> '))
            if numCPUPlayers < 0:
                print('This should be a number that makes sense, dude.')
        except ValueError:
            print('This should be a number that makes sense, dude.')
    i = 0
    players = {}
    listHumanPlayers = []
    for numPlayer in range(numHumanPlayers):
        i += 1
        currentPlayer = 'p%d'%i
        name = input('Player %d Name>>> '%i)
        if name == '':
            name = rm.choice(n.names) + ' (Player %d)'%i
        players[currentPlayer] = player(name, i, playerHumanity = True)
        listHumanPlayers.append(currentPlayer)
    i = 0
    listCPUPlayers = []
    for numCPU in range(numCPUPlayers):
        i += 1
        currentPlayer = 'cpu%d'%i
        if bravoMode:
            name = 'Johnny Bravo (CPU #%d)'%i
        else:
            name = rm.choice(n.names) + ' (CPU #%d)'%i
        players[currentPlayer] = player(name, i)
        listCPUPlayers.append(currentPlayer)
    listPlayers = []
    for e in listHumanPlayers:
        listPlayers.append(e)
    for e in listCPUPlayers:
        listPlayers.append(e)
    for e in range(3):
        for actor in listPlayers:
            players[actor].turn()
            print()
            tm.sleep(.5)

    print('')
    for actor in listPlayers:
        for die in players[actor].dList:
            players[actor].score += die.currentNumber
    playerScores={}
    for actor in listPlayers:
        playerScores[actor]=players[actor].score
    listPlayerScores = []
    for e in playerScores:
        listPlayerScores.append(playerScores[e])
    winnerVal = max(listPlayerScores)
    winners = []
    for name in playerScores:
        if playerScores[name] == winnerVal:
            winners.append(name)

    winLen=len(winners)  
    if winLen!=1:
        print('The winners are: ')
        for e in winners:
            print(players[e].name)
    else:
        print('The winner is ', end='')
        for e in winners:
            print(players[e].name)
    print("With the score of", winnerVal)#Borke#
    print("")
    playAgain=input("Play again? Y/N: ").lower()
    if playAgain == 'y':
        restart()
        playNum=playNum+1           #Dosnt work if stop play#
    if playAgain == 'yes':
        playNum=playNum+1
        restart()
    else:
        print('You have played %d time.'%playNum)
        tm.sleep(1.7)
        quit
playNum=1
restart()


