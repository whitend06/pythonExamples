def isAsal(number):
	check = 0
	for i in range(2,int(number/2)+1):
		if(number%i==0):
			check=i
	if(check==0):
		return True
	return False

def getDivisor(number1,number2):
	for i in range(2,int(number1+1)):
		if((isAsal(i) and i%2!=0) or i==2):
			if(number1%i==0 and number2%i==0):
				return i
	return 0

def getEbob(number1,number2):
	ebob=1
	ebobList=[]
	for i in range(2,int(number1+1)):
		divisor = getDivisor(number1,number2)
		if(divisor!=0):
			ebobList.append(divisor)
			number1=number1/divisor
			number2=number2/divisor
	for e in ebobList:
		ebob*=e
	return ebob


sayi1 = abs(int(input("Lütfen Bir Sayi giriniz :")))
sayi2 = abs(int(input("Lütfen Bir Sayi giriniz :")))
if(sayi1<sayi2):
	ebob = getEbob(sayi1,sayi2)
else:
	ebob = getEbob(sayi2,sayi1)
print(sayi1,"ve",sayi2,"değerlerinin EBOB'u :",ebob)