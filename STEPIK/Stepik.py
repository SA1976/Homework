def fib(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-2] + fib[i-1])
    return fib[i]

def main():
    n = int(input())
    print(fib(n))



if __name__ == "__main__":
    main()