print("Çarpım Tablosu")
for i in range(11):
	print(str(i),end='	')
print("")	
for j in range(1,11):
	print(str(j),end='	')
	for k in range(1,11):
		print(str(j*k),end='	')
		#print(str(i),"x",str(j),"=",str(i*j),end='')
	print("")	