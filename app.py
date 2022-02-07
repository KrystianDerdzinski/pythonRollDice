from random import random

numHistory = []

input('Press enter to roll the dice')

def getUserInput():
	inputText = input('\nPress enter to roll again or h to show history\n')

	if inputText == 'h':
		print('History: ', numHistory)
	else:
		result = getRandomNumber(1, 6)
		numHistory.append(result)
		print(result)
		
	getUserInput()

def getRandomNumber(min, max):
	return round(random() * (max - min) + min)

firstNum = getRandomNumber(1,6)
print(firstNum)
numHistory.append(firstNum)

getUserInput()
