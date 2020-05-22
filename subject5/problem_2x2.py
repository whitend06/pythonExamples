sayi = str(abs(int(input("Sayı giriniz :"))))
basamak = len(sayi)
toplam = 0
toplamBasamak = 1
for i in range(basamak):
	for j in range(basamak):
		toplamBasamak*=int(sayi[i])
	toplam+=toplamBasamak
	toplamBasamak=1

if(str(toplam)==sayi):
	print(sayi+" sayısı armstrong sayıdır.")
else:
	print(sayi+" sayısı armstrong sayı değildir.")