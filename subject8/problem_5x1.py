import random
import time

class Kumanda():

	def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["Trt"],kanal = "Trt",kalan_kullanim=15):

		self.tv_durum = tv_durum
		self.tv_ses = tv_ses
		self.kanal_listesi = kanal_listesi
		self.kanal = kanal
		self.kalan_kullanim = kalan_kullanim

	def tv_ac(self):
		if(self.tv_durum=="Açık"):
			print("Televizyon Zaten Açık....")
		else:
			print("Televizyon Açılıyor....")
			self.tv_durum = "Açık"

	def tv_kapat(self):
		if(self.tv_durum=="Kapalı"):
			print("Televizyon Zaten Kapalı....")
		else:
			print("Televizyon Kapanıyor....")
			self.tv_durum = "Kapalı"

	def ses_ayarları(self):
		while True:
			cevap = input("Sesi Azalt: '<'\nSesi Artır: '>'\nÇıkış : cikis\n")

			if(cevap == "<"):
				if(self.tv_ses != 0):
					self.tv_ses-=1
					print("Ses:",self.tv_ses)
			elif(cevap == ">"):
				if(self.tv_ses != 31):
					self.tv_ses += 1
					print("Ses:",self.tv_ses)
			else:
				print("Ses Güncellendi:",self.tv_ses)
				break
	def kanal_ekle(self,kanal_ismi):
		print("Kanal ekleniyor...")
		time.sleep(1)
		self.kanal_listesi.append(kanal_ismi)
		print("Kanal Eklendi....")

	def rastgele_kanal(self):
		rastgele = random.randint(0,len(self.kanal_listesi)-1)
		self.kanal = self.kanal_listesi[rastgele]
		print("Şu an ki Kanal:",self.kanal)

	def kanallari_sirala(self,reverse=False):
		print("Kanallar Sıralanıyor")
		self.kanal_listesi.sort(reverse=reverse)
		i=1
		for kanal in self.kanal_listesi:
			print(str(i),":",kanal)
			i+=1

	def __len__(self):
		return len(self.kanal_listesi)

	def __str__(self):
		return "Tv Durumu:{}\nTv Ses:{}\nKanal Listesi: {}\nŞu anki Kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

	def kullanim(self):
		self.kalan_kullanim-=1
		if(self.kalan_kullanim==0):
			return False
		elif(self.kalan_kullanim <= 10):
			print("Kalan Kullanım Hakkınız :",self.kalan_kullanim)
		return True

kumanda = Kumanda()

print("""
Televizyon Uygulaması
1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rastgele Kanala Geçme

7. Televizyon Bilgileri

8. Kanalları Sırala

9. Kanalları Tersten Sırala

Çıkmak için 'q' ya basın.
""")
while True:
	islem = input("İşlemi Seçiniz :")

	if(islem=="q"):
		print("Program sonlandırılıyor....")
		break
	elif(islem=="1"):
		kumanda.tv_ac()
	elif(islem=="2"):
		kumanda.tv_kapat()
	elif(islem=="3"):
		kumanda.ses_ayarları()
	elif(islem=="4"):
		kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin : ")
		kanal_listesi = kanal_isimleri.split(",")
		for eklenecekler in kanal_listesi:
			kumanda.kanal_ekle(eklenecekler)
	elif(islem=="5"):
		print("Kanal Sayısı:",len(kumanda))
	elif(islem=="6"):
		kumanda.rastgele_kanal()
	elif(islem=="7"):
		print(kumanda)
	elif(islem=="8"):
		kumanda.kanallari_sirala()
	elif(islem=="9"):
		kumanda.kanallari_sirala(True)
	else:
		print("Geçersiz İşlem")
		continue

	if(not kumanda.kullanim()):
		print("Kumanda Ömrünüz Bitmiştir...\nLütfen Hizmet Sağlayıcınız ile İletişime Geçiniz...")
		break
