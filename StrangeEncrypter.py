#STRANGE ENCRYPT


"""choose random ranges of indexes within an already random character for character encrypted string then take those ranges and represent them 
with a single character, making sure that there are as many sections as there are possible characters"""


import random
from itertools import islice


Characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h',
'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.',',','1','2','3','4','5','6','7','8','9','0']


Key = [['A',''],['B',''],['C',''],['D',''],['E',''],['F',''],['G',''],['H',''],['I',''],['J',''],['K',''],['L',''],['M',''],['N',''],['O',''],['P',''],
['Q',''],['R',''],['S',''],['T',''],['U',''],['V',''],['W',''],['X',''],['Y',''],['Z',''],['a',''],['b',''],['c',''],['d',''],['e',''],['f',''],['g',''],
['h',''],['i',''],['j',''],['k',''],['l',''],['m',''],['n',''],['o',''],['p',''],['q',''],['r',''],['s',''],['t',''],['u',''],['v',''],['w',''],['x',''],
['y',''],['z',''],[' ',''],['.',''],[',',''],['1',''],['2',''],['3',''],['4',''],['5',''],['6',''],['7',''],['8',''],['9',''],['0','']]

def convertToString(charArray):
	newString = "" 
	for i in charArray:
		newString += i
	return newString

def createKey():
	#Chooses random characters to replace each character with in the key
	#removes the characters from disposeableChars to make sure characters are not used more than once
	disposeableChars = Characters;
	KeyForUser = ""
	
	for i in range(0,len(Key)):
		#Choose a random index from the disposeable chars, apply that to key index i,
		#then delete that index from disposeable Chars
		randomIndex = random.randint(0,len(disposeableChars) - 1)
		Key[i][1] = disposeableChars[randomIndex]
		KeyForUser += disposeableChars[randomIndex]
		del disposeableChars[randomIndex]
		
	return KeyForUser

def randomChunk(li, min_chunk=1, max_chunk=3):
	it = iter(li)
	while True:
		nxt = list(islice(it,randint(min_chunk,max_chunk)))
		if nxt:
			yield nxt
		else:
			break

def groupEncrypt(stringToEncrypt):
	#assigns characters for random groups of characters
	encryptedString = stringToEncrypt
	encryptedChars = []
	groupKey = []
	#Character to start on
	currentCharacter = 0
	
	ammountOfChar = len(encryptedChars)
	
	if ammountOfChar > len(Characters):
		minSizeOfArrayChunk = ammountOfChar/len(Characters)
	else:
		minSizeOfArrayChunk = 1
	for i in encryptedString:
		encryptedChars.append(i)
	while ammountOfChar > 0:
		randomChunk(encryptedChars, minSizeOfArrayChunk, minSizeOfArrayChunk+5)
	for i in range(0, len(encryptedChars)):
		#grab random letter from tempCharacters array and append to group key then
		#remove char from tempCharacters array
		groupKey.append()
	return { data:convertToString(encryptedChars) key:groupKey }

def encryptString(stringToEncrypt):
	#parses through string and replaces characters based on the key
	encryptedString = stringToEncrypt
	encryptedChars = []
	for i in encryptedString:
		encryptedChars.append(i)
	for i in range(0, len(stringToEncrypt)):
		for j in range(0,len(Key)):
		
			if stringToEncrypt[i] == Key[j][0]:
			
				encryptedChars[i] = Key[j][1]
				break
			#else check next letter in key/continue
			
	return convertToString(encryptedChars)
	

def decryptString(stringToDecrypt, UserKey):
	#parses through string and replaces characters based on the key
	decryptedString = stringToDecrypt
	decryptedChars = []
	for i in decryptedString:
		decryptedChars.append(i)
	for i in range(0, len(stringToDecrypt)):
		for j in range(0,len(Characters)):
		
			if stringToDecrypt[i] == UserKey[j]:
			
				decryptedChars[i] = Characters[j]
				break
			#else check next letter in key/continue
	return convertToString(decryptedChars)

#MAIN
print("Would you like to encrypt or decrypt a file (E/D):")
if input() == "E":
	print("Your Encryption Key:")
	print()
	print(str(createKey()))
	print()
	print("Enter a file to encrypt... ")

	fileName = input()

	fileContent = open(fileName)

	newEncryptedFile = encryptString(fileContent.read())

	fileContent.close()

	print()
	print("Your Encrypted String: ", str(newEncryptedFile))

	newFileName = fileName.split('.')

	encryptedFile = open((newFileName[0] + "++" + newFileName[1] + ".gunk"), 'w')

	encryptedFile.write(newEncryptedFile)

	encryptedFile.close()
	
	print()
	print("Encryption complete!")
else:
	print()
	print("Enter a file to decrypt:")
	fileName = input()
	
	print()
	print("Enter your decryption key:")
	decryptionKey = input()
	
	encryptedFileRead = open(fileName, 'r')

	newEncryptedString = encryptedFileRead.read()

	newDecryptedString = decryptString(newEncryptedString, decryptionKey)
	
	encryptedFileRead.close()
	
	print()
	print("Your Decrypted String: ", str(newDecryptedString))
	
	fileNameWithExtension = fileName.split('.')
	fileNameParts = fileNameWithExtension[0].split("++")
	newFileName = fileNameParts[0] + "." + fileNameParts[1]
	
	decryptedFile = open(newFileName, 'w')

	decryptedFile.write(newDecryptedString)

	decryptedFile.close()
	
	print()
	print("Decryption complete!")