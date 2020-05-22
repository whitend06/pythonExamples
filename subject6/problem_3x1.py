def checkMukemmel(sayi):
	toplam = 0
	for i in range(1,int(sayi/2)+1):
		if(sayi%i==0):
			toplam+=i
	if(toplam==sayi):
		return True
	else:
		return False
for sayi in range(1,1001):
	if(checkMukemmel(sayi)):
		print(str(sayi)+" sayısı mükemmel sayıdır.")
