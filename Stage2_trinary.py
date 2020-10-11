import numpy as np
import pprint
trinaryPrecursor = np.loadtxt("trinaryPrecursor.csv")
listTrinaryPrecursor = trinaryPrecursor.tolist()
# makeItSuckLess = pprint.PrettyPrinter(indent=4)
# makeItSuckLess.pprint(trinaryPrecursor)

listTrinaryPrecursor = [int(num) for num in listTrinaryPrecursor]

lookup = [chr(code) for code in range(ord('A'), ord('Z'))]
lookup.append('!')

trinarySnips = [listTrinaryPrecursor[i:i + 3] for i in range(0, len(listTrinaryPrecursor), 3)]

triLetter = np.zeros(len(trinarySnips), dtype="unicode_")

for index in range(0, len(trinarySnips)-1):
    print(trinarySnips[index])
    triValue = trinarySnips[index][2]*1 + trinarySnips[index][1]*3 + trinarySnips[index][0]*9
    print(triValue)
    triLetter[index] = lookup[triValue]
    # triLetter[index] = (chr(ord('A') - 1 + triValue))
    print(triLetter[index])

print(triLetter)
