def fibonacci(num):
    fib_list = [0,1]
    while len(fib_list) < num:
        x = fib_list[len(fib_list)-1]
        y = fib_list[len(fib_list)-2]
        fib_list.append(x + y)
        return fib_list

def fibo_sum(num, radix=None):
	fib_list = [0,1]
	while len(fib_list) <= num:
		x = fib_list[len(fib_list)-1]
		y = fib_list[len(fib_list)-2]
		fib_list.append(x + y)
		thesum = 0
		if radix == None:
			for i in fib_list:
				thesum += i
			return thesum
		elif radix == "even":
			for i in fib_list:
				fib_list_even = []
			if i % 2 == 0:
				fib_list_even.append(i)
			for i in fib_list_even:
				thesum += i
			return thesum
		elif radix == "odd":
			for i in fib_list:
				fib_list_odd = []
			if i % 2 != 0:
				fib_list_odd.append(i)
			for i in fib_list_odd:
				thesum += i
			return thesum
