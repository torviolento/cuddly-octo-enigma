list = []
for i in range (0,1000):
	try:
		chr(i)
	except:
		list.append(i)

for l in list:
	print l,
		
	
