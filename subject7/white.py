def topla(num1,num2):
	return num1+num2
def abs(num):
	a=str(num).split(".")
	b=str(a[0])
	if("-"==b[0]):
		return int(b.split("-")[1])
	else:
		return int(b)

def fabs(num):
	a=str(num)
	if("-"==a[0]):
		return float(a.split("-")[1])
	else:
		return float(a)

def factorial(num):
	a=abs(num)
	b=1
	for i in range(1,a+1):
		b*=i
	return b

def floor(num):
	a=str(num)
	if("-"==a[0]):
		return int("-"+str(abs(num)+1))
	else:
		return abs(num)
def fmod(num,base):
	return float(num-int(num/base)*base)

def fsum(nums):
	result=0
	for num in nums:
		result+=num
	return result

def hypot(num1,num2):
	return sqrt(((num1*num1)+(num2*num2)))

def pow(num1,num2):
	result = 1
	for i in range(int(num2)):
		result*=num1
	return float(result)

def sqrt(num):
	a=num
	b=float((a+1)/2)
	while b<a:
		a=b
		b=float((a+float(num/a))/2)
	return a
