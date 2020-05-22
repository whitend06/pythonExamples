vize1 = abs(int(input("1. vize :")))
vize2 = abs(int(input("2. vize :")))
final = abs(int(input("Final :")))

toplam = 0

toplam = (vize1/100*30)+(vize2/100*30)+(final/100*40)

if(toplam>=90):
	print("AA")
elif(toplam>=85):
	print("BA")
elif(toplam>=80):
	print("BB")
elif(toplam>=75):
	print("CB")
elif(toplam>=70):
	print("CC")
elif(toplam>=65):
	print("DC")
elif(toplam>=60):
	print("DD")
elif(toplam>=55):
	print("FD")
else:
	print("FF")