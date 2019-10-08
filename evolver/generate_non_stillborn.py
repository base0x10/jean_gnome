#!/usr/bin/env python3
import is_stillborn
import os
import sys
def main():
    fname = sys.argv[1]
    while True:
        with open(fname, "wb+") as f:
            f.write(os.urandom(601))
        if is_stillborn.is_stillborn(fname) == 0:
            print("Found one")
            exit(0)
        os.remove(fname)
        os.remove(fname + ".red")
        

if __name__ == "__main__":
    main()
