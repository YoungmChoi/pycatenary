#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 01:06:00 2024

@author: yomy
"""

import numpy as np
from pycatenary import cable
from matplotlib import pyplot as plt


# define properties of cable
length = 6.98   # length of line
w = 1.036       # submerged weight
EA = 560e3      # axial stiffness

# length = [6.0, 3.0]
# w = [1.0, 2.0]
# EA = [560e3, 300e3]

floor = True    # if True, contact is possible at the level of the anchor
anchor = [0., 0., 0.]
# fairlead = [5.2, 1., 2.65]
fairlead = [5.2, 0., 2.65]


# create cable instance
l1 = cable.MooringLine(L=length,
                       w=w,
                       EA=EA,
                       anchor=anchor,
                       fairlead=fairlead,
                       floor=floor)

# compute calculations
l1.computeSolution()

s = length

nSegment = 300

sArray = np.linspace(0, length, nSegment)

T   = np.zeros([nSegment, 3])
xyz = np.zeros([nSegment, 3])

# get xyz coordinates along line
for i in range(nSegment):
    T[i] = l1.getTension(sArray[i])
    xyz[i] = l1.s2xyz(sArray[i])

# print("T:", T)
plt.plot(xyz[:, 0], xyz[:, 2])

np.savetxt('linePosition.txt', xyz)
np.savetxt('force.txt', T)

print(T[-1,:])

