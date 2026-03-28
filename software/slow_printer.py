from pwn import *

e = ELF("slow_printer")     # per caricare l'ELF da patchare
context.binary = e      # per impostare l'architettura (x86_64) e l'endianess (big endian, little endian) in relazione al file caricato
e.write(0x4011fe, 5*asm('nop'))       # sostituisce la funzione all'indirizzo specificato con 5 volt nope
e.save('fast_printer')      # per salvare l'ELF in un nuovo file
