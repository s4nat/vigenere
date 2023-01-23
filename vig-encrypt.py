alphalist = "abcdefghijklmnopqrstuvwxyzåäöabcdefghijklmnopqrstuvwxyzåäö"
alphadict = {}
keyshift = {}

for i in range(29):
    alphadict[i] = alphalist[i]
    keyshift[alphalist[i]] = i

print(alphadict)
print(keyshift)

plaintext="iloveuppsala"
key = "jöhn"

ptr = 0
ciphertextls = []
keyptr = -1

def getIndex(text, pointer):
    return keyshift[text[pointer]]

print(getIndex(plaintext, 8))

while ptr < len(plaintext):
    keyptr+=1
    keyptr=keyptr%len(key)

    index = getIndex(plaintext,ptr) + getIndex(key,keyptr)
    index = index%29
    cipherletter = alphadict[index]
    ciphertextls.append(cipherletter)
    ptr += 1

print("".join(ciphertextls))
