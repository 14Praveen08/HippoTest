a=input()
b=input()
n=len(a)
m=len(b)
count = 0
lcs = [[0] * (m + 1) for _ in range(n + 1)]
for i, c1 in enumerate(a):
	for j,c2 in enumerate(b):
		if c1 == c2:
			lcs[i][j] = lcs[i-1][j-1] + 1
		else:
			lcs[i][j] = max(lcs[i][j-1],lcs[i-1][j])
print(lcs[n-1][m-1])
