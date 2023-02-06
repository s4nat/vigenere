import math
from numpy import std, array
from visualisers import RealFreq, keyshift, alphalist

def generateArrayCheck(ciphertext, chkarr, keylen=16):
    npArray = chkarr.copy()
    for p in range(1,(keylen)+1):
        for l in range(1):
            for c in ciphertext[l::p]:
                npArray[p-1][keyshift[c]] += 1
        for i in range(29):
            v = npArray[p-1][i]
            npArray[p-1][i] = (100*(v/len(ciphertext[::p])))

    return npArray

def knownKeyLenArr(ciphertext, keylen=1):
    npArray = array([[0.]*29]*keylen)
    for p in range(1,(keylen)+1):
        for l in range(1):
            for c in ciphertext[p-1::keylen]:
                npArray[p-1][keyshift[c]] += 1
        for i in range(29):
            v = npArray[p-1][i]
            npArray[p-1][i] = (100*(v/len(ciphertext[::p])))

    return npArray*10

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
        if verbose:
            print(ctr, ": this:", thisstd, "rs :", rstd, "diff: ", diff)

    print("KeyLenMostLikely", best)
    return best

def crackWithKnownLen(ciphertext, keylength=1, verbose=False):
    # cracking = [[0.]*29]*keylength
    crackArr = knownKeyLenArr(ciphertext,keylen=keylength)

    makeIntRf = [0]*29
    for i in range(29):
        makeIntRf[i] = math.ceil(RealFreq[i])

    idxList=[]
    totalBest = 0
    for l in range(keylength):
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
                cmpr = moving[j]
                if f < 1 and cmpr < 1:
                    pts += 5
                else:
                    if f > cmpr:
                        pts+=f*cmpr*cmpr
                    else:
                        pts+=f*cmpr*f
                
            if pts > bestPoints:
                likelyAns = i
                bestPoints=pts
            save = moving.pop(0)
            moving.append(save)
        

        idxList.append(alphalist[likelyAns])
        totalBest+=bestPoints
    
    key = ("".join(idxList))
    if verbose:
        print(key)

    return key, totalBest/keylength

def brute(ciphertext, verbose=False):
    guesses = []
    scores=[]
    bestScore = 0
    idx = 0
    for i in range(1,17):
        guess, score = crackWithKnownLen(ciphertext, keylength=i)
        guesses.append(guess)
        score = math.ceil(score)
        scores.append(score)
        if score > bestScore and i > 1:
            idx = i-1
            bestScore=score
    
    if verbose:
        print(bestScore, "\n", scores)

    return guesses, idx

# DO NOT DELETE!
