import numpy as np
import re
cypherText = open("cypherText", "r").read()
plainText = open("PlainText", "r").read()

if len(cypherText) != len(plainText):
    print("error cypherText length than plaintext")
    print("cypherText is " + str(cypherText.__len__()) + " characters long")
    print("plaintext is " + str(plainText.__len__()) + " characters long")

# try:
#     len(cypherText) == len(plainText)
# except CypherLengthError:
#     print("error cypherText length than plaintext")



#prune punctuation
#acceptable ord value list
# print([ord('A'),ord("F"), ord('Z'),ord('!')])
validCypherChars= re.compile('[A-Z!]')
cleanedCypherText = validCypherChars.findall(cypherText)
cleanedPlainText = validCypherChars.findall(plainText)

offset = np.zeros(len(cleanedCypherText), dtype="int8")
offsetLetter = np.zeros(len(cleanedCypherText), dtype="unicode_")
trinaryPrecursor= np.zeros(len(cleanedCypherText), dtype="int8")

if len(cleanedCypherText) != len(cleanedPlainText):
    print("error cleaned cypherText length than clean plaintext")
    print("cypherText is " + str(cleanedCypherText.__len__()) + " characters long")
    print("plaintext is " + str(cleanedPlainText.__len__()) + " characters long")


#should really make this some kind of switch case
for index1 in range(0, len(cleanedPlainText), 1):
    print("position " + str(index1) + "\n" + cleanedCypherText[index1] + "\n" + cleanedPlainText[index1])
    offset[index1] = ord(cleanedCypherText[index1]) - ord(cleanedPlainText[index1])
    print(str(offset[index1]))
    if offset[index1] == -1:
        print('L')
        offsetLetter[index1] = 'L'
        trinaryPrecursor[index1] = 0
    elif offset[index1] == 0:
        print('C')
        offsetLetter[index1] = 'C'
        trinaryPrecursor[index1] = 1
    elif offset[index1] == 1:
        print('R')
        offsetLetter[index1] = 'R'
        trinaryPrecursor[index1] = 2
    elif offset[index1] == ord("!")-ord("A"):
        print('L!')
        offsetLetter[index1] = 'L'
        trinaryPrecursor[index1] = 0
    elif offset[index1] == ord("!") - ord("Z"):
        print('R!')
        offsetLetter[index1] = 'R'
        trinaryPrecursor[index1] = 2
    else:
        print("badshift")
        break

    index1 = index1 + 1

print(offset)
print(offsetLetter)
print(trinaryPrecursor)

np.savetxt("offset.csv", offset, delimiter=",",fmt="%d")
np.savetxt("offsetLetter.csv", offsetLetter, delimiter=",", fmt="%s")
np.savetxt("trinaryPrecursor.csv", trinaryPrecursor, delimiter=",", fmt="%d")


