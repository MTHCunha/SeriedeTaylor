import math

def taylor_sen(x, max_error):
    a = 0
    n = 0
    result = 0
    error = max_error + 1
    while error > max_error:
        if n == 0:
            term = x
        elif n % 2 == 1:
            term = -x**(2*n+1) / math.factorial(2*n+1)
        else:
            term = x**(2*n+1) / math.factorial(2*n+1)
        result += term
        n += 1
        error = abs(term * x**(n) / math.factorial(n))
    return result

def diferenca(f, seno):
    diferenca = f - math.sin(seno)
    return diferenca

def k(x, max_error):
    a = 0
    n = 0
    result = 0
    error = max_error + 1
    while error > max_error:
        if n == 0:
            term = x
        elif n % 2 == 1:
            term = -x ** (2 * n + 1) / math.factorial(2 * n + 1)
        else:
            term = x ** (2 * n + 1) / math.factorial(2 * n + 1)
        result += term
        n += 1
        error = abs(term * x ** (n) / math.factorial(n))
    return n

print("Valor da função: ",taylor_sen(0.3, 0.000000001))
print(k(0.3, 0.000000001))
print("Diferença entre o valor calculado e o real: ",diferenca(taylor_sen(0.3, 0.000000001), 0.3))