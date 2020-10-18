import os
import time
import copy
import directions
from utility import *

solved_cube = [
    [
        ["w","w","w"],
        ["w","w","w"],
        ["w","w","w"]
    ],
    [
        ["g","g","g"],
        ["g","g","g"],
        ["g","g","g"]
    ],
    [
        ["r","r","r"],
        ["r","r","r"],
        ["r","r","r"]
    ],
    [
        ["b","b","b"],
        ["b","b","b"],
        ["b","b","b"]
    ],
    [
        ["o","o","o"],
        ["o","o","o"],
        ["o","o","o"]
    ],
    [
        ["y","y","y"],
        ["y","y","y"],
        ["y","y","y"]
    ]
]
cube = copy.deepcopy(solved_cube)

"""

       w w w
       w W w
       w w w
g g g  r r r  b b b  o o o
g G g  r R r  b B b  o O o
g g g  r r r  b b b  o o o
       y y y
       y Y y
       y y y

"""

# Prints solved cube
display_cube(solved_cube)
print("\n\n")
display_cube(shuffle(cube))
