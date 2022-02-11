#Encrypter

#
#       GUNK ENCRYPTER VER 2.1.0
#
#           By William Lim
#

import random
from itertools import islice
import tkinter as tk
import playsound
import numpy as npy

random.seed()

PotentialChars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h',
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
	global PotentialChars
	
	#Chooses random PotentialChars to replace each character with in the key
	#removes the PotentialChars from disposeableChars to make sure PotentialChars are not used more than once
	disposeableChars = PotentialChars.copy()
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
	theList = []
	while True:
		nxt = list(islice(it,random.randint(min_chunk,max_chunk)))
		if nxt:
			theList.append( nxt )
		else:
			newList = []
			for i in range(0, len(theList)):
				listSegment = ""
				for j in theList[i]:
					listSegment += j
				newList.append(listSegment)
			return newList

def groupEncrypt(stringToEncrypt):
	global PotentialChars
	#assigns PotentialChars for random groups of PotentialChars
	encryptedString = stringToEncrypt
	encryptedChars = []
	separatedEncryption = []
	groupKey = []
	#Character to start on
	currentCharacter = 0
	
	tempPotentialChars = PotentialChars.copy()
	for i in encryptedString:
		encryptedChars.append(i)
	ammountOfChar = len(encryptedChars)
	if ammountOfChar >= len(PotentialChars):
		minSizeOfArrayChunk = round(ammountOfChar/len(PotentialChars)) + 1
	else:
		minSizeOfArrayChunk = 0
	newEncryptedChars = randomChunk(encryptedString, minSizeOfArrayChunk, minSizeOfArrayChunk+5)
	for i in range(0, len(newEncryptedChars)):
		#grab random letter from tempPotentialChars array and append to group key then
		#remove char from tempPotentialChars array
		if i < len(newEncryptedChars):
			separatedEncryption += newEncryptedChars[i] + "©"
		else:
			separatedEncryption += newEncryptedChars[i]
		characterIndex = round(random.randrange(0,len(tempPotentialChars)))
		groupKey.append(tempPotentialChars[characterIndex])
		del tempPotentialChars[characterIndex]
	d  = {
		'key': convertToString(separatedEncryption),
		'data': convertToString(groupKey)
	}
	return d

def encryptString(stringToEncrypt):
	#parses through string and replaces PotentialChars based on the key
	theKey = createKey()
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
			
	groupEnc = groupEncrypt(convertToString(encryptedChars))
	d = {
		'key': groupEnc.get('key') + "Æ" + theKey,
		'data': groupEnc.get('data')
	}
	return d
	

def decryptString(stringToDecrypt, UserKey):
	global PotentialChars
	#parses through string and replaces PotentialChars based on the key
	encKeys = UserKey.split("Æ")
	#group parse
	groupKey = encKeys[0].split("©")
	groupDecrypted = ""
	for i in range(0, len(stringToDecrypt)):
		groupDecrypted += groupKey[i]
	#single parse
	decryptedString = groupDecrypted
	decryptedChars = []
	for i in decryptedString:
		decryptedChars.append(i)
	for i in range(0, len(decryptedString)):
		for j in range(0,len(PotentialChars)):
		
			if decryptedString[i] == encKeys[1][j]:
			
				decryptedChars[i] = PotentialChars[j]
				break
			#else check next letter in key/continue
	return convertToString(decryptedChars)

#GUI

root = tk.Tk()

EnF1 = tk.StringVar

DeF1 = tk.StringVar
DeF2 = tk.StringVar

root.title(" ENCRYPTER ")


Title1 = tk.Frame(root)
frm = tk.Frame(root)
Title2 = tk.Frame(root)
frm2 = tk.Frame(root)
frm3 = tk.Frame(root)

Title1.grid()
frm.grid()
Title2.grid()
frm2.grid()
frm3.grid()

tk.Label(Title1, text="Encrypter").grid(column=0, row=0)
tk.Label(frm, text="File path:").grid(column=0, row=0)
T = tk.Entry(frm, textvariable = EnF1, width = 52)
T.grid(column=1, row=0)
tk.Label(Title2, text="Decrypter").grid(column=0, row=0)
tk.Label(frm2, text="File path:").grid(column=0, row=0)
tk.Label(frm2, text=" Key path:").grid(column=0, row=1)
T2 = tk.Entry(frm2, textvariable = DeF1, width = 52)
T3 = tk.Entry(frm2, textvariable = DeF2, width = 52)
T2.grid(column=1, row=0)
T3.grid(column=1, row=1)

def encryptPress():
	try:
		fileContent = open(T.get())
	except FileNotFoundError:
		playsound.playsound('sounds/FilenameError.wav')
	newEncryptedFile = encryptString(fileContent.read())

	fileContent.close()

	newFileName = T.get().split('.')

	encryptedFile = open((newFileName[0] + "++" + newFileName[1] + ".gunk"), 'w')

	encryptedFile.write(newEncryptedFile.get('data'))

	encryptedFile.close()
	
	encryptionKey = open((newFileName[0] + "++" + newFileName[1] + ".gunkkey"), 'w')

	encryptionKey.write(newEncryptedFile.get('key'))

	encryptionKey.close()
	playsound.playsound('sounds/NotifSound.mp3')

	
def decryptPress():
	try:
		encryptedFileRead = open(T2.get(), 'r')
		encryptedFileKeyRead = open(T3.get(), 'r')
	except FileNotFoundError:
		playsound.playsound('sounds/FilenameError.wav')
	newEncryptedString = encryptedFileRead.read()
	newEncryptedKeyString = encryptedFileKeyRead.read()

	newDecryptedString = decryptString(newEncryptedString, newEncryptedKeyString)
	
	encryptedFileRead.close()
	encryptedFileKeyRead.close()
	
	fileNameWithExtension = T2.get().split('.')
	fileNameParts = fileNameWithExtension[0].split("++")
	newFileName = fileNameParts[0] + "." + fileNameParts[1]
	
	decryptedFile = open(newFileName, 'w')

	decryptedFile.write(newDecryptedString)

	decryptedFile.close()
	playsound.playsound('sounds/NotifSound.mp3')

tk.Button(frm, text="Encrypt", command=encryptPress).grid(column=2, row=0)
tk.Button(frm2, text="Decrypt", command=decryptPress).grid(column=2, row=0)

tk.Button(frm3, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()