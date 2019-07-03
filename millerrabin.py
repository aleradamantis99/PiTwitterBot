from math import log, ceil
from random import randrange
from time import time
from gmpy2 import mpz, log2, powmod
def is_Miller_prime (x, k):
    if x < 6:
        return [0, 0, 1, 1, 0, 1][x]
    x = mpz (x)
    """
    for i in range (1, int (ceil (log2(x)))):
        m = (x-1)/(2**i)
        if (m.is_integer()) & (m%2 != 0):
            r = i
            break
    """
    
    s, d = 0, x - 1
    while d & 1 == 0:
        s, d = s + 1, d >> 1
    
    for r in range (0, k):
        a = randrange (2, x-2)
        b = powmod (a, int (d), x)
        if b == 1 or b == x-1:
            continue
        for i in range (0, s):
            b = powmod (b, 2, x)
            if b == 1:
                return 0
            if b == x-1:
                break
        else:
            return 0
    return 1

if __name__ == "__main__":
	while True:
		num1 = int (input("Primer número: "))
		if num1&1 == 0:
		    num1 +=1
		num2 = int (input("Segundo número: "))
		k = int (input ("Introduzca k( mayor k implica mayor precisión, pero más tiempo): "))
		s = 0
		tiempoin = time()
		
		for i in range (num1, num2, 2):
		    if is_Miller_prime (i, k):
		        s +=1
		        print (i, "es primo")
		
		tiempofin = time ()
		tiempo = tiempofin - tiempoin
		
		print (s)
		print (tiempo)
		input ()
