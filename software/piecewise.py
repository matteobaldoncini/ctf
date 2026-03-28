from pwn import *

host = "piecewise.challs.cyberchallenge.it"
port = 9110


if __name__ == "__main__":
    req = remote(host, port)
    flag = ""

    while flag == "" or flag[-1] != "}":
        line = req.recvline()
        line = line.decode().strip()
        # print(line)
        if "number" in line:
            args = line.split()
            num = int(args[5])
            byte = int(int(args[8][:2]) / 8)
            endianess = args[9][:-7]
            msg = num.to_bytes(byte, byteorder=endianess)
            req.send(msg)
        elif "empty line" in line:
            req.send(b"\x0a")

        req.recvuntil(b"flag: ")
        flag = req.recvline().decode().strip()
        print(flag)

    print(f"\nflag: {flag}\n")
    req.close()
    exit(0)
