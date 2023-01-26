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
pt="udåvdnnsåqhzlhwqdyödböveöghbdyekgxävxngxngwfsxnvxnupjle"
k = "jöh"
ct = vig_decrypt(pt, k)
print(ct)

print(len(pt))

idx = 0

klen_search = {}
for i in range(1,17):
    tmp = []
    while idx < len(pt):
        tmp.append(pt[idx:idx+i])
        idx+=i
    
    klen_search[i] = tmp
    idx=0

# print(klen_search)


# # find repeated positions
# def rpos(dictionary, rletter):
#     out_dict = {}
#     return out_dict

all = "abcdefghijklmnopqrtsuvwxyzåäö"
for j in range(1,16):
    print(j)
    for i in range(1,3):
        r = all[i:i+j]

        print(vig_decrypt(pt,r))
