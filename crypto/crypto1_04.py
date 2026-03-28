from pwn import *
import string

host = "padding.challs.cyberchallenge.it"
port = 9030

print(f"I am connecting to {host}:{port}")

connection = remote(host, port)

flag = "" #flag="CCIT{r3m3mb3r_th3_3cb_p"
m = 31*"a" #m = (31-len(flag))*"a"
alphabet = string.ascii_letters + string.digits + string.punctuation
c=""

while c!="}":
	connection.recvuntil(b"encrypt:")
	connection.sendline(m.encode())
	flag_dec = connection.recvline().strip().split()[-1]
	flag_dec = flag_dec.decode()

	for c in alphabet:
		connection.recvuntil(b"encrypt:")
		print(f"Trying: {m+flag+c}, len:{len(m+flag+c)}")
		connection.sendline((m+flag+c).encode())
		flag_p_dec = connection.recvline().strip().split()[-1]
		flag_p_dec = flag_p_dec.decode()
		print(f"ref: {flag_dec[:32]}\tflag_p: {flag_p_dec[:32]}")

		if flag_dec[32:64] in flag_p_dec[32:64]:
			m = m[1:]
			flag = flag + c
			print(flag)
			break
