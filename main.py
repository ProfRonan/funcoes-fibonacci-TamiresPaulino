def fibonacci (n): 
    if n < 0:
        raise ValueError("n tem que ser maior do que zero")
    fibonacci = [0,1]
    while len(fibonacci) < n + 1:
        prox_fibonacci = fibonacci [-1] + fibonacci[-2]
        fibonacci.append(prox_fibonacci)
    return fibonacci [n]

if __name__ == '__main__':
    a = int(input('N:'))
    print(fibonacci(a))
