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

# fix real "!" issue
# find position of real "!" in plain text.  Then remove that index from both cypher and plain?
validCypherChars = re.compile('[!]')

stringCleanedPlainText = ''.join(cleanedPlainText)
exclamationPosIterator = validCypherChars.finditer(stringCleanedPlainText)
for match in exclamationPosIterator:
    print(match.span())

doubleCleanedPlainText = cleanedPlainText[0:10]
doubleCleanedPlainText.extend(cleanedPlainText[12:589])
doubleCleanedPlainText.extend(cleanedPlainText[591:])

doubleCleanedCypherText = cleanedCypherText[0:10]
doubleCleanedCypherText.extend(cleanedCypherText[12:589])
doubleCleanedCypherText.extend(cleanedCypherText[591:])

cleanedPlainText = doubleCleanedPlainText
cleanedCypherText = doubleCleanedCypherText

if len(cleanedCypherText) != len(cleanedPlainText):
    print("error cleaned cypherText length than clean plaintext")
    print("cypherText is " + str(cleanedCypherText.__len__()) + " characters long")
    print("plaintext is " + str(cleanedPlainText.__len__()) + " characters long")


length = len(cleanedPlainText)-2

offset = np.zeros(length, dtype="int8")
offsetLetter = np.zeros(length, dtype="unicode_")
trinaryPrecursor = np.ones(length, dtype="int8")

directions = ["L", "C", "R"]



# should really make this some kind of switch case
for index1 in range(0, length, 1):
    print("position " + str(index1) + "\n" + cleanedCypherText[index1] + "\n" + cleanedPlainText[index1])
    offset[index1] = ord(cleanedCypherText[index1]) - ord(cleanedPlainText[index1])
    print(str(offset[index1]))
    result = 0
    if offset[index1] == -1:
        result = 0
    elif offset[index1] == 0:
        result = 1
    elif offset[index1] == 1:
        result = 2
    elif offset[index1] == ord("!") - ord("A"):
        result = 0
    elif offset[index1] == ord("!") - ord("Z"):
        result = 2
    else:
        print("badshift")
        break

    trinaryPrecursor[index1] = result
    offsetLetter[index1] = directions[result]
    print(offsetLetter[index1])
    print(result)
    #index1 = index1 + 1  #this was uncommented before yet it somehow did not iterate by 2 or kill everything becuase range is werid

print(offset)
print(offsetLetter)
print(trinaryPrecursor)

np.savetxt("offset.csv", offset, delimiter=",", fmt="%d")
np.savetxt("offsetLetter.csv", offsetLetter, delimiter=",", fmt="%s")
np.savetxt("trinaryPrecursor.csv", trinaryPrecursor, delimiter=",", fmt="%d")


