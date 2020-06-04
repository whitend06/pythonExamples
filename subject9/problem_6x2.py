def checkEven(num,isList=False):
	if num%2==1:
		if(not isList):
			raise ValueError('"'+str(num)+'" is not a even value.\n')
		else:
			return False
	else:
		return str(num)

val=3
liste=[1,2,3,4,5,6,7,8,9,10]
try:
	print(checkEven(val)+" is a even value.\n\n")
except Exception as e:
	print(e)

for i in liste:
	try:
		a=checkEven(i,True)
		if(not a):
			print(str(i)+" is a even value.\n")
	except Exception as e:
		print(e)
