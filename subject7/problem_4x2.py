import white

def help():
	print("Welcome to Python Advanced Calcultor")
	print("")
	print("h  : Help")
	print("+  : Toplama")
	print("-  : Çıkartma")
	print("*  : Çarpma")
	print("/  : Bölme")
	print("1  : Get Absolute Value from Integer")
	print("2  : Get Absolute Value from Float")
	print("3  : Get Factoriel")
	print("4  : Get Float Floor")
	print("5  : Get Left Behind After Mod")
	print("6  : Get Sum in a Array Elements")
	print("7  : Get Hypotenuse from Given 2 Edge")
	print("8  : Get Logarithm in 10 Base")
	print("9  : Get Power")
	print("10 : Get Square Root Given Number")
print("")
help()
choice = str(input("Choice : "))
while True:
	#values = str(input("Numbers (seperate with cama (,) if necessary) : "))
	if(choice=="1"):
		value = int(input("Number : "))
		result = int(abs(value))
		print("Result is : "+str(result))
	elif(choice=="2"):
		value = float(input("Number : "))
		result = float(white.fabs(value))
		print("Result is : "+str(result))
	elif(choice=="3"):
		value = abs(int(float(input("Number : "))))
		result = int(white.factorial(value))
		print("Result is : "+str(result))
	elif(choice=="4"):
		value = float(input("Number : "))
		result = int(white.floor(value))
		print("Result is : "+str(result))
	elif(choice=="5"):
		value = float(input("Number : "))
		mod = float(input("mod : "))
		result = float(white.fmod(value,mod))
		print("Result is : "+str(result))
	elif(choice=="6"):
		values = []
		while True:
			value = input("Number (q for calculate): ")
			if(value=="q"):
				break
			else:
				values.append(float(value))
				print("current numbers : "+''.join(str(values)))
		result = float(white.fsum(values))
		print("Result is : "+str(result))
	elif(choice=="7"):
		parendicular = float(input("Parendicular Edge : "))
		base = float(input("Base Edge : "))
		result = float(white.hypot(parendicular,base))
		print("Result is : "+str(result))
	elif(choice=="8"):
		value = float(input("Number : "))
		result = white.log10(value)
		print("Result is : "+str(result))
	elif(choice=="9"):
		base = float(input("Base : "))
		power = float(input("Power : "))
		result = float(white.pow(base,power))
		print("Result is : "+str(result))
	elif(choice=="10"):
		value = float(input("Number : "))
		result = float(white.sqrt(value))
		print("Result is : "+str(result))
	elif(choice=="+"):
		number1 = float(input("1. Number : "))
		number2 = float(input("2. Number : "))
		result = number1+number2
		print("Result is : "+str(result))
	elif(choice=="-"):
		number1 = float(input("1. Number : "))
		number2 = float(input("2. Number : "))
		result = number1-number2
		print("Result is : "+str(result))
	elif(choice=="*"):
		number1 = float(input("1. Number : "))
		number2 = float(input("2. Number : "))
		result = number1*number2
		print("Result is : "+str(result))
	elif(choice=="/"):
		number1 = float(input("1. Number : "))
		number2 = float(input("2. Number : "))
		result = number1/number2
		print("Result is : "+str(result))
	elif(choice=="h" or choice=="help"):
		help()
	elif(choice=="quit" or choice=="q"):
		break
	else:
		print("incorrect choice")
	print("")
	print("h  : Help")
	#print("q : Exit")
	choice = str(input("Choice : "))
