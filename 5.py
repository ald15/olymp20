
def su(n):
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s

def main(a, b, s):
	count = 0
	if s % 2 == 1:
		count += 1
	for i in range(a + 1, b + 1):
		if   i % 1000000000 == 0:
			s -= 9 * 9
		elif i % 100000000 == 0:
			s -= 9 * 8
		elif i % 10000000 == 0:
			s -= 9 * 7
		elif i % 1000000 == 0:
			s -= 9 * 6
		elif i % 100000 == 0:
			s -= 9 * 5
		elif i % 10000 == 0:
			s -= 9 * 4
		elif i % 1000 == 0:
			s -= 9 * 3
		elif i % 100 == 0:
			s -= 9 * 2
		elif i % 10 == 0:
			s -= 9 
		s+=1
		if s % 2 == 1:
			#print(i)
			count += 1
	return count

a, b = int(input()), int(input())
sA = su(a)

con = 100000
if a - b <= con:
	count = main(a, b, sA)
else:
	sAM = (a + con - 1) // con * con
	sBM = b // con * con
	cM = main(sAM // con, sBM // con, su(sAM))
	d = sBM - sAM + 1
	r = cM * 49999 + (d - cM) * 50001
	r = main(a, sAM - 1, su(a)) + r + main(sBM, b, su(SBM))
	count = r

print(count)