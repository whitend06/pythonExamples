sayi = abs(int(input("Sayı giriniz :")))
toplam = 0
for i in range(1,int(sayi/2)+1):
	if(sayi%i==0):
		toplam+=i
if(toplam==sayi):
	print(str(sayi)+" sayısı mükemmel sayıdır.")
