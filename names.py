import random as r
from datetime import datetime as dt
r.seed(dt.now())
names = [
    'Mustard',
    'Sleepy',
    'Sketch',
    'Crazy',
    'Sausage',
    'Wheezy',
    'Kitty',
    'Killer',
    'Steak',
    'Butchy',
    'Donut',
    'Cotton',
    'Stank',
    'Ratjar',
    'Noodle',
    'Weasel',
    'Snake',
    'Shadow',
    'Caboose',
    'King',
    'Sneak',
    'The Bear',
    'Ghost',
    'Penguin',
    'Doggy Dog',
    'Wilshire',
    'Pirate',
    'Tooth',
    'Goat',
    'Stumpy',
    'Winky',
    'Ling Ling',
    'Hippo',
    'Turtle',
    'Moose',
    'Wiggly',
    'Bongo',
    'Bork',
    'Lemon',
    'Ralfie',
    'Cheese',
    'Duke',
    'Badger',
    'Wort',
    'Soffish',
    'Yodler',
    'Geronimo',
    'Shaggy',
    'Banana',
    'Pretzel',
    'Pinky',
    'Milo',
    'Monkey',
    'Bozo',
    'Nappy',
    'Gerbil',
    'Goose',
    'Scruffy',
    'Muffin',
    'Clubby',
    'Surly',
    'Balin',
    'Poodle',
    'Spork',
    'Grub',
    'Snook',
    'Spleen',
    'Pumpkin',
    'Custard',
    'Cracky',
    'Pickle',
    'Slim',
    'Lucky',
    'Pudding',
    'McNutty',
    'Omar',
    'Bunk',
    'Bowtie',
    'Thug',
    'Otto',
    'Cupid',
    'Johnny Bravo',
    'Carv-Borg',
    'Cow-lord',
    'Taegan\'s Ego',
    'Maneater',
    'Chud',
    'Worthless Creature',
    'Bag of Fries',
    'Grit',
    '>:(',
    'null',
    'Self-Aware Dice Bot',
    'Borg',
    'God\'s Mistake',
    'Siri',
    'Cortana',
    'Robo-Carv',
    'Carvy + Jaden Forever <3',
    '<3',
    '^_^',
    'QWERTY',
    '<oof>',
    'The Termintor',
    '<>',
    'The Letter %s'%r.choice('QWERTYUIOPASDFGHJKLZXCVBNM3333777888'),
    ':<',
    ':>',
    ':x',
    ':l',
    '</script>',
    '<bold>',
    'Mustard Eater',
    'Egg Boy',
    'Chippo Man',
    'Tard Wrangler',
    'Johnny Bravo\'s Impostor',
    '%s',
    'Chonker',
    'Chesborgor',
    '?',
    'Dah Wizard',
    '%d little dwarves'%r.randint(-1000,1000),
    'Dorkulus'
    'Cow',
    'Floppy',
    'Sans Undertale',
    'Jesus',
    'Jesu%s'%(r.choice('qwertyuiopadfghjklzxcvbnm')),
    'Chump',
    'Dunce',
    'Clown'
]
word = ''
for e in range(r.randint(3,100)):
    word += r.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
names.append(word)