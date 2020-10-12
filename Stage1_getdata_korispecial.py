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

directions = ["L", "C", "R"]

length = len(cleanedPlainText)-2

trinaryPrecursor = ["x" for i in range(length)]
offset = ["x" for i in range(length)]
offsetLetter = ["X" for i in range(length)]


for index in range(1, len(cleanedPlainText) - 1):
    # Sanity check
    print("position " + str(index) + "\n" + cleanedCypherText[index] + "\n" + cleanedPlainText[index])
    
    # Calculate the current offset
    curr_offset = ord(cleanedCypherText[index]) - ord(cleanedPlainText[index])
    
    # Store it
    offset[index-1] = curr_offset

    # Sanity check
    print(str(curr_offset))
    
    # Find our result
    result = 0
    if curr_offset == -1:
        result = 0
    elif curr_offset == 0:
        result = 1
    elif curr_offset == 1:
        result = 2
    elif curr_offset == ord("!") - ord("A"):
        result = 0
    elif curr_offset == ord("!") - ord("Z"):
        result = 2
    else:
        print("badshift")
        break

    # Append to our lists
    trinaryPrecursor[index-1] = result
    offsetLetter[index-1] = directions[result]

    # Sanity check
    print(offsetLetter[index - 1])
    print(result)

# Convert our lists to np arrays
trinaryPrecursor = np.array(trinaryPrecursor)
offsetLetter = np.array(offsetLetter)
offset = np.array(offset)

# Print our findings
print(offset)
print(offsetLetter)
print(trinaryPrecursor)

# np.savetxt("offset.csv", offset, delimiter=",", fmt="%d")
# np.savetxt("offsetLetter.csv", offsetLetter, delimiter=",", fmt="%s")
# np.savetxt("trinaryPrecursor.csv", trinaryPrecursor, delimiter=",", fmt="%d")


