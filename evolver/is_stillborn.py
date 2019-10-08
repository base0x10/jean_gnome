#!/usr/bin/env python3
import sys
import os

def is_stillborn(fname):
    if os.path.exists(fname + ".red"):
        fname = fname + ".red"
    else:
        if not os.path.exists(fname):
            return -1
        os.system('python3 bin2rc.py %s' % fname)
        fname = fname + ".red"
        if not os.path.exists(fname):
            return -1
    res = os.popen('./exmars -c 100 %s' % fname).read().split(" ")
    if res[0][0] != "1":
        return -1
    return 0
    print(res)

if __name__ == "__main__":
    exit(is_stillborn(sys.argv[1]))
