m = "104e137f425954137f74107f525511457f5468134d7f146c4c"
m = bytes.fromhex(m)
n = len(m)

for k in range(0x100):	# check all the possible hex key with len = 1 byte
	k = f"{k:02x}"	# k is an integer, so I convert it into an hex string
	k = k*n		# to repeat the key along the all the ciphertext
	k = bytes.fromhex(k)	# convert the key into bytes
	z = bytes([x^y for x,y in zip(m,k)])	# XOR the ciphertext with the key
	if all(33<=b<=126 for b in z):		# to filter the not printable plaintexts
		z = z.decode()	# get the string from the bytes format
		if "_" in z:	# to filter the printable strings which don't contain the "_" character
			print(z)
