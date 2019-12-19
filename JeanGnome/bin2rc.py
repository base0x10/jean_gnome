#!/usr/bin/env python3

import sys
import mmap
import os


def convert_instr(data):
    """
    jean_gnome operates on files of a fixed length in bytes,
    as a bitvector.  bin2rc converts from that file to a warrior:
    it is a surjective but not injective mapping.  Each warrior
    is mapped to by some bit-vector.  Two bit-vectors may map
    to the same warrior.  

    Each warrior is exactly 100 instructions long
    The 0th byte modulo 100 indicates which instruction
    will have the ORG label.

    There are 17*7*8*8 implemented Opcode/modifiers/a_mode/b_mode
    So two bytes are used to identify one instruction.  The specific mapping
    maps all-zero vectors to DAT.F #0, #0 which is the initial instruction in
    the core
    
    there are 100 2-byte instructions

    file[0] = ORG label specifier
    file[1:7] instruction 0
    ...
    file[595:601] instruction 99

    each instruction is first two bytes for an Opcode/modifier/a_mode/b_mode
    second two bytes are a_field, third two bytes is b_field.  Ultimately each
    is 6 bytes
    """

    # 5 bits
    opcodes = [
        "DAT",
        "MOV",
        "ADD",
        "SUB",
        "MUL",
        "DIV",
        "MOD",
        "JMP",
        "JMZ",
        "JMN",
        "DJN",
        "SPL",
        "SLT",
        "CMP",
        "SEQ",
        "SNE",
        "NOP",
    ]
    # 3 bits
    modifiers = ["F", "A", "B", "BA", "AB", "X", "I"]

    # 3 bits
    modes = ["#", "$", "@", "<", ">", "*", "{", "}"]

    instr_number = (data[0] << 8) | data[1]
    a_val = ((data[2] << 8) | data[3]) % 8000
    b_val = ((data[4] << 8) | data[5]) % 8000

    op_str = opcodes[(instr_number & 0b11111) % len(opcodes)]
    instr_number >>= 5

    modifier_str = modifiers[(instr_number & 0b111) % len(modifiers)]
    instr_number >>= 3

    modes_str_a = modes[(instr_number & 0b111) % len(modes)]
    instr_number >>= 3

    modes_str_b = modes[(instr_number & 0b111) % len(modes)]
    instr_number >>= 3
    return "%s.%s %s%d, %s%d\n" % (
        op_str,
        modifier_str,
        modes_str_a,
        a_val,
        modes_str_b,
        b_val,
    )


def convert_mapped_file(mm):
    org = mm[0] % 100
    lines = [convert_instr(mm[1 + 6 * i : 1 + i + 6 * (i + 1)]) for i in range(0, 100)]

    lines[org] = "START " + lines[org]
    asm = "".join(lines)
    return "ORG START\n" + asm + "\n"


def convert_file(fname):
    try:
        flen = os.stat(fname).st_size
        assert flen == 1 + 6 * 100
    except:
        return None
    else:
        with open(fname, "r+b") as hex_warrior_file:
            mm = mmap.mmap(hex_warrior_file.fileno(), 0)
            redcode_warrior = convert_mapped_file(mm)
        with open(fname + ".red", "w") as redcode:
            redcode.write(redcode_warrior)

        return fname + ".red"


# operate as a stand alone shell program
if __name__ == "__main__":
    try:
        fname = sys.argv[1]
        res_fname = convert_file(fname)
        if not res_fname:
            print("Issue opening source or destination file")
            exit(1)
        print("Formatted %s as %s" % (fname, res_fname))
    except:
        print("Issue with input.  Call with `bin2rc.py <path to binary file>`")
