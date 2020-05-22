kilo = abs(int(input("Kilonuz :")))
boy = abs(float(input("Boyunuz :")))


endex = kilo/(boy*boy)
if(endex<1.85):
	print("Zayıf")
elif(endex<25):
	print("Normal")
elif(endex<30):
	print("Fazla Kilolu")
else:
	print("Obez")	

