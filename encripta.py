from getKeys import getKeys

primeList = open('./primeList.txt').readlines()
#input = open('./input.txt')
#output = './output.txt'

keysGenerated = getKeys(primeList)

print(keysGenerated)