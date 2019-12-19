#!/usr/bin/env python3
import sys
import os

import bin2rc

def is_stillborn(fname, mars):
    if os.path.exists(fname + ".red"):
        fname = fname + ".red"
    else:
        if not os.path.exists(fname):
            return -1
        fname = bin2rc.convert_file(fname)
        if not os.path.exists(fname):
            return -1
    res = os.popen("./%s -c 100 %s" % (mars, fname)).read().split(" ")
    if res[0][0] != "1":
        return -1
    return 0


if __name__ == "__main__":
    exit(is_stillborn(sys.argv[1], sys.argv[2]))
