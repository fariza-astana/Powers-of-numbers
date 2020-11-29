def power():
    a = int(input())
    n = int(input())
    if a != 0:
        if n % 2 == 0:
            step1 = (a ** 2)**(n//2)
            print(step1)
        power()
        if n % 2 != 0:
            step2 = a * (a**(n-1))
            print(step2)
        power()
power()
