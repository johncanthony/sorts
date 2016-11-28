def fib(num,a,b):
	
	if(num<=2):
		return b

	num = num - 1 

	
	return fib(num,b,a+b)
