import random
class diePicture:
    def __init__(self, value, name, die):
        self.n = name
        self.v = value
        self.r1 = die[0]
        self.r2 = die[1]
        self.r3 = die[2]
        self.r4 = die[3]
        self.r5 = die[4]
        self.allRows = die
    def putNextTo(self, *die):
        theDie = []
        theDie.append(dieObjects['die%d'%self.v])
        for e in die:
            theDie.append(dieObjects['die%d'%e])
        lineNum = -1
        for line in range(5):
            lineNum += 1
            for die in theDie:
                print(die.allRows[lineNum], end = ' ')
            print('\n', end = '')
        
    def printSelf(self):
        for e in self.allRows:
            print(e)

d0 = ['██████████',
      '██████████',
      '██████████',
      '██████████',
      '██████████'
      ]
d1 = ['██████████',
      '██████████',
      '████  ████',
      '██████████',
      '██████████'
      ]
d2 = ['██████████',
      '██  ██████',
      '██████████',
      '██████  ██',
      '██████████'
      ]
d3 = ['██████████',
      '█  ███████',
      '████  ████',
      '███████  █',
      '██████████'
      ]
d4 = ['██████████',
      '█  ████  █',
      '██████████',
      '█  ████  █',
      '██████████'
      ]
d5 = ['██████████',
      '█  ████  █',
      '████  ████',
      '█  ████  █',
      '██████████'
      ]
d6 = ['██████████',
      '█  █  █  █',
      '██████████',
      '█  █  █  █',
      '██████████'
      ]

dieList = [d1,d2,d3,d4,d5,d6]
dieObjects = {}
i = 0
for e in dieList:
    i += 1
    dieObjects['die%d'%i] = diePicture(i, 'die%d'%i, e)

def diit():
    x = random.randint(1,6)
    dieObjects['die%d'%x].printSelf()
    input()
    diit()
dObj = dieObjects
