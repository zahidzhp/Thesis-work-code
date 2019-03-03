# -*- coding: utf-8 -*-
"""
Created on Mar 23 11:57 2017

@author: Denis Tome'
"""

__all__ = [
    'VISIBLE_PART',
    'MIN_NUM_JOINTS',
    'CENTER_TR',
    'SIGMA',
    'STRIDE',
    'SIGMA_CENTER',
    'INPUT_SIZE',
    'OUTPUT_SIZE',
    'NUM_JOINTS',
    'NUM_OUTPUT',
    'H36M_NUM_JOINTS',
    'JOINT_DRAW_SIZE',
    'LIMB_DRAW_SIZE'
]

# threshold
VISIBLE_PART = 1e-3
MIN_NUM_JOINTS = 5
CENTER_TR = 0.4

# net attributes
SIGMA = 7
STRIDE = 8
SIGMA_CENTER = 21
INPUT_SIZE = 368
OUTPUT_SIZE = 46
NUM_JOINTS = 14
NUM_OUTPUT = NUM_JOINTS + 1
H36M_NUM_JOINTS = 17

# draw options
JOINT_DRAW_SIZE = .5
LIMB_DRAW_SIZE = .5
NORMALISATION_COEFFICIENT = 1280*720
