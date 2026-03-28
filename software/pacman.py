from pwn import *
import os


e = ELF("./pacman")

e.address = 0x100000

target_add = 0x100E26
new_istruction = b"\xeb\x07"

e.write(target_add, new_istruction)

e.save("./pacman_gdb")
