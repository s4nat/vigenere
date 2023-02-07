def vig_decrypt(plaintext,key):
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

        index = getIndex(plaintext,ptr) - getIndex(key,keyptr)
        index = index%29
        cipherletter = alphadict[index]
        ciphertextls.append(cipherletter)
        ptr += 1

    return("".join(ciphertextls))

# pt="udölnfnsögrrlhygnqöddsczögjunqekimpkxmpjnx"
# pt="udåvdnnsåqhzlhwqdyödböveöghbdyekgxävxngxngwfsxnvxnupjle"
# k = "jöh"
# ct = vig_decrypt(pt, k)
# print(ct)
