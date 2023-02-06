import math
from numpy import std, array
from visualisers import RealFreq, keyshift, alphalist

def findKeyLen(targetArr, verbose=True):
    ctr = 0
    rstd = math.ceil(100*std(RealFreq))
    best = 0
    beststd = 1000
    for i in targetArr:
        ctr+=1
        thisstd = math.ceil(100*std(i))
        if thisstd>rstd:
            diff=thisstd-rstd
        else:
            diff=rstd-thisstd
        if (diff < beststd):
            best=ctr
            beststd=diff
        print(ctr, ": this:", thisstd, "rs :", rstd, "diff: ", diff)

    print("KeyLenMostLikely", best)
    return best

def crackWithKnownLen(ciphertext, keylength=1):
    cracking = [[0.]*29]*keylength
    crackArr = array(cracking)

    makeIntRf = [0]*29
    for i in range(29):
        makeIntRf[i] = math.ceil(RealFreq[i])

    idxList=[]
    for l in range(keylength):
        for c in ciphertext[l::keylength]:
            crackArr[l][keyshift[c]] += 1
        for i in range(29):
            v = crackArr[l][i]
            crackArr[l][i] = (100*(v/len(ciphertext[::keylength])))

        moving = []
        for i in crackArr[l]:
            moving.append(math.ceil(i))

        likelyAns = 0
        bestPoints = 0
        # for idx in range(KEYLEN):
        for i in range(29):
            pts = 0
            for j in range(len(makeIntRf)):
                f = makeIntRf[j]
                if f>moving[j]:
                    diff=f-moving[j]
                else:
                    diff=moving[j]-f
                print(diff, end=" ")
                if diff <= 5:
                    pts+=6-diff
                if diff > 5:
                    pts-=2*(diff-5)
            print(i, pts,end=" @@ \n")
            if pts > bestPoints:
                likelyAns = i
                bestPoints=pts
            save = moving.pop(0)
            moving.append(save)

        idxList.append(alphalist[likelyAns])
    
    key = ("".join(idxList))
    print(key)

    return key, crackArr