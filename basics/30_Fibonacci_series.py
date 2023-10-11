def fibonacci(n):
    if (n == 1 or n == 0):
        return 0
    else:
        f0 = 0
        f1 = 1
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter the no of times u want it: "))
print(f"The fibonacci series for {n} times is {fibonacci(n)}")
    