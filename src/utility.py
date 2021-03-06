import os
import copy
import time
import random
from directions import *

def show(cube: list):

    for face in cube:
        for side in face:
            index = 0
            for square in side:
                if square.lower() == "g":
                    side[index] = "\033[1;32;40mg\033[1;37;40m"
                elif square.lower() == "r":
                    side[index] = "\033[1;31;40mr\033[1;37;40m"
                elif square.lower() == "b":
                    side[index] = "\033[1;34;40mb\033[1;37;40m"
                elif square.lower() == "o":
                    side[index] = "\033[1;35;40mo\033[1;37;40m"
                elif square.lower() == "y":
                    side[index] = "\033[1;33;40my\033[1;37;40m"
                index += 1

    middle = [cube[1], cube[2], cube[3], cube[4]]

    for side in cube[0]:
        print(" " * 7, end ="")
        print(" ".join(side), end="\n")

    for face in middle:
        newline = "\n" if middle.index(face) == len(middle) - 1 else "  "
        print(" ".join(face[0]) + newline, end="")
    for face in middle:
        newline = "\n" if middle.index(face) == len(middle) - 1 else "  "
        print(" ".join(face[1]) + newline, end="")
    for face in middle:
        newline = "\n" if middle.index(face) == len(middle) - 1 else "  "
        print(" ".join(face[2]) + newline, end="")
    for side in cube[5]:
        print(" " * 7, end="")
        print(" ".join(side))

def shuffle(cube: list, progress: int = 0.1) -> list:

    shuffled_cube = copy.deepcopy(cube)

    for _ in range(1, 100):
        chosen_func  = random.choice([u, l, f, r, b, d, u_, l_, f_, r_, b_, d_])
        shuffled_cube = chosen_func(shuffled_cube)
        if progress:
            show(shuffled_cube)
            time.sleep(progress)
            os.system("cls")

    return shuffled_cube
