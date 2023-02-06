from cleanup import *
from vig_encrypt import *
import matplotlib.pyplot as plt
import numpy as np
import math

import os
from extractfile import RealFreq, alphalist, keyshift


def plot_axis(ax, x, y, title="", label='', colour='g', width = 0.33, shift=0):
    plt.style.use('_mpl-gallery')
    if label == '':
        ax.bar(x,y,colour)
    else:
        ax.bar(x+shift, y, width=width,color=colour,edgecolor=colour,linewidth=0,label=label)
        ax.legend(loc='upper left')
    ax.set_title(title)
    ax.xaxis.set_visible(False)
    # ax.set_ylim([min(y) - np.std(y), max(y) + np.std(y)])
    # ax.set_xlim([min(x), max(x)])
    ax.set_ylim([0, 11])
    ax.set_xlim([min(x), max(x)])
    ax.set_xticks(x+shift)
    ax.grid(True)

def plot_full_v2(data, isolate=-1, width=0.2):
    xaxis = []
    for i in range(len(data[0])):
        xaxis.append(i)
    
    inputX = np.array(xaxis)

    axi = [plt.axis]*4
    fig, axi = plt.subplots(nrows=4, figsize=(22,9), sharex=True)
    if isolate>0:
        width=0.5
    for i in range(4):
        if isolate==-1:
            plot_axis(axi[i], inputX, RealFreq, 'REAL', label='REAL', colour='black', width=width*5, shift=0.4)
            plot_axis(axi[i], inputX, data[0+4*i], str(1+4*i), label=str(1+4*i), colour='r', shift=width, width=width)
            plot_axis(axi[i], inputX, data[1+4*i], str(2+4*i), label=str(2+4*i), colour='darkgreen', shift=width*2, width=width)
            plot_axis(axi[i], inputX, data[2+4*i], str(3+4*i), label=str(3+4*i), colour='c', shift=width*3, width=width)
            plot_axis(axi[i], inputX, data[3+4*i], str(4+4*i), label=str(4+4*i), colour='y', shift=width*4, width=width)
        else:
            plot_axis(axi[i], inputX, RealFreq, 'REAL', label='REAL', colour='black', width=width*2-0.1, shift=0.4)
        if isolate==0:
            plot_axis(axi[i], inputX, data[0+4*i], str(1+4*i), label=str(1+4*i), colour='r', shift=width, width=width)
        elif isolate==1:
            plot_axis(axi[i], inputX, data[1+4*i], str(2+4*i), label=str(2+4*i), colour='g', shift=width, width=width)
        elif isolate==2:
            plot_axis(axi[i], inputX, data[2+4*i], str(3+4*i), label=str(3+4*i), colour='b', shift=width, width=width)
        elif isolate==3:
            plot_axis(axi[i], inputX, data[3+4*i], str(4+4*i), label=str(4+4*i), colour='magenta', shift=width, width=width)

def plot_guess(data, isolate=1):
    isolate-=1
    width=0.5
    xaxis = []
    for i in range(29):
        xaxis.append(i)
    
    inputX = np.array(xaxis)

    axi = [plt.axis]*29
    fig, axi = plt.subplots(nrows=29, figsize=(22,60), sharex=True)
    
    moving = []
    for i in data[isolate]:
        moving.append(i)
    
    for i in range(29):
        plot_axis(axi[i], inputX, RealFreq, 'REAL', label='REAL', colour='black', width=width*2-0.1, shift=0.4)
        plot_axis(axi[i], inputX, moving, str(alphalist[i]), label=str(alphalist[i]), colour='r', shift=width, width=width)
        
        save = moving.pop(0)
        moving.append(save)

def plot_guess2(data, isolate=1):
    isolate-=1
    width=0.5
    xaxis = []
    for i in range(29):
        xaxis.append(i)
    
    inputX = np.array(xaxis)

    axi = [plt.axis]*29
    fig, axi = plt.subplots(nrows=29, figsize=(22,60), sharex=True)
    
    moving = []
    for i in data[isolate]:
        moving.append(i)
    
    for i in range(29):
        plot_axis(axi[i], inputX, RealFreq, 'REAL', label='REAL', colour='black', width=width*2-0.1, shift=0.4)
        plot_axis(axi[i], inputX, moving, str(alphalist[i]), label=str(alphalist[i]), colour='r', shift=width, width=width)
        
        save = moving.pop(0)
        moving.append(save)



