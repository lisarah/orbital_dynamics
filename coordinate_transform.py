# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:22:53 2023

@author: Sarah Li
"""
import numpy as np
from math import sin, cos

""" Earth's standard gravitational parameter GM_e."""
_MU  = 3.986e5 # km^3 s^-2


def threeOneThree_rot(a1, a2, a3):
    """ Return the 313 rotation matrix for Euler angles. 
    
    Input: 
        a1: rotation 1 about axis 3 (in degrees).
        a2: rotation 2 about axis 1 (in degrees).
        a3: rotation 3 about axis 3 (in degrees).
    """
    E00 = cos(a3)*cos(a1) - sin(a3)*cos(a2)*sin(a1)
    E01 = cos(a3)*sin(a1) + sin(a3)*cos(a2)*cos(a1)
    E02 = sin(a3)*sin(a2)
    E10 = -sin(a3)*cos(a1) - cos(a3)*cos(a2)*sin(a1)
    E11 = -sin(a3)*sin(a1) + cos(a3)*cos(a2)*cos(a1)
    E12 = cos(a3)*sin(a2)
    E20 = sin(a2)*sin(a1)
    E21 = -sin(a2)*cos(a1)
    E22 = cos(a2)
    return np.array([[E00, E01, E02], [E10, E11, E12], [E20, E21, E22]])

def orbital2xyz(Omega, i, w, vector):
    """ Given Omega, i, w, turn a vector from the orbital plane to xyz plane.
    
    Input:
        Omega: Longitude of ascending node.
        i: inclination angle.
        w: argument of the perihelion.
        vector: orbital plane vec in e/p/h basis. 
    """
    rot_mat = threeOneThree_rot(Omega, i, w)
    return rot_mat.T.dot(vector)
    
