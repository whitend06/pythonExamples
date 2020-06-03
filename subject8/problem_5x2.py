import random
import time

class Bilgisayar():

	def __init__(self,pcStatus="Kapalı",case="CoolerMaster",price=8500,ram=[4,2],gpu_product="Nvidia",gpu_model="1070",gpu_ram=8,gpu_fan=3, cpu_product="intel",cpu_model="i7"):
		self.pcStatus = pcStatus
		self.case = case
		self.ram = ram
		self.gpu_product = gpu_product
		self.gpu_model = gpu_model
		self.gpu_ram = gpu_ram
		self.gpu_fan = gpu_fan
		self.cpu_product = cpu_product
		self.cpu_model = cpu_model
		self.price = price
	def __str__(self):
		return """
Bilgisayar Özellikleri

PC Durumu : {}

Kasa : {}

Ram : {}

GPU Product : {}

GPU Model : {}

GPU Ram : {}

GPU Fan : {}

CPU Product : {}

CPU Model : {}
""".format(self.pcStatus,self.case,self.ram,self.gpu_product,self.gpu_model,self.gpu_ram,self.gpu_fan,self.cpu_product,self.cpu_model)
	def __len__(self):
		return self.price
	def pc_ac(self):
		print("Computer Openning")
		time.sleep(1)
		print("""
			//        //  ////      //  //        //  \\     //
			//            // //     //  //        //   \\   //
			//        //  //  //    //  //        //    \\ // 
			//        //  //   //   //  //        //      // 
			//        //  //    //  //  //        //     // \\ 
			//        //  //     // //  //        //    //   \\
			////////  //  //      ////  ////////////   //     \\
			""")
		time.sleep(1)
		print("Welcome...")
		self.pcStatus = "Açık"
	def pc_kapat(self):
		print("Computer Shuting Down. . .")
		time.sleep(2)
		print("Good Bye...")

	def fiyat_belirle(self):
		while True:
			secim=input("Fiyat Azalt: '-'\nFiyat Artır: '+'\nÇıkış : q\n")
			if(secim == "-"):
				if(self.price != 5000):
					self.price-=250
					print("Fiyat : ",self.price)
				else:
					print("Fiyat 5000 Tl Altı Olamaz. .")
			elif(secim == "+"):
				if(self.price != 15000):
					self.price += 250
					print("Fiyat : ",self.price)
				else:
					print("Fiyat 15000 Tl Üstü Olamaz. .")
			elif(secim=="q"):
				print("Fiyat Güncellendi:",self.price)
				break
			else:
				print("Geçersiz Input")

	def ram_ekle(self,yeni_ram):
		print("Ram ekleniyor...")
		if(len(self.ram)<5):
			if(self.pcStatus=="Açık"):
				self.pc_kapat()
				self.ram.append(yeni_ram)
				print("Ram Eklendi....")
				self.pc_ac()
			else:
				self.ram.append(yeni_ram)
				print("Ram Eklendi....")
			self.price += yeni_ram*150
		else:
			print("4 Ram Slotuda Doludur")
	def ram_cikart(self):
		i=0
		print("çıkartmak istediğiniz rami slotunu seçiniz..")
		for ram in self.ram:
			print(str(i+1)+" : "+str(self.ram[i]))
			i+=1
		slot = input("Seçim :")
		if(0<=int(slot)<=3):
			self.price -= yeni_ram*self.ram[int(slot)]
			self.ram.pop(int(slot)-1)

pc1 = Bilgisayar()
#print(len(pc1))
#pc1.pc_ac()
#pc1.pc_kapat()
#pc1.fiyat_belirle()
#pc1.ram_ekle(8)
#pc1.ram_cikart()
#print(pc1)


print("""
Televizyon Uygulaması
1. Bilgisayarı Aç

2. Bilgisayarı Kapat

3. Fiyat Ayarları

4. Ram Ekle

5. Ram Çıkart

6. Fiyatı Göster

7. Televizyon Bilgileri

Çıkmak için 'q' ya basın.
""")
while True:
	islem = input("İşlemi Seçiniz :")

	if(islem=="q"):
		print("Program sonlandırılıyor....")
		break
	elif(islem=="1"):
		pc1.pc_ac()
	elif(islem=="2"):
		pc1.pc_kapat()
	elif(islem=="3"):
		pc1.fiyat_belirle()
	elif(islem=="4"):
		while True:
			yeni_ram = int(input("Eklemek İstediğiniz Ram Miktarını Giriniz (1,2,4,8,16)\nÇıkış için : 0 : "))
			if(yeni_ram in (1,2,4,8,16)):
				pc1.ram_ekle(yeni_ram)
			elif(yeni_ram==0):
				break
			else:
				print("Geçersiz Input. .")
	elif(islem=="5"):
		pc1.ram_cikart()
	elif(islem=="6"):
		print(len(pc1))
	elif(islem=="7"):
		print(pc1)
	else:
		print("Geçersiz İşlem")
		continue
