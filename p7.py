'''input
320
'''

n = int(input())
ans =0
if n <=150:
	ans+= n*2.40
elif n >150 and  n<=300:
	ans += (n-150)*3 + 150*2.40
else :
	ans += (n-300)*3.20 + 150*3 + 150*2.40

print("Bill is : " +str(ans))
