import random
import time

class cpu():
	def __init__(self,product="intel",model="i7"):
		self.product = product
		self.model = model
	def __str__(self):
		return self.product,self.model

class Bilgisayar():

	def __init__(self,pcStatus="Kapali",case="CoolerMaster",ram=[4], cpu=cpu()):
		self.pcStatus = pcStatus
		self.case = case
		self.ram = ram
		self.cpu = cpu
		print(cpu)
	def __str__(self):
		return """
Bilgisayar Ozellikleri

PC Durumu : {}

Kasa : {}

Ram : {}

GPU Product : 

GPU Model : 

GPU Ram : 

GPU Fan : 

CPU Product : 

CPU Model : 
""".format(self.pcStatus,self.case,str(self.ram))


pc1 = Bilgisayar()

print(pc1)
