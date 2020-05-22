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

def getEkok(number1,number2):
	ekok=1
	ekokList=[]
	for i in range(2,int(number1+1)):
		divisor = getDivisor(number1,number2)
		if(divisor!=0):
			ekokList.append(divisor)
			number1=number1/divisor
			number2=number2/divisor
	for e in ekokList:
		ekok*=e
	ekok*=number1
	ekok*=number2
	return int(ekok)

sayi1 = abs(int(input("Lütfen Bir Sayi giriniz :")))
sayi2 = abs(int(input("Lütfen Bir Sayi giriniz :")))
if(sayi1>sayi2):
	ekok = getEkok(sayi1,sayi2)
else:
	ekok = getEkok(sayi2,sayi1)
print(sayi1,"ve",sayi2,"değerlerinin EKOK'u :",ekok)