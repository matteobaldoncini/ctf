m = list()
with open("/home/matteo/Scaricati/message(1).enc","r") as f:
	for riga in f:
		m.append(bytes.fromhex(riga.strip()))

xoreds = {}
for i in range(len(m)):
	for j in range(len(m)):
		if i<j:
			new = bytes([x^y for x,y in zip(m[i], m[j])])
			xoreds[f"{i}-{j}"] = new
			print(new)


for s in xoreds.items():
	x = s[1]
	print(s[1])

