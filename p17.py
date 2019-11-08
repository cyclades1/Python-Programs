'''input
13
'''
n = int(input())
if n == 1:
	print("1")
else:
	ans = 1
	for i in range(1,n+1):
		ans *= i;
	print(ans)