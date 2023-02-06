from filepaths import paths
import numpy as np

def getCipherFiles(folder='*'):
    crypticDirs = list(paths.get('DATA_DIR').glob(folder))
    allFiles = []
    for dir in crypticDirs:
        for file in list(dir.glob('*crypto')):
            allFiles.append(file)
    return allFiles

def readFiles(files):
    output = []
    filenames = []
    for i in files:
        filenames.append(i.stem)
        file = open(i,"r+")
        output.append(file.read())
        file.close()
    return output, filenames

def touchFile(filename, answer):
    try:
        my_file = open(filename, 'w+')
    except IOError:
        my_file = open(filename, 'w+')
    my_file.write(answer)
    my_file.close()

def setup():
    alphalist = "abcdefghijklmnopqrstuvwxyzåäö"
    alphadict = {}
    keyshift = {}

    for i in range(29):
        alphadict[i] = alphalist[i]
        keyshift[alphalist[i]] = i

    frequencies = [0.]*29
    keylen = [frequencies]*16

    chkarr = np.array(keylen)
    RealFreq = [0.]*29

    RealFreq[keyshift['a']] = 9.38
    RealFreq[keyshift['b']] = 1.54
    RealFreq[keyshift['c']] = 1.49
    RealFreq[keyshift['d']] = 4.70
    RealFreq[keyshift['e']] = 10.15
    RealFreq[keyshift['f']] = 2.03
    RealFreq[keyshift['g']] = 2.86
    RealFreq[keyshift['h']] = 2.09
    RealFreq[keyshift['i']] = 5.82
    RealFreq[keyshift['j']] = 0.61
    RealFreq[keyshift['k']] = 3.14
    RealFreq[keyshift['l']] = 5.28
    RealFreq[keyshift['m']] = 3.47
    RealFreq[keyshift['n']] = 8.54
    RealFreq[keyshift['o']] = 4.48
    RealFreq[keyshift['p']] = 1.84
    RealFreq[keyshift['q']] = 0.02
    RealFreq[keyshift['r']] = 8.43
    RealFreq[keyshift['s']] = 6.59
    RealFreq[keyshift['t']] = 7.69
    RealFreq[keyshift['u']] = 1.92
    RealFreq[keyshift['v']] = 2.42
    RealFreq[keyshift['w']] = 0.14
    RealFreq[keyshift['x']] = 0.16
    RealFreq[keyshift['y']] = 0.71
    RealFreq[keyshift['z']] = 0.07
    RealFreq[keyshift['å']] = 1.34
    RealFreq[keyshift['ä']] = 1.80
    RealFreq[keyshift['ö']] = 1.31
    for i in range(len(RealFreq)):
        RealFreq[i] *= 1
    
    freqDict = {}
    reverseFD = {}
    for i in range(len(RealFreq)):
        freqDict[alphalist[i]]=RealFreq[i]
        reverseFD[RealFreq[i]]=alphalist[i]
    
    RealFreq = np.array(RealFreq)
    return RealFreq, alphadict, alphalist, keyshift, chkarr

RealFreq, __, alphalist, keyshift, __ = setup()

# def unlink_DStore(files):
#     for f in files:
#         try:
#             f.read_csv(f)
#         except:
#             f.unlink()
#     return 