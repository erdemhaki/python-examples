import sys


a = 100


def faktoriyel(x):
	result = 1
	for i in range(1,x+1):
		result = result * i
	return result



def faktoriyel2(y):
	if y == 1:
		return 1
	else:
		return y * faktoriyel(y-1)
		
print faktoriyel(a)