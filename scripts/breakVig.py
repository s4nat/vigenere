from os import getcwd, path
from pathlib import Path
from sys import path as sp, argv
sp.append(path.join((Path.cwd()),"scripts"))

from filepaths import paths

from extractfile import getCipherFiles, readFiles, setup, touchFile
cipherFiles = getCipherFiles()
len(cipherFiles)

from combine import cipherToPlainWithKey, plainToCipher
import matplotlib.pyplot as plt
import numpy as np
import math

from visualisers import plot_full_v2, plot_guess, plot_guess2
from decryptors import findKeyLen, crackWithKnownLen, generateArrayCheck, knownKeyLenArr, brute

def saveOutputLen(ciphers, keylen, newName):
    OUTDIR = paths.get('OUTPUT_DIR')
    p = Path(OUTDIR,newName)
    p.mkdir(exist_ok=True)
    Kguess,__ = crackWithKnownLen(ciphers, keylength=keylen)
    Pguess = cipherToPlainWithKey(ciphers, Kguess)
    plainPath = Path(p,("".join([newName,".plain"])))
    keyPath = Path(p,("".join([newName,".key"])))
    touchFile(plainPath, Pguess)
    touchFile(keyPath, Kguess)

def saveOutputKey(ciphers, key, newName):
    OUTDIR = paths.get('OUTPUT_DIR')
    p = Path(OUTDIR,newName)
    p.mkdir(exist_ok=True)
    Pguess = cipherToPlainWithKey(ciphers, key)
    plainPath = Path(p,("".join([newName,".plain"])))
    keyPath = Path(p,("".join([newName,".key"])))
    touchFile(plainPath, Pguess)
    touchFile(keyPath, key)
    print()

# Complete Setup
rf, alphadict, alphalist, keyshift, chkarr = setup()
keylen = 16

def noArgs():
    # Get ciphertexts and files
    ctl, filenames = readFiles(cipherFiles)

    i = 0
    CtPairList = []
    longkey = False
    for TargetedText in ctl:    
        longkey = i < 6
        kgs, idx = brute(TargetedText, longkey=longkey)

        CtPairList.append((TargetedText,kgs[idx]))

        # print(ctl.index(TargetedText), filenames[ctl.index(TargetedText)])
        # print(cipherToPlainWithKey(TargetedText, kgs[idx], verbose=False))

        i+=1

    for i in range(len(CtPairList)):
        saveOutputKey(CtPairList[i][0], CtPairList[i][1], filenames[i])

    print("Ran on existing files")


def saveOutputKey(ciphers, key, newName, outdir=paths.get('OUTPUT_DIR')):
    OUTDIR = outdir
    p = Path(OUTDIR,newName)
    p.mkdir(exist_ok=True)
    Pguess = cipherToPlainWithKey(ciphers, key, verbose=False)
    plainPath = Path(p,("".join([newName,".plain"])))
    keyPath = Path(p,("".join([newName,".key"])))
    touchFile(plainPath, Pguess)
    touchFile(keyPath, key)
    print()


def main(*argv):
    args = argv[1:]
    # args is a list of the command line args
    if len(args) != 2:
        print("\nRun Format: \npython3 breakVig.py <TargetFilePath> <outputDir>\n")
        return
    
    filepath = [Path(args[0])]
    ctl, filenames = readFiles(filepath)

    outdir = Path(args[1])

    i = 0
    CtPairList = []
    longkey= filenames[0] in "123456"
    for TargetedText in ctl:
        kgs, idx = brute(TargetedText, longkey=longkey)

        CtPairList.append((TargetedText,kgs[idx]))

        # print(ctl.index(TargetedText), filenames[ctl.index(TargetedText)])
        # print(cipherToPlainWithKey(TargetedText, kgs[idx], verbose=False))

        i+=1

    for i in range(len(CtPairList)):
        saveOutputKey(CtPairList[i][0], CtPairList[i][1], filenames[i], outdir=outdir)

main(*argv)