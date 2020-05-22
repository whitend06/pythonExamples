kareArray=[]
def kareAl(sayi):
	return sayi*sayi
def findHipotenus(a,b):
	hipotenus = kareAl(a)+kareAl(b)
	for c in kareArray:
		if(hipotenus==c):
			return kareArray.index(c)+1
	return 0
for i in range(1,101):
	kareArray.append(kareAl(i))
for a in range(1,101):
	for b in range(1,101):
		c = findHipotenus(a,b)
		if(c!=0):
			print(a,b,c)
