sayilar = []

sayi1 = abs(int(input("1. sayıyı giriniz :")))
sayilar.append(sayi1)
sayi2 = abs(int(input("2. sayıyı giriniz :")))
sayilar.append(sayi2)
sayi3 = abs(int(input("3. sayıyı giriniz :")))
sayilar.append(sayi3)

sayilar.sort(reverse=True)
print(sayilar[0])