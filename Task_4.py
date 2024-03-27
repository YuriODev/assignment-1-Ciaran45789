# Your solution comes here
n = int(input("Enter a number above 20 to countdown from: "))
if n < 20: quit()

for i in range(20, n+1):
    print(i, end=' ')