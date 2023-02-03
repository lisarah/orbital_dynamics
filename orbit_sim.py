# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:50:45 2023

Orbital simulations
@author: Sarah
"""
import numpy as np
import math 
import coordinate_transform as coords


# orbital elements
a = 7300 # km
e = 0.05
i = math.radians(42) # deg
Omega = 0 # deg
w = math.radians(45) # deg
M_0 = 0 # deg


r_0 = np.array([a*(1-e), 0, 0]) # periapsis
v_0 = np.array([0, coords._MU*(2/a/(1-e) - 1/a), 0])
xyz_r_0 = coords.orbital2xyz(Omega, i, w, r_0)
xyz_v_0 = coords.orbital2xyz(Omega, i, w, v_0)