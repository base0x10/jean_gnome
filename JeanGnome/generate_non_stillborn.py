#!/usr/bin/env python3
import is_stillborn
import os
import sys


def generate_non_stillborn(fname, mars):
    while True:
        with open(fname, "wb+") as f:
            f.write(os.urandom(601))
        if is_stillborn.is_stillborn(fname, mars) == 0:
            return
        os.remove(fname)
        os.remove(fname + ".red")


if __name__ == "__main__":
    generate_non_stillborn(sys.argv[1])
