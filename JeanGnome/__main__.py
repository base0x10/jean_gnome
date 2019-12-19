#!/usr/bin/env python3

doc = """
JeanGnome is a program which uses genetic algorithms to evolve and optimize redcode programs
"""

import argparse
import os
import evolver

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=doc)
    parser.add_argument("mars", type=str, help="Path to a mars emulator executable")
    parser.add_argument(
        "popdir",
        type=str,
        help="Path to a directory where JeanGnome can store populations",
    )

    args = parser.parse_args()
    try:
        os.popen(args.mars).read().split(" ")[0]
        os.path.isdir(args.popdir)
    except:
        print("Invalid arguments")

    flist = os.listdir(args.popdir)
    ev = evolver.evolver(args.mars, args.popdir, population_seed=flist)
    ev.evolve()
