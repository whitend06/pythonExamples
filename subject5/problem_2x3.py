print("Çarpım Tablosu")
for i in range(11):
	if(i==0):
		print("X",end='	')
	else:
		print(str(i),end='	')
print("")	
for j in range(1,11):
	print(str(j),end='	')
	for k in range(1,11):
		print(str(j*k),end='	')
	print("")	