def isprime(num):
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break

    return True if flag == 0 else False


def primerange(low, upper):
    for num in range(low, (upper + 1)):
        if isprime(num):
             print(num)

primerange(10, 50)
