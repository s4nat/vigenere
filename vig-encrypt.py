def vig_encrypt(plaintext,key):
    alphalist = "abcdefghijklmnopqrstuvwxyzåäö"
    alphadict = {}
    keyshift = {}

    for i in range(29):
        alphadict[i] = alphalist[i]
        keyshift[alphalist[i]] = i

    def getIndex(text, pointer):
        return keyshift[text[pointer]]

    ptr = 0
    ciphertextls = []
    keyptr = -1

    while ptr < len(plaintext):
        keyptr+=1
        keyptr=keyptr%len(key)

        index = getIndex(plaintext,ptr) + getIndex(key,keyptr)
        index = index%29
        cipherletter = alphadict[index]
        ciphertextls.append(cipherletter)
        ptr += 1

    return("".join(ciphertextls))

pt="iloveuppsala"
k = "jöhn"

ct = vig_encrypt(pt, k)
print(ct)
