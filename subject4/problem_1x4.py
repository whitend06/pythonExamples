secim = input("Üçgen mi Dörtgen mi:")
kenarlar = []

if(secim=="Dörtgen"):
	kenar1 = abs(int(input("1. kenarı giriniz :")))
	kenarlar.append(kenar1)
	kenar2 = abs(int(input("1. kenarı giriniz :")))
	kenarlar.append(kenar2)
	kenar3 = abs(int(input("1. kenarı giriniz :")))
	kenarlar.append(kenar3)
	kenar4 = abs(int(input("1. kenarı giriniz :")))
	kenarlar.append(kenar4)
	kenarlar.sort()
	if(kenar1==kenar2==kenar3==kenar4):
		print("Kare")
	elif(kenar1==kenar2 and kenar3==kenar4):
		print("Dikdörtgen")
	else:
		print("Sıradan Dörtgen")
elif(secim=="Üçgen"):
	kenar1 = abs(int(input("1. kenarı giriniz :")))
	kenarlar.append(kenar1)
	kenar2 = abs(int(input("1. kenarı giriniz :")))
	kenarlar.append(kenar2)
	kenar3 = abs(int(input("1. kenarı giriniz :")))
	kenarlar.append(kenar3)
	if((abs(kenar2-kenar3)<kenar1<(kenar2+kenar3)) and (abs(kenar1-kenar3)<kenar2<(kenar1+kenar3)) and (abs(kenar1-kenar2)<kenar3<(kenar1+kenar2))):
		kenarlar.sort()
		if(kenar1==kenar2 and kenar2==kenar3):
			print("eşkenar üçgen")
		elif(kenarlar[0]==kenarlar[1] or kenarlar[1]==kenarlar[2] or kenarlar[0]==kenarlar[2]):
			print("ikizkenar üçgen")
		else:
			print("Sıradan Üçgen")
	else:
		print("girilen değerler bir üçgen belirtmemektedir.")
else:
	print("Hatalı Giriş")