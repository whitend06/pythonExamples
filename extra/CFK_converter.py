def convertF2C(degree):
	return ((degree-32)*(5/9))
def convertK2C(degree):
	return (degree-273.15)
def convertC2K(degree):
	return (degree+273.15)
def convertC2F(degree):
	return((degree*9/5)+32)

while True:
	print("Celsius : C")
	print("Fahrenheit : F")
	print("Kelvin : K")
	print("örneğin: 20.5 C, -35 F, 50 K")
	data = (input("Lütfen Bir Derece ve türünü giriniz :")).upper()

	degree = data.split(" ")[0]
	kind = data.split(" ")[1]
	if((kind=="C" or kind=="K" or kind=="F") and float(degree)):
		degree = float(degree)
		print("===========================================")

		print("Celsius : C")
		print("Fahrenheit : F")
		print("Kelvin : K")
		while True:
			dataCovnert = (input("Lütfen Çevirmek İstediğiniz Türünü Giriniz : ")).upper()
			print("")
			if(dataCovnert=="C" or dataCovnert=="K" or dataCovnert=="F"):
				print("+++++++++++++")
				if(kind=="K"):
					cDegree = convertK2C(degree)
				elif(kind=="F"):
					cDegree = convertF2C(degree)
				else:
					cDegree=degree

				if(dataCovnert=="C"):
					print(str(degree),kind," : ",str(cDegree),"Celsius")
				elif(dataCovnert=="K"):
					kDegree = convertC2K(cDegree)
					print(str(degree),kind," : ",str(kDegree),"Kelvin")
				elif(dataCovnert=="F"):
					fDegree = convertC2F(cDegree)
					print(str(degree),kind," : ",str(fDegree),"Fahrenheit")
				print("+++++++++++++")
				print("")
				print("===========================================")
				print("")
				print("")
				break

			else:
				print("Veri tipi hatalı")



	else:
		print("Veri tipi hatalı")


