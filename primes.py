

def isPrime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	elif n % 2 == 0:
		return False
	else:
	    for x in range(3, n, 2):
		    if n % x == 0:
			    return False
		    else:
			    return True
def primes(p):
	nums = []
	for x in range(0, p+1):
		if isPrime(x):
			nums.append(x)
	return nums


print primes(20)