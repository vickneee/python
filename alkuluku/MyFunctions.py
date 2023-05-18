def IsPrime(n):
    Factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            Factors.append(i)
    if len(Factors) == 2:
        return [Factors, True]
    else:
        return [Factors, False]
