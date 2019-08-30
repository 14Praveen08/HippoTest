size = int(input())
price = list(map(int,input().split(" ")))
n = len(price)
profit = [0]*n
maxprice = price[n-1]
for i in range(n-2,0,-1):
	if price[i]>maxprice:
		maxprice = price[i]
	profit[i]=max(profit[i+1],maxprice - price[i])
minprice = price[0]
for i in range(1,n):
	if price[i] < minprice:
		minprice = price[i]
	profit[i]=max(profit[i-1],profit[i]+(price[i]-minprice))
result=profit[n-1]
print(result)
