def fibonacci(num):
    fib_list = [0,1]
    while len(fib_list) < num:
        x = fib_list[len(fib_list)-1]
        y = fib_list[len(fib_list)-2]
        fib_list.append(x + y)
        return fib_list