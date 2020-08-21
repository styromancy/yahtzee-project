import random as rm
from datetime import datetime
rm.seed(datetime.now())
import results
prb = results.markov
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def findNextLetter(char):
	nextChar = ''
	total_percent = 0
	conditional = {}
	for letters in alphabet:
		total_percent += prb[char + letters]
		if prb[char + letters] != 0:
			conditional[letters] = total_percent
	x = rm.randint(0,int(total_percent))
	for letters in conditional:
		if x <= conditional[letters]:
			return letters

def wordBuilder(char,length):
	word = char
	for letters in range(length - 1):
		word += findNextLetter(word[-1])
	return word
