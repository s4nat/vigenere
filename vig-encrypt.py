alphalist = "abcdefghijklmnopqrstuvwxyzåäöabcdefghijklmnopqrstuvwxyzåäö"
alphadict = {}
keyshift = {}

print(alphalist[:1])

for i in range(29):
    alphadict[i] = alphalist[i]
    keyshift[alphalist[i]] = i

print(alphadict)
print(keyshift)

plaintext="iloveuppsala"
key = "jöhn"

ptr = 0
ciphertext = ""
keyptr = -1

def getIndex(text, pointer):
    return keyshift[text[pointer]]

print(getIndex(plaintext, 8))

while ptr < len(plaintext):
    if keyptr < len(key)-1:
        keyptr+=1
    else:
        keyptr=0
    index = getIndex(plaintext,ptr) + getIndex(key,keyptr)
    index = index%29
    cipherletter = alphadict[index]
    
    ciphertext += cipherletter
    ptr += 1

print(ciphertext)
