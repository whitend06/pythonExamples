def onlar(onluk):
	if(onluk==1):
		return "On"
	elif(onluk==2):
		return "Yirmi"
	elif(onluk==3):
		return "Otuz"
	elif(onluk==4):
		return "Kırk"
	elif(onluk==5):
		return "Elli"
	elif(onluk==6):
		return "Altmış"
	elif(onluk==7):
		return "Yetmiş"
	elif(onluk==8):
		return "Seksen"
	elif(onluk==9):
		return "Doksan"

def birler(birlik):
	if(birlik==0):
		return ""
	elif(birlik==1):
		return "Bir"
	elif(birlik==2):
		return "İki"
	elif(birlik==3):
		return "Üç"
	elif(birlik==4):
		return "Dört"
	elif(birlik==5):
		return "Beş"
	elif(birlik==6):
		return "Altı"
	elif(birlik==7):
		return "Yedi"
	elif(birlik==8):
		return "Sekiz"
	elif(birlik==9):
		return "Dokuz"

while True:
	sayi = abs(int(input("Lütfen Bir Sayi giriniz :")))
	if(10<=sayi and sayi<100):
		break
	else:
		print("Lütfen 2 basamaklı sayılar giriniz")
onlar = onlar(int(sayi/10))
birler = birler(int(sayi%10))
print(onlar,birler)